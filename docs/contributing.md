# Contributing to mini-scanner

Thanks for taking a look at this project. mini-scanner began as a
learning exercise — building a small TCP port scanner from scratch to
understand the ideas behind tools like `nmap` — and it's shared as open
source in that same spirit: something built while learning, offered back
to others who are learning too. Contributions from people at any
experience level are genuinely welcome, including your first-ever pull
request.

## Ways to contribute

You don't have to write code to contribute:

- **Report a bug** — open an issue with steps to reproduce, what you
  expected, and what actually happened
- **Suggest an improvement** — new scan options, better output formatting,
  docs clarifications, etc.
- **Improve documentation** — fix a typo, clarify a confusing paragraph,
  add an example
- **Write code** — fix a bug, add a feature, improve test coverage
- **Review pull requests** — feedback on open PRs is genuinely useful

## Getting set up

```bash
# fork the repo, then clone your fork
git clone https://github.com/<your-username>/mini-scanner.git
cd mini-scanner

# install in editable mode
pip install -e .

# (optional) install dev/test dependencies if present
pip install -r requirements-dev.txt   # skip if this file doesn't exist yet

# run the test suite before you start, to confirm a clean baseline
pytest
```

## Making a change

1. Create a branch from `main`:
   `git checkout -b fix/short-description` or `feature/short-description`
2. Make your change, keeping commits focused and readable.
3. Add or update tests for any behavior you change.
4. Run the test suite locally and make sure it passes.
5. Update relevant docs (`README.md`, docstrings, help text) if behavior
   or usage changed.
6. Open a pull request against `main` with:
   - A clear description of *what* changed and *why*
   - Any relevant issue number (`Fixes #12`)
   - Before/after output if the change affects CLI behavior

## Pull request expectations

- Keep PRs focused — one logical change per PR is easier to review than a
  bundle of unrelated fixes.
- It's fine to open a draft PR early and ask for feedback before it's
  finished — that's often the fastest way to learn the codebase.
- Be responsive to review comments, but don't feel discouraged by them —
  review is about the code, not a judgment of the contributor.

## A note on scope, since this is a scanner

Contributions that add scanning capability should stay focused on
legitimate network diagnostics and security-education use cases (the same
spirit as tools like `nmap`). Please don't submit changes intended to
evade detection, spoof traffic, or otherwise aid unauthorized access to
systems. See [SECURITY.md](SECURITY.md) for how we think about responsible
use of this tool more broadly.

## Questions

If anything here is unclear, or you're not sure whether an idea fits the
project, open an issue and ask before investing a lot of time — that's
what issues are for, and no question is too basic.
