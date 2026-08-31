## Nick Coleman

**IT DevOps · MSc Information Security — Royal Holloway, University of London**

I do automation and infra work for a living and keep a two-node Proxmox cluster at home so I
can make the same mistakes on my own time. Most of what I write is Python, most of
what I deploy is declared in a repo somewhere, and nothing gets `apply`'d by hand if
a pipeline can do it instead.

A fair amount of my work lives on a self-hosted **Forgejo** instance rather than here —
the homelab repos especially. Some things also live on [Codeberg](https://codeberg.org/ncoleman).

---

### What I work with

| | |
|---|---|
| **Languages** | Python, Bash |
| **Infrastructure** | Proxmox VE, LXC, Docker, OpenTofu/Terraform, Ansible, nix-darwin + home-manager |
| **CI/CD** | Forgejo Actions, GitHub Actions, Kestra, Semaphore, pre-commit |
| **Platform** | Traefik, step-ca, Technitium DNS, MinIO, Authentik, PBS, Uptime Kuma |
| **Python** | FastAPI, Django, SQLAlchemy + Alembic, pytest, uv, ruff |
| **Security** | CVSS 4.0, OWASP, threat modelling, responsible disclosure, bandit / pip-audit / detect-secrets in CI |

---

### Side projects

**Some stuff I am working on**

| | |
|---|---|
| [**touchneedle**](https://github.com/nicoleman0/touchneedle) | Verifies that the citations in a document are real, accurately described, and consistently used — including the signature a fabricated AI bibliography leaves behind. Exits non-zero, so it drops into CI. `pip install touchneedle` |
| [**surgite**](https://github.com/nicoleman0/surgite) | Standup summaries from your git history — browser, terminal, or a shareable link. FastAPI + Postgres, no SPA framework, ~15 source files. `pip install surgite` |
| [**temenos**](https://github.com/nicoleman0/temenos) | Cross-platform CLI for domain research |
| [**kismob**](https://github.com/nicoleman0/kismob) | Mobile-first PWA for monitoring a Kismet wardriving rig |
| [**Road To War: July 1914**](https://codeberg.org/ncoleman/road-to-war) | Browser game about the thirty days between Sarajevo and general war. FastAPI, opposing chancelleries run by the same rules you are |
| [**run-run-run**](https://codeberg.org/ncoleman/run-run-run) | A local CI runner. GitLab-style `needs:` dependency graph, each job in its own Docker container, independent jobs concurrent |

---

### The homelab

`corvidae` — a two-node Proxmox cluster (Dell Optiplex 7070 Micro + GMKtec M5 Plus) with a
Raspberry Pi 5 as a corosync QDevice, so either node can drop and the survivor stays quorate.
Around fifteen LXCs plus a Debian Docker VM.

It's run as GitOps end to end:

- **OpenTofu** declares every guest (`hosts.yaml` / `vms.yaml`). A PR runs `tofu plan`, merging to `main` runs `tofu apply`, `main` is protected, and nobody applies by hand. State lives in **MinIO**, versioned and locked.
- **Ansible** configures the insides — fourteen roles covering Proxmox hosts, Traefik, Technitium, Jellyfin, SSH hardening, LXC provisioning, and guest updates.
- **Kestra** runs the scheduled side: cluster health, DHCP and DNS checks, disk and storage reporting, VPN health, host config backups, patching.
- **Forgejo Actions** on a self-hosted runner drives all of it. **Traefik** fronts the services, **step-ca** issues the internal certs, **PBS** takes the backups.
- The whole thing is documented in an MkDocs wiki that a Claude Code bot keeps current.

My Mac is declarative too — nix-darwin + home-manager + sops-nix, one `task switch` from clean to configured.

---

### Dissertation

**Delegated Defence: Prompt Injection and the Host-Model Assumption in Deployed MCP Servers.**

Depth-first security audits of deployed Model Context Protocol servers. Each server goes
through recon → static → dynamic → synthesis; every finding is grounded in an artifact
(`file:line`, a runnable PoC, or a captured request/response), scored with CVSS 4.0, and
classified against the OWASP MCP Top 10. Findings go out under responsible disclosure.

---

### Elsewhere

- **Blog** — [corvus-dev.com](https://corvus-dev.com) (Astro, hand-written CSS, zero client JS, deployed to Cloudflare Pages from Forgejo Actions)
- **Codeberg** — [@ncoleman](https://codeberg.org/ncoleman)
