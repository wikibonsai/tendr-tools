# 🪴 tendr-tools 🎍

[![A WikiBonsai Project](https://img.shields.io/badge/%F0%9F%8E%8B-A%20WikiBonsai%20Project-brightgreen)](https://github.com/wikibonsai/wikibonsai)

This repository provides lightweight, deterministic tool adapters so agents built with popular frameworks can call `tendr-cli` without ever touching raw files directly.

Everything stays 100% plaintext, git-safe, and cultivatable.

🤖 🚰 ✂️ Tend your [🎋 WikiBonsai](https://github.com/wikibonsai/wikibonsai) digital garden with integrated tooling.

## Why tendr-tools?

Most agent frameworks give agents raw filesystem or shell access.  
That quickly leads to corrupted hierarchies, broken [[links]], and messy attributes.

`tendr-tools` gives agents a single safe entrypoint: Discrete, predictable `tendr` commands wrapped as native Tools (or Skills) for each framework.

## Installation

```bash
git clone https://github.com/wikibonsai/tendr-tools.git
cd tendr-tools
```

Set your vault location (defaults to ~/.tendr/garden):

```bash
export TENDR_VAULT=~/path/to/your/garden
```


## Available Integrations

| Framework              | Folder       | File                | Type   |
|------------------------|--------------|---------------------|--------|
| LangGraph / LangChain  | `langgraph/` | `tendr_tool.py`    | Tool   |
| CrewAI                 | `crewai/`    | `tendr_tool.py`    | Tool   |
| Letta                  | `letta/`     | `tendr_tool.py`    | Tool   |
| OpenClaw               | `openclaw/`  | `tendr_skill.md`   | Skill  |

## Quick Start

See the README inside each framework folder for usage examples and code snippets.

All tools respect:

- `TENDR_VAULT` environment variable
- `tendr-cli` safety rules and auth mode (`user` vs `agent`)
- Your existing semtree, typed links, and CAML structure

## Philosophy

A knowledge base that merely **accumulates** is a liability.  
One that gets actively **tended** becomes an asset that appreciates over time.
[Read more [here](https://wibomd.substack.com/p/cultivation-accumulation)]

These integrations make it easy for agents to _cultivate_ instead of just retrieve.

## Related Projects

- [garden-beds](https://github.com/wikibonsai/garden-beds) — Starter vaults
- [tendr-cli](https://github.com/wikibonsai/tendr-cli) — Core deterministic commands
- [tendr-skill](https://github.com/wikibonsai/tendr-skill) — Agent behavior & prompts
- [wikibonsai](https://github.com/wikibonsai/wikibonsai) — The legible knowledge layer

---

**Status**: Early / Beta — always keep backups and use version control.

Happy tending 🌱
