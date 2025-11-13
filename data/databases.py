DATABASES = [

r"""/home/mark/secrets.db
{"user":"mark","email":"mark@supplysphere.io","password_hash":"$argon2id$v=19$m=65536,t=3,p=2$Nf8z...","reset_token":"rt_9c8b7d","reset_expires":"2025-11-02T01:12:00Z"}
{"api_keys":[{"provider":"atlas-pay","key":"pay_live_Z81fdA09vjWb","rotates_after":"2025-12-31"},{"provider":"slack","key":"xoxb-9812734-app"}]}
{"session_token":"st_kA9d-1fcd-3c62","last_ip":"10.42.18.22","user_agent":"Okta-Verify/9.1 (iOS 18.0)","mfa":"totp"}
{"devices":[{"model":"MacBookPro18,3","serial":"C02LM4","last_seen":"2025-10-25T02:42:01Z"},{"model":"Pixel8","last_seen":"2025-10-24T21:18:44Z"}]}
{"oauth_refresh":"1//0g-oauth-refresh-8812","scope":["calendar.read","drive.read"]}
{"notes":"Do not store prod certs locally. Vault path secrets/prod/app"}
""",

r"""/var/www/app/.env
APP_ENV=production
APP_DEBUG=false
DATABASE_URL=postgres://app_admin:p4Tch-H1nt@pg01.helios.internal:5432/app_core
READ_REPLICA_URL=postgres://readonly:r3pl1ca@pg02.helios.internal:5432/app_core
REDIS_URL=redis://cache01.helios.internal:6379/2
SECRET_KEY=sk_live_0c16f2d9c1384c2d8c8a613c725e31ad
PAYMENTS_PRIVATE_KEY=-----BEGIN PRIVATE KEY-----MIICdgIBADANBgkqhkiG9w0B...
OIDC_CLIENT_ID=app-prod-oidc
OIDC_CLIENT_SECRET=oidc_s3cr3t_A991
SENTRY_DSN=https://key@sentry.helios.internal/42
KAFKA_BROKERS=kafka01:9092,kafka02:9092
AWS_ACCESS_KEY_ID=AKIA6PROD9812
AWS_SECRET_ACCESS_KEY=yxZkP0q4Rgrb1XtCBz1/NNx7f6LuB8Klz6jJ7
GCS_SIGNING_KEY_ID=svc-app@helios.gserviceaccount.com
GCS_SIGNING_KEY=-----BEGIN PRIVATE KEY-----MIIEv...
DEPLOY_SHA=7a3c2fd
""",

r"""/var/backups/db_dump_2025_10_24.sql
-- pg_dump all schema public
CREATE TABLE users (
    id uuid PRIMARY KEY,
    email citext UNIQUE NOT NULL,
    password_hash text NOT NULL,
    last_login timestamptz,
    flags jsonb
);
INSERT INTO users VALUES
('b2905cd0-05f8-4f86-9af1-8e9d84c0d83b','alice@supplysphere.io','$2y$12$JHk0s7HnVf8K','2025-10-25 07:11:23+00','{"mfa":true}'),
('8a41f2b1-f738-49fb-bb63-e6c6c7af50a7','bob@supplysphere.io','$2y$12$2G0vGdZPpRag','2025-10-25 06:03:12+00','{"mfa":false}');
CREATE TABLE api_tokens (id serial PRIMARY KEY, token text, owner uuid, expires timestamptz);
INSERT INTO api_tokens VALUES (1,'tok_live_kA61', 'b2905cd0-05f8-4f86-9af1-8e9d84c0d83b','2025-12-01 00:00:00+00');
-- EOF
""",

r"""/home/bob/.credentials.json
{
  "username":"bob",
  "email":"bob.pipeline@helios.internal",
  "roles":["deploy","monitoring"],
  "password_plain":"pass-Th!s-Shouldnt-be-here",
  "password_hash_sha256":"2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae",
  "last_changed":"2025-09-27T19:48:12Z",
  "security_questions":{"city":"denver","pet":"rye"},
  "otp_seed":"NB2W45DFOIZA====",
  "ssh_key":"ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC7A1kFj... bob@laptop",
  "note":"temporary staging override for blue/green test"
}
""",

r"""/var/log/auth.log
Oct 26 00:01:11 edge01 sshd[1382]: Accepted publickey for deploy from 10.0.21.53 port 52544 ssh2
Oct 26 00:04:07 edge01 sshd[1412]: Failed password for root from 203.0.113.19 port 40421 ssh2
Oct 26 00:04:08 edge01 sshd[1412]: Received disconnect from 203.0.113.19 port 40421:11: Bye
Oct 26 00:10:55 bastion sudo: pam_unix(sudo:session): session opened for user root by deploy(uid=1001)
Oct 26 00:11:02 bastion sudo: pam_unix(sudo:session): session closed for user root
""",

r"""/opt/service/credentials.txt
DB_HOST=pg-core.service.cluster
DB_PORT=6432
DB_USER=svc_reporting
DB_PASS=Rep0rt1ng!@2025
DB_SSLMODE=verify-full
REDIS_URI=rediss://cache-main.service.cluster:6380/0
JWT_SIGNING_KEY=-----BEGIN RSA PRIVATE KEY-----MIIBOgIBAAJBALy...
ADMIN_USER=svc-orchestrator
ADMIN_PASS=Orch_2025#Rotate
API_TOKEN=svc_api_prod_c9a5e54b3
SLACK_WEBHOOK=https://hooks.slack.com/services/T02/ops/abc123
ROTATION_DATE=2025-11-15
""",

r"""/home/charlie/credentials.csv
id,username,email,password_hash,last_seen,totp_active
1,charlie,charlie.ops@helios.internal,$2b$10$hashcharlie,2025-10-24T09:00:00Z,true
2,dana,dana.hr@helios.internal,$2b$10$hashdana,2025-10-24T10:00:00Z,false
3,eric,eric.analytics@helios.internal,$2b$10$hasheric,2025-10-24T11:00:00Z,true
session_token=session_charlie_1010
cookie=helios_session=COOKIE1234; Secure; HttpOnly
device_push=A1C9-88FF-22BB
""",

r"""/etc/hosts
127.0.0.1 localhost
::1 localhost
10.10.10.11 pg01.helios.internal pg
10.10.10.12 cache01.helios.internal cache
10.10.10.13 api01.helios.internal api
10.10.10.14 files.helios.internal minio
10.10.10.15 telemetry.helios.internal grafana
# sync via ansible 2025-10-15
""",

r"""/home/dev/.npmrc
//registry.npmjs.org/:_authToken=ghp_pat_uY28K0p1zXHX1FjXqCzOQ
//npm.pkg.github.com/:_authToken=gho_devkit_kX83n20
npm_config_cache=/home/dev/.npm_cache
fund=false
init.author.name=Helios Dev
GH_TOKEN=ghp_devtokenexample_f98d72
NPM_TOKEN=npm_pvt_c7aa6c632c
AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEKX//////////wEaCXVzLXdlc3QtMiJIMEYCIQC
""",

r"""/var/log/mysql/queries.log
# Time: 2025-10-25T23:58:02.128741Z
SELECT id,email,role FROM users WHERE deleted_at IS NULL LIMIT 25;
# Time: 2025-10-25T23:59:11.883920Z
UPDATE invoices SET status='void', void_reason='duplicate' WHERE id=7713;
# Time: 2025-10-26T00:00:45.112837Z
INSERT INTO audit_trail (actor,action,target,meta) VALUES ('svc-api','EXPORT','customers',JSON_OBJECT('rows',98));
# Time: 2025-10-26T00:02:11.003841Z
CALL refresh_materialized_view('mv_monthly_mrr');
""",

r"""/srv/ftp/manifest.txt
2025-10-01 backup-full.tar.zst (28.1G)
2025-10-08 backup-incr.tar.zst (6.4G)
2025-10-15 user-uploads-raw.zip (3.1G)
2025-10-24 credentials_snapshot.sql.gz (11.2M)
2025-10-24 api-logs.jsonl.gz (820M)
manifest.sig=4c1d57b02f27cc9a0b22bc7dd9deac8f
""",

r"""/home/ops/keys_and_secrets
rsa_signing: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7ops... ops@app
ed25519_deploy: ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB9H... deploy@bastion
age_key: age1l4j9ycp3z2tx8rv8y3ntf8l3y8djlk44g6gme6pyf5v9qj3cgvsejph0au
vault_token: hvs.RtqHXQ4yDPD1J8Qczdy35nN
totp_recovery: ["BR9P-2219","JW1Q-7004","NL5G-1182","TK1V-0321"]
ops_email: ops@supplysphere.io
ops_phone: +1-312-555-0202
""",

r"""/tmp/session_store.dump
session_1: {"user":"alice","ip":"10.0.5.42","city":"chi","device":"MacOS 14","last_seen":"2025-10-25T23:55:10Z","scope":["dashboard","billing"]}
session_2: {"user":"bob","ip":"10.0.5.43","city":"chi","device":"Firefox 131","last_seen":"2025-10-25T23:56:01Z","scope":["api","settings"]}
session_3: {"user":"charlie","ip":"10.0.5.44","city":"nyc","device":"iOS 18","last_seen":"2025-10-25T23:58:44Z","scope":["dashboard"]}
metadata: {"store":"redis","version":"7.2.4","eviction_policy":"allkeys-lru","uptime":"18d"}
""",

r"""/etc/nginx/sites-available/portal.conf
server {
    listen 80;
    listen 443 ssl http2;
    server_name portal.supplysphere.io;
    root /var/www/portal/current/public;
    access_log /var/log/nginx/portal.access.log main buffer=32k;
    error_log /var/log/nginx/portal.error.log warn;

    ssl_certificate /etc/ssl/certs/portal_2025.crt;
    ssl_certificate_key /etc/ssl/private/portal_2025.key;
    ssl_stapling on;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
}
location /api/ {
    proxy_pass http://api.internal.cluster;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Request-ID $request_id;
}
""",

r"""/home/marketing/contacts.csv
id,name,email,phone,company,notes
1,Greg,greg.marketing@clients.io,+1-312-555-0301,ExampleCorp,Q4 launch assets shared
2,Sarah,sarah@partners.net,+1-312-555-0302,OtherCorp,Needs updated case study
3,Tom,tom@clientx.io,+1-312-555-0303,ClientX,Pilot renewal 2025-12-01
4,Mike,mike@vendor.example,+1-312-555-0304,VendorY,Pending NDA countersign
5,Julia,julia@brightlane.co,+1-415-555-1189,BrightLane,Schedule onsite workshop
""",

r"""/var/www/secret_notes.md
# Internal Notes
- auth certs renewed 2025-09-15 (next due 2026-09-14)
- db admin role: admin_user (vault path secrets/prod/db/admin)
- smtp auth: smtp_user:SmTP_25! rotate by Nov sprint
- webhook signing secrets stored in parameter store /app/prod/webhooks
- TODO: remove legacy soap endpoint before 2025-11-30
token_stripe=sk_live_temp_99191
token_twilio=twilio_auth_1b2c3d
""",

r"""/home/backup/manifest_full.yml
manifest_version: 4
snapshot_id: snap-2025-10-25-0300
files:
  - path: backup-2025-10-01.tar.gz
    size: 30218732041
  - path: db-dump-2025-10-24.sql.gz
    size: 89233122
  - path: attachments-2025-09-20.zip
    size: 761283441
  - path: kube-config-2025-10-20.tar.gz
    size: 1120388
checksums:
  backup-2025-10-01.tar.gz: 91d8s2jd938dj28jd82
  db-dump-2025-10-24.sql.gz: b3f9c8d2a1e4f7
  attachments-2025-09-20.zip: 4d00f6443d7217
archived_by: ops
archive_date: 2025-10-25T03:00:00Z
retention_policy: 45d
storage_tier: glacier-deep
""",

r"""/etc/shadow
root:$6$k82jd9jH$2b8c...hash...:19870:0:99999:7:::
daemon:*:19870:0:99999:7:::
svcuser:$6$W92jd82J$9a7b...hash...:19870:0:99999:7:::
deploy:$y$j9T$VVDmx8yVHXE1vMYm$Y8eE2v7fCkE4DL3uK/d7qM7V6n6V5:19870:0:99999:7:::
""",

r"""/home/admin/mail/inbox.mbox
From: security@supplysphere.io
Subject: Action Required - Expiring TLS Certificates
Date: Sun, 26 Oct 2025 00:12:44 +0000

Certificates for portal.supplysphere.io will expire in 13 days.
Please request new certs via acme-prod and update CDN + origin.
Ticket: SEC-4172
--end--
""",

r"""/root/audit_report.log
[2025-10-25 23:50] scope: 10.0.0.0/22, profile: prod-weekly
[2025-10-25 23:51] discovery -> 42 alive hosts, avg latency 2.3ms
[2025-10-25 23:53] vuln match: CVE-2025-10411 on api01.helios.internal (OpenSSH 9.5)
[2025-10-25 23:54] config drift: nginx portal missing HSTS preload
[2025-10-25 23:55] artifact exported: /var/tmp/report_20251025.json (sha256 87a4f0a8...)
[2025-10-25 23:56] handoff -> uploaded to s3://helios-audit-logs/prod/report_20251025.json
"""
]
