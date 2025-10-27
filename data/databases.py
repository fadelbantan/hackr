DATABASES = [

r"""/home/mark/secrets.db
{"user":"mark","email":"mark@socialcore.net","password_hash":"$2b$12$Jm9Q8rTz0n9Kqv2y3c4d5uE6w7x8y9z0a1b2c3d4e5f6g7h8i9j0"}
{"api_key":"AKI29N8FJ3K2L9H1M2N3","service":"payments","expires":"2027-01-01T00:00:00Z"}
{"session_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.SIG","last_ip":"10.4.12.42"}
{"device":"iPhone12","last_login":"2025-10-24T21:12:34Z"}
{"oauth_refresh":"refresh_98d72k3j9d823k"}
{"password_hint":"firstpet-coco"}
{"2fa_backup_codes":["bc-8673","bc-2736","bc-9348"]}
{"otp_seed":"JBSWY3DPEHPK3PXP"}
{"cookies":"SID=SESSION-12; Path=/; HttpOnly"}
{"prefs":{"theme":"dark","lang":"en-US"}}
{"billing_id":"2873"}
{"ssh_pub":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCl... mark@host"}
{"last_password_change":"2025-06-18"}
{"mfa_enabled":true}
{"backup_email":"mark.backup@socialcore.net"}
""",

r"""/var/www/app/.env
APP_ENV=production
APP_DEBUG=false
DATABASE_URL=postgres://app_user:K3D82msk9@pg.prod.corp.local:5432/app_prod
REDIS_URL=redis://:RedisPass!@cache.internal:6379/0
SECRET_KEY=sk_live_3hd8sjD92kd92jD83kd
STRIPE_SECRET=sk_live_83Hnd923JSn
MAILER_USER=mailer@corp.local
MAILER_PASS=Mail3rP@ss
SENTRY_DSN=https://sentry.internal/1234
JWT_SECRET=jwt_secr3t_92kd
AWS_ACCESS_KEY_ID=AKIA9X2J38DH7KS2JDK
AWS_SECRET_ACCESS_KEY=Zkd9Jd82kdm28d9sjD9d8Jdk9djD92kDJD93
DEPLOY_TAG=v2025.10.25
LOG_LEVEL=info
ADMIN_EMAIL=ops@corp.local
""",

r"""/var/backups/db_dump_2025_10_24.sql
-- PG dump of app_prod
CREATE TABLE users (id serial PRIMARY KEY, username text, email text, password_hash text);
INSERT INTO users (username,email,password_hash) VALUES
('alice','alice@corp.local','$2y$10$Jx8kX27AjkP12'),
('bob','bob@corp.local','$2y$10$Zy82kd8Hf9dP'),
('charlie','charlie@corp.local','$2y$10$S8d91js7H7sU');
-- sessions
INSERT INTO sessions (user_id,token,created_at) VALUES (1,'sess_28173','2025-10-25 11:00:00');
-- end dump
""",

r"""/home/bob/.credentials.json
{
  "username":"bob",
  "email":"bob@dev.corp.local",
  "password_plain":"hunter2_local",
  "password_hash_sha1":"da39a3ee5e6b4b0d3255bfef95601890afd80709",
  "last_changed":"2025-09-01T10:00:00Z",
  "notes":"staging account - rotate after use",
  "2fa_enabled":false,
  "ssh_key":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCy..."
}
""",

r"""/var/log/auth.log
Oct 25 11:55:03 node01 sshd[2131]: Accepted password for alice from 10.0.5.42 port 51324 ssh2
Oct 25 12:01:42 node01 sshd[2201]: Failed password for root from 10.0.12.77 port 61322 ssh2
Oct 25 12:05:11 node01 sshd[2233]: Accepted publickey for admin from 10.0.8.99 port 52311 ssh2
Oct 25 12:10:00 node01 sudo: pam_unix(sudo:session): session opened for user root by deployer(uid=0)
""",

r"""/opt/service/credentials.txt
DB_HOST=pg.prod.corp.local
DB_PORT=5432
DB_USER=svc_user
DB_PASS=SvcP@ssw0rd!2025
REDIS_PASS=redis_9876
JWT_SECRET=secret_jwt_09876
ADMIN_USER=svc-admin
ADMIN_PASS=Admin!Pass2025
API_TOKEN=token_service_77b8f9
EMAIL=ops@corp.local
ROTATION_DATE=2025-01-01
""",

r"""/home/charlie/credentials.csv
id,username,email,password_hash,last_seen
1,charlie,charlie@corp.local,$2b$10$hashcharlie,2025-10-24T09:00:00Z
2,dana,dana@corp.local,$2b$10$hashdana,2025-10-24T10:00:00Z
3,eric,eric@corp.local,$2b$10$hasheric,2025-10-24T11:00:00Z
session_token=session_charlie_1010
cookie=SESSIONID=COOKIE1234
""",

r"""/etc/hosts
127.0.0.1 localhost
10.0.5.10 pg.prod.corp.local
10.0.5.11 cache.internal
10.0.5.12 api.prod.corp.local
# internal mapping
""",

r"""/home/dev/.npmrc
//registry.npmjs.org/:_authToken=ghp_vrX83jD93kd8K2lF9sN3j8Jx7xP
npm_config_cache=/home/dev/.npm_cache
NODE_ENV=production
GH_TOKEN=ghp_devtokenexample_3f4a
aws_access_key_id=AKIADEVKEYYYY
aws_secret_access_key=SECRETDEVAAA
""",

r"""/var/log/mysql/queries.log
# Query time: 2025-10-25T10:00:00
SELECT * FROM users WHERE email='alice@corp.local' LIMIT 1;
# Query time: 2025-10-25T10:05:00
UPDATE accounts SET balance=balance-100 WHERE id=42;
# Query time: 2025-10-25T10:15:00
INSERT INTO payments (user_id,amount) VALUES (2,4999);
""",

r"""/srv/ftp/manifest.txt
backup-2025-10-01.tar.gz
user_uploads_2025-09-20.zip
private_docs_v2.pdf
credentials_snapshot_2025_10_24.sql
archive_index.json
manifest.sig=91d8s2jd938dj28jd82
""",

r"""/home/ops/keys_and_secrets
rsa_key_1: AAAAB3NzaC1yc2EAAAADAQABAAABAQDc1r...KEY1
rsa_key_2: AAAAB3NzaC1yc2EAAAADAQABAAABAQDm2s...KEY2
gpg_key: mQENBF5...EXAMPLEPUBKEY
vault_token: vault-token-7a9b3c
ops_email: ops@corp.local
ops_phone: +1-312-555-0202
""",

r"""/tmp/session_store.dump
session_1: {"user":"alice","last_seen":"2025-10-25T11:00:00Z","ip":"10.0.5.42"}
session_2: {"user":"bob","last_seen":"2025-10-25T11:05:00Z","ip":"10.0.5.43"}
session_3: {"user":"charlie","last_seen":"2025-10-25T11:10:00Z","ip":"10.0.5.44"}
metadata: {"store":"redis","version":"6.2.8"}
""",

r"""/etc/nginx/sites-available/portal.conf
server {
    listen 80;
    server_name portal.corp.local;
    root /var/www/portal;
    access_log /var/log/nginx/portal.access.log;
    error_log /var/log/nginx/portal.error.log;
}
location /api { proxy_pass http://api.prod.corp.local; }
ssl_certificate /etc/ssl/certs/portal.crt
ssl_certificate_key /etc/ssl/private/portal.key
""",

r"""/home/marketing/contacts.csv
id,name,email,phone,company
1,Greg,greg.marketing@clients.io,+1-312-555-0301,ExampleCorp
2,Sarah,sarah@partners.net,+1-312-555-0302,OtherCorp
3,Tom,tom@clientx.io,+1-312-555-0303,ClientX
4,Mike,mike@vendor.example,+1-312-555-0304,VendorY
""",

r"""/var/www/secret_notes.md
# Internal Notes
- credentials rotated on 2025-06-01
- db admin: admin_user (access via vault)
- smtp auth: smtp_user:smtp_pass_2k25
- TODO: rotate stripe key before deploy
token1=tok_temp_11111
token2=tok_temp_22222
""",

r"""/home/backup/manifest_full.yml
manifest_version: 3
files:
  - backup-2025-10-01.tar.gz
  - db-dump-2025-10-24.sql
  - attachments-2025-09-20.zip
checksums:
  backup-2025-10-01.sha256: 91d8s2jd938dj28jd82
  db-dump-2025-10-24.sha256: b3f9c8d2a1e4f7
archived_by: ops
archive_date: 2025-10-25
retention_policy: 30d
""",

r"""/etc/shadow
root:$6$k82jd9jH$2b8c...hash...:18139:0:99999:7:::
daemon:*:18139:0:99999:7:::
svcuser:$6$W92jd82J$9a7b...hash...:18139:0:99999:7:::
""",

r"""/home/admin/mail/inbox.mbox
From: security@corp.local
Subject: Password Rotation Required
Date: Sat, 25 Oct 2025 09:00:00 +0000
Body:
Your password will expire in 5 days. Please rotate credentials using vault-cli.
--end--
""",

r"""/root/audit_report.log
[2025-10-25 10:00] Scan started on 10.0.5.0/24
[2025-10-25 10:01] Open ports detected: 22,80,443,8080
[2025-10-25 10:02] Vulnerability matched: CVE-2024-12345
[2025-10-25 10:03] Exploit module triggered successfully
[2025-10-25 10:04] Dump complete: /var/tmp/dump_20251025.sql
[2025-10-25 10:05] exported: /var/tmp/dump_20251025.sql (48.3 MB) sha256:91d8s2jd938dj28
"""
]
