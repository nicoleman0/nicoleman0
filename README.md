## Nick Coleman

I build Python tools, experiment with LLM security, and run a two-node Proxmox homelab.
Most of what I deploy is declared in a repo and applied through a pipeline.

[Blog](https://corvus-dev.com) · [Codeberg](https://codeberg.org/ncoleman)

### Open-source contributions

<!-- contributions:start -->
**7 merged PRs across 5 community projects.**

All public merged PRs to repositories outside my account.

#### [stub42/pytz](https://github.com/stub42/pytz)

- [#149](https://github.com/stub42/pytz/pull/149) Raise UnknownTimeZoneError for non-string zone arguments
- [#148](https://github.com/stub42/pytz/pull/148) Make \_FixedOffset a BaseTzInfo exposing \_utcoffset

#### [commitizen-tools/commitizen](https://github.com/commitizen-tools/commitizen)

- [#1773](https://github.com/commitizen-tools/commitizen/pull/1773) fix(config): add warning for multiple configuration files and update documentation

#### [ashita-ai/arbiter](https://github.com/ashita-ai/arbiter)

- [#88](https://github.com/ashita-ai/arbiter/pull/88) Add input validation with helpful error messages
- [#85](https://github.com/ashita-ai/arbiter/pull/85) Feature/pretty print refactor

#### [totalbrain/TxT2PDF](https://github.com/totalbrain/TxT2PDF)

- [#5](https://github.com/totalbrain/TxT2PDF/pull/5) Enhanced performance and add benchmarking for PDF conversion.

#### [ShahzaibAhmad05/gitree](https://github.com/ShahzaibAhmad05/gitree)

- [#205](https://github.com/ShahzaibAhmad05/gitree/pull/205) docs: add interactive selection example to README
<!-- contributions:end -->

<!-- metrics:start -->

<!-- metrics:end -->

### Selected projects

| Project | What it does |
|---|---|
| [touchneedle](https://github.com/nicoleman0/touchneedle) | Checks whether document citations are real, accurately described and consistently used. Runs in CI. |
| [surgite](https://github.com/nicoleman0/surgite) | Standup summaries from git history, in the browser or terminal. |
| [elengtis](https://github.com/nicoleman0/elengtis) | A configurable MCP prompt-injection benchmark using YAML and LangGraph. |
| [rescribo](https://github.com/nicoleman0/rescribo) | A customer feedback inbox connecting Slack, GitHub and human follow-up. |

### The homelab

I run a two-node Proxmox cluster with a Raspberry Pi as its QDevice, managed with
OpenTofu, Ansible and Forgejo Actions. My Mac configuration lives in nix-darwin
and home-manager.

The homelab repositories and operational docs live on a private Forgejo instance.
I write about my projects at [corvus-dev.com](https://corvus-dev.com).

### Research

My MSc Information Security dissertation at Royal Holloway examines prompt injection
in deployed MCP servers and the assumption that a hardened model makes them safe.
The work combines source review and live testing, with findings grounded in
reproducible evidence and handled through responsible disclosure.
