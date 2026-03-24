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
Bashexport TENDR_VAULT=~/path/to/your/garden
```