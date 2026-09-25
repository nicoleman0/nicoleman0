## Nick Coleman

I build Python tools, experiment with LLM security, and run a two-node Proxmox homelab.
Most of what I deploy is declared in a repo and applied through a pipeline.

[Blog](https://corvus-dev.com) · [Codeberg](https://codeberg.org/ncoleman)

### Open-source contributions

<!-- metrics:start -->
![GitHub stats and notable contributions](github-metrics.svg)
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
