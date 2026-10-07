# coderabbit — the fleet's CodeRabbit defaults

This repository holds one file that matters: [`.coderabbit.yaml`](.coderabbit.yaml).
CodeRabbit reads it as the **central configuration** for the `lentago` organization:
every repository that does not carry its own `.coderabbit.yaml` inherits it
([how central configuration works](https://docs.coderabbit.ai/configuration/central-configuration)).

**What it sets, and why**

- CodeRabbit is a second reviewer, **never a gate**: it does not block merges and is
  not a required status check anywhere in the fleet. Required checks are the ones
  that can fail deterministically; a slow external review in that set would stall
  auto-merge.
- The high-level summary goes into the **walkthrough comment**, not the PR
  description. In this fleet the PR body becomes the squash commit message and
  stays the author's words.
- Generated trees are excluded (`brand/generated/`, `demo/generated/`, the harvested
  fleet reports, lockfiles). A hand-edit to any of those already fails CI in the
  owning repo.
- Path instructions carry the fleet's own rules so its comments agree with them:
  least privilege and self-protecting boundaries in Terraform; the
  required-check deadlock rule for workflows; the voice guide for reader-facing
  Markdown; standard-library-only code in uvularia's core; nothing
  Lentago-specific in client templates.
- The voice guide and the canonical PR-workflow text are read as code guidelines
  from their source repos, so there is one copy of each.

**Overriding for one repository**

Configuration sources do not merge. A repository that needs different settings
copies this file in as its own `.coderabbit.yaml` and edits it; that file then
wins outright.

**Checking what a PR actually resolved to**

Comment `@coderabbitai configuration` on any pull request. CodeRabbit replies with
the resolved YAML, annotated with the source of every value.

**Changing fleet-wide behaviour**

Open a pull request here. The file is validated against CodeRabbit's published
schema in CI before it can merge.

---

> 🌱 **Lentago Labs** is a pro-bono operations practice for organizations that
> run on volunteers, donations, and one overworked tech person. Everything here
> is free to take, and we practice what we publish: our own estate runs this
> way, in the open. Start at the [org profile](https://github.com/lentago).
