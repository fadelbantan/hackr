DEFAULT_CODE = '''#!/usr/bin/env python3
"""Hybrid Recon / Analysis Toolkit
===================================
This synthetic module pretends to implement a multi-stage reconnaissance
and data analysis pipeline combining asynchronous network probing,
log parsing, credential heuristics, and lightweight ML scoring.

Disclaimer: All endpoints, tokens, payloads, and intelligence routines
below are fictitious. This file is used strictly for demo/typing effects.
"""

from __future__ import annotations
import asyncio
import dataclasses
import hashlib
import hmac
import json
import os
import queue
import random
import re
import socket
import struct
import sys
import threading
import time
from base64 import b64encode, b64decode
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Iterable, Union, Callable

# ----------------------------- Utilities ---------------------------------

ENV = os.getenv("APP_ENV", "dev")
START_TS = time.time()
RANDOM_SEED = int(START_TS) % 9973
random.seed(RANDOM_SEED)

HEX = "0123456789abcdef"

def now_ms() -> int:
    return int(time.time() * 1000)

def short_hash(data: Union[str, bytes]) -> str:
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha1(data).hexdigest()[:12]

def secure_compare(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    res = 0
    for x, y in zip(a.encode(), b.encode()):
        res |= x ^ y
    return res == 0

# ----------------------------- Data Classes -------------------------------

@dataclasses.dataclass
class Target:
    host: str
    port: int = 443
    tags: List[str] = dataclasses.field(default_factory=list)
    def label(self) -> str:
        return f"{self.host}:{self.port}" if self.port else self.host

@dataclasses.dataclass
class Finding:
    target: Target
    kind: str
    detail: str
    score: float
    ts_ms: int = dataclasses.field(default_factory=now_ms)
    def to_dict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)

# ----------------------------- Queues -------------------------------------

class WorkQueue:
    def __init__(self) -> None:
        self.q: "queue.Queue[Target]" = queue.Queue()
    def push(self, t: Target) -> None:
        self.q.put(t)
    def pop(self, timeout: float = 0.2) -> Optional[Target]:
        try:
            return self.q.get(timeout=timeout)
        except queue.Empty:
            return None

# ----------------------------- Networking ---------------------------------

async def async_probe(host: str, port: int, timeout: float = 1.2) -> Dict[str, Any]:
    meta: Dict[str, Any] = {"host": host, "port": port, "ok": False, "banner": None, "latency_ms": None}
    start = time.perf_counter()
    try:
        loop = asyncio.get_running_loop()
        fut = loop.getaddrinfo(host, port, type=socket.SOCK_STREAM)
        infos = await asyncio.wait_for(fut, timeout=timeout)
        family, socktype, proto, canon, sockaddr = infos[0]
        s = socket.socket(family, socktype, proto)
        s.settimeout(timeout)
        s.connect(sockaddr)
        try:
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            data = s.recv(128)
            meta["banner"] = data.decode(errors="ignore").strip()
        except Exception:
            meta["banner"] = None
        s.close()
        meta["ok"] = True
    except Exception:
        meta["ok"] = False
    finally:
        meta["latency_ms"] = round((time.perf_counter() - start) * 1000, 2)
    return meta

# ----------------------------- Scoring ------------------------------------

def score_banner(banner: Optional[str]) -> float:
    if not banner:
        return 0.15
    score = 0.3
    patterns = ["Apache", "nginx", "Server", "cloud", "edge"]
    for p in patterns:
        if p.lower() in banner.lower():
            score += 0.1
    if "PHP" in banner:
        score -= 0.05
    return min(max(score, 0.0), 1.0)

# ----------------------------- ML Stub ------------------------------------

class MiniModel:
    def __init__(self) -> None:
        self.coeff = [random.uniform(-0.4, 0.9) for _ in range(5)]
    def infer(self, features: List[float]) -> float:
        acc = 0.0
        for c, f in zip(self.coeff, features):
            acc += c * f
        return 1 / (1 + pow(2.71828, -acc))

MODEL = MiniModel()

# ----------------------------- Credential Heuristics ----------------------

COMMON_SUFFIXES = ["2024", "2025", "prod", "admin", "test", "secure"]

def synthesize_password(seed: str) -> str:
    base = short_hash(seed)
    suffix = random.choice(COMMON_SUFFIXES)
    return base + "!" + suffix

# ----------------------------- Recon Engine -------------------------------

class ReconEngine:
    def __init__(self) -> None:
        self.findings: List[Finding] = []
        self.lock = threading.Lock()
    def record(self, f: Finding) -> None:
        with self.lock:
            self.findings.append(f)
    def summary(self) -> Dict[str, Any]:
        with self.lock:
            return {
                "count": len(self.findings),
                "avg_score": round(sum(f.score for f in self.findings) / max(len(self.findings), 1), 3),
                "top": [f.to_dict() for f in sorted(self.findings, key=lambda x: x.score, reverse=True)[:5]],
            }

ENGINE = ReconEngine()

# ----------------------------- Workers ------------------------------------

def worker_loop(wq: WorkQueue, thread_id: int, stop_evt: threading.Event) -> None:
    while not stop_evt.is_set():
        t = wq.pop()
        if not t:
            continue
        banner = f"Synthetic/{t.host}/{thread_id}" if random.random() < 0.6 else None
        features = [random.random() for _ in range(5)]
        ml_score = MODEL.infer(features)
        b_score = score_banner(banner)
        final = round((ml_score * 0.7) + (b_score * 0.3), 4)
        finding = Finding(target=t, kind="service", detail=banner or "no-banner", score=final)
        ENGINE.record(finding)

# ----------------------------- Orchestrator -------------------------------

class Orchestrator:
    def __init__(self, targets: List[Target], threads: int = 4) -> None:
        self.targets = targets
        self.threads = threads
        self.stop_evt = threading.Event()
        self.wq = WorkQueue()
        for t in targets:
            self.wq.push(t)
        self.workers: List[threading.Thread] = []
    def start(self) -> None:
        for i in range(self.threads):
            th = threading.Thread(target=worker_loop, args=(self.wq, i, self.stop_evt), daemon=True)
            th.start()
            self.workers.append(th)
    def wait(self, timeout: float = 2.0) -> None:
        t0 = time.time()
        while time.time() - t0 < timeout:
            if self.wq.q.empty():
                break
            time.sleep(0.05)
        self.stop_evt.set()
        for th in self.workers:
            th.join(timeout=0.5)
    def export(self) -> str:
        return json.dumps(ENGINE.summary(), indent=2)

# ----------------------------- HMAC Signing -------------------------------

SECRET_KEY = b"demo-secret-key"

def sign_payload(payload: Dict[str, Any]) -> str:
    raw = json.dumps(payload, sort_keys=True).encode()
    digest = hmac.new(SECRET_KEY, raw, hashlib.sha256).digest()
    return b64encode(digest).decode()

# ----------------------------- Log Parser ---------------------------------

LOG_SAMPLE = """
2025-11-01T00:00:01Z conn accepted src=10.0.0.5 dst=10.0.0.9
2025-11-01T00:00:02Z auth fail user=admin ip=10.0.0.5
2025-11-01T00:00:03Z auth success user=deploy ip=10.0.0.6
2025-11-01T00:00:04Z scan detected src=203.0.113.42 vector=tcp-syn
2025-11-01T00:00:05Z conn accepted src=10.0.0.7 dst=10.0.0.9
"""

LOG_PATTERN = re.compile(r"^(?P<ts>\S+) (?P<event>\w+) (?P<data>.+)$")

def parse_logs(text: str) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for line in text.strip().splitlines():
        m = LOG_PATTERN.match(line)
        if not m:
            continue
        row = m.groupdict()
        out.append(row)
    return out

# ----------------------------- Configuration ------------------------------

DEFAULT_TARGETS = [
    Target(host="edge01.internal", port=443, tags=["edge", "tls"]),
    Target(host="api01.internal", port=443, tags=["api", "json"]),
    Target(host="db01.internal", port=5432, tags=["db", "sql"]),
    Target(host="files.internal", port=9000, tags=["object", "storage"]),
]

# ----------------------------- CLI Entrypoint -----------------------------

async def async_stage() -> None:
    # Simulate network probes concurrently
    probes = [async_probe(t.host, t.port) for t in DEFAULT_TARGETS]
    results = await asyncio.gather(*probes)
    for r in results:
        banner = r.get("banner")
        score = score_banner(banner)
        ENGINE.record(Finding(target=Target(r["host"], r["port"]), kind="probe", detail=banner or "none", score=score))

def main() -> None:
    orch = Orchestrator(DEFAULT_TARGETS, threads=3)
    orch.start()
    orch.wait(timeout=1.4)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_stage())
    loop.close()
    payload = ENGINE.summary()
    payload["signed"] = sign_payload(payload)
    print("SUMMARY:\n" + json.dumps(payload, indent=2))
    parsed = parse_logs(LOG_SAMPLE)
    print("\nPARSED_LOGS:")
    for row in parsed:
        print(row)
    print("\nGenerated password sample:", synthesize_password("edge01.internal"))

if __name__ == "__main__":
    main()

# End of synthetic module. Total lines intentionally exceed 300.
'''
