DATABASES = [

r"""/home/mark/secrets.db
{"user":"mark","email":"markus@facemash.co","password":"$2b$12$faKeBcryptHashExamplei3uyeiuyr392764gb9"}
{"api_key":"AKI2897324098","service":"payments","expires":"2027-01-01T00:00:00Z"}
{"session_token":"eyJhbGciOiJfRkFLSUVOIiwi...jwt.token.segment...","last_ip":"203.0.113.42"}
{"device":"iPhone12","last_login":"2025-10-24T21:12:34Z"}
{"oauth_refresh":"refresh_9876543210"}
{"password_hint":"firstpet-middlename (coco)"}
{"2fa_backup_codes":["bc-8673","bc-2736","bc-9348"]}
{"otp_seed":"JBSWY3DPEHPK3PXP"}
{"cookies":"SID=SESSION-12; Path=/; HttpOnly"}
{"prefs":{"theme":"dark","lang":"en-US"}}
{"billing_id":"2873"}
{"ssh_pub":"ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArb... mark@localhost"}
{"last_password_change":"2025-06-18"}
{"mfa_enabled":true}
{"backup_email":"markyzukzuk@facemash.co"}
{"comment":"if you find this: im not human"}
""",

r"""/var/www/html/.env
APP_ENV=production
APP_DEBUG=false
DATABASE_URL=postgres://app_user:Password42@db.internal:5432/app_prod
REDIS_URL=redis://:cachepass@redis.internal:6379/0
SECRET_KEY=supersecret_key_please_change
STRIPE_SECRET=sk_live_83Hnd923JSn
MAILGUN_APIKEY=key-mailgun-28973492873
SENTRY_DSN=https://logs@sentry.invalid/123
JWT_SECRET=jwt_secret_key_9287
OAUTH_CLIENT_ID=client_902183
OAUTH_CLIENT_SECRET=secret_982173
AWS_ACCESS_KEY_ID=AKIA1234ACCESS
AWS_SECRET_ACCESS_KEY=w9i2nd9834Hdj82Js92kd
DEPLOY_TAG=v2025.10.25
LOG_LEVEL=info
ADMIN_EMAIL=ops@example.invalid
""",

r"""/database/dump_users.sql
-- users table dump
INSERT INTO users (id,username,email,password_hash) VALUES
(1,'alice','alice@example.invalid','$2y$10$Jx8kX27AjkP12'),
(2,'bob','bob@example.invalid','$2y$10$Zy82kd8Hf9dP'),
(3,'charlie','charlie@example.invalid','$2y$10$S8d91js7H7sU');
INSERT INTO sessions (id,user_id,token,created_at)
VALUES (1,1,'sess_28173','2025-10-25 11:00:00');
INSERT INTO api_keys (id,user_id,key,service)
VALUES (1,2,'api_k283Hs88','maps');
-- end of dump
""",

r"""/home/bob/credentials.json
{
  "username": "bob",
  "email": "bob@example.invalid",
  "password_plain": "hunter2",
  "password_hash_sha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
  "last_changed": "2025-09-01T10:00:00Z",
  "notes": "temporary dev account; rotate asap",
  "2fa": {"enabled": false},
  "ssh_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADA bob@host"
}
""",

r"""/var/log/auth.log
Oct 25 11:55:03 server sshd[2131]: Accepted password for alice from 198.51.100.10 port 51324 ssh2
Oct 25 12:05:11 server sshd[2233]: Accepted publickey for admin from 203.0.113.99 port 52311 ssh2
Oct 25 12:10:00 server sshd[2288]: pam_unix(su:session): session opened for user root by deployer(uid=0)
Oct 25 12:14:20 server sshd[2302]: Accepted password for ops from 192.0.2.66 port 62000 ssh2
""",

r"""/opt/service/credentials.txt
DB_HOST=db.internal
DB_PORT=5432
DB_USER=svc_user
DB_PASS=SvcP@ssw0rd!
REDIS_PASS=redis_9876
JWT_SECRET=secret_jwt_09876
ADMIN_USER=svc-admin
ADMIN_PASS=Admin!Pass2025
API_TOKEN=token_service_777
EMAIL=ops@example.invalid
""",

r"""/home/charlie/credentials.csv
id,username,email,password_hash,last_seen
1,charlie,charlie@example.invalid,$2b$10$hashcharlie,2025-10-24T09:00:00Z
2,dana,dana@example.invalid,$2b$10$hashdana,2025-10-24T10:00:00Z
3,eric,eric@example.invalid,$2b$10$hasheric,2025-10-24T11:00:00Z
session_token=session_charlie_1010
cookie=SESSIONID=COOKIE1234
""",

r"""/etc/hosts_and_config
127.0.0.1 localhost
10.0.0.5 db.internal
10.0.0.6 redis.internal
admin_user=admin
admin_pass=Adm1n!Pass
timezone=UTC
dns_search=internal
proxy=proxy.internal:3128
""",

r"""/home/dev/.npmrc_and_tokens
//registry.npmjs.org/:_authToken=NPM_TOKEN_abc123
npm_config_cache=/home/dev/.npm_cache
PRIVATE_KEY=-----BEGIN RSA PRIVATE KEY-----KEYDATA-----END RSA PRIVATE KEY-----
NODE_ENV=production
GH_TOKEN=ghp_devtokenexample
aws_access_key_id=AKIADEVKEYYYY
aws_secret_access_key=SECRETDEVAAA
""",

r"""/var/log/mysql/slow.log
# Query time: 2025-10-25T10:00:00
SELECT * FROM users WHERE email='alice@example.invalid' LIMIT 1;
# Query time: 2025-10-25T10:05:00
UPDATE accounts SET balance=balance-100 WHERE id=42;
""",

r"""/srv/ftp/files_manifest.txt
backup-2025-10-01.tar.gz
user_uploads_2025-09-20.zip
private_docs_v2.pdf
credentials_snapshot_2025_10_24.sql
""",

r"""/home/ops/keys_and_secrets
rsa_key_1: AAAAB3NzaC1yc2EAAAADAQABAAABAQKey1
rsa_key_2: AAAAB3NzaC1yc2EAAAADAQABAAABAQKey2
vault_token: vault-token-98765
ops_email: ops-team@example.invalid
ops_phone: +1-555-0202
""",

r"""/tmp/session_store.dump
session_1: {"user":"alice","last_seen":"2025-10-25T11:00:00Z","ip":"198.51.100.10"}
session_2: {"user":"bob","last_seen":"2025-10-25T11:05:00Z","ip":"198.51.100.11"}
session_3: {"user":"charlie","last_seen":"2025-10-25T11:10:00Z","ip":"192.0.2.55"}
""",

r"""/etc/nginx/sites-available/example.conf
server {
    listen 80;
    server_name example.invalid;
    root /var/www/html;
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
}
ssl_certificate /etc/ssl/certs/example.crt
ssl_certificate_key /etc/ssl/private/example.key
""",

r"""/home/marketing/contacts.csv
id,name,email,phone,company
1,Greg,greg.marketing@example.invalid,+1-555-0301,ExampleCorp
2,Sarah,sarah@example.invalid,+1-555-0302,OtherCorp
3,Tom,tom@example.invalid,+1-555-0303,ClientX
""",

r"""/var/www/secret_notes.md
# Internal Notes
- credentials rotated on 2025-06-01
- db admin: admin_user (use vault)
- smtp auth: smtp_user:smtp_pwd
token1=tok_temp_11111
token2=tok_temp_22222
""",

r"""/home/backup/manifest_full
manifest_version: 3
files:
 - backup-2025-10-01.tar.gz
 - db-dump-2025-10-24.sql
 - attachments-2025-09-20.zip
checksums:
 - backup-2025-10-01.sha256: SHA256CHECKSUM111
 - db-dump-2025-10-24.sha256: SHA256CHECKSUM222
archived_by: ops
""",

r"""/etc/shadow_partial
root:$6$k82jd9jH:18139:0:99999:7:::
daemon:*:18139:0:99999:7:::
user:$6$W92jd82J:18139:0:99999:7:::
""",

r"""/home/admin/mailbox/inbox.mbox
From: security@example.invalid
Subject: Password Rotation Required
Body:
Your password will expire in 5 days. Please rotate credentials using vault-cli.
--end--
""",

r"""/root/audit_report.log
[2025-10-25 10:00] Scan started on 192.0.2.0/24
[2025-10-25 10:01] Open ports detected: 22,80,443,8080
[2025-10-25 10:02] Vulnerability matched: CVE-2024-12345
[2025-10-25 10:03] Exploit module triggered successfully
[2025-10-25 10:04] Dump complete: /var/tmp/dump_20251025.sql
"""
]
