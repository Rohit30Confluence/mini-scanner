# Repository Audit Checklist

Use this checklist before every release to ensure the repository remains healthy, consistent, and production-ready.

---

# Repository Structure

Verify that the following exist:

- [ ] README.md
- [ ] LICENSE
- [ ] CONTRIBUTING.md
- [ ] CODE_OF_CONDUCT.md
- [ ] CHANGELOG.md
- [ ] ROADMAP.md
- [ ] SUPPORT.md
- [ ] SECURITY.md
- [ ] CODEOWNERS
- [ ] FUNDING.yml
- [ ] pyproject.toml
- [ ] requirements-dev.txt
- [ ] Makefile
- [ ] Dockerfile
- [ ] docker-compose.yml
- [ ] .dockerignore
- [ ] .gitignore
- [ ] .editorconfig
- [ ] .pre-commit-config.yaml
- [ ] tox.ini
- [ ] mkdocs.yml

---

# GitHub Configuration

Verify:

- [ ] CI workflow passes
- [ ] CodeQL succeeds
- [ ] Dependency Review succeeds
- [ ] Release workflow succeeds
- [ ] Dependabot configuration valid
- [ ] Security policy exists
- [ ] Issue templates work
- [ ] Pull Request template works

---

# Python Packaging

Verify:

- [ ] Package installs successfully
- [ ] Editable install works
- [ ] Version is correct
- [ ] Metadata is complete
- [ ] License included
- [ ] README renders correctly

Commands:

```bash
python -m build
pip install dist/*.whl
```

---

# Testing

Run:

```bash
pytest -v
```

Coverage:

```bash
pytest --cov=mini_scanner
```

Verify:

- [ ] All tests pass
- [ ] Coverage acceptable
- [ ] No flaky tests

---

# Code Quality

Run:

```bash
black --check .
isort --check-only .
ruff check .
mypy mini_scanner
```

Verify:

- [ ] Formatting passes
- [ ] Imports sorted
- [ ] No lint errors
- [ ] Type checking passes

---

# Docker

Build:

```bash
docker build -t mini-scanner .
```

Verify:

- [ ] Image builds
- [ ] CLI works
- [ ] Tests run
- [ ] Image size acceptable

---

# Documentation

Verify:

- [ ] MkDocs builds
- [ ] No broken links
- [ ] Navigation complete
- [ ] Examples tested
- [ ] API documentation up to date

Build:

```bash
mkdocs build --strict
```

---

# Security

Run:

```bash
pip-audit
```

Verify:

- [ ] No known vulnerabilities
- [ ] No secrets committed
- [ ] Dependencies reviewed
- [ ] SECURITY.md current

---

# Release

Before publishing:

- [ ] Version updated
- [ ] CHANGELOG updated
- [ ] Documentation updated
- [ ] CI green
- [ ] Git tag created
- [ ] GitHub Release created

---

# Final Review

Verify:

- [ ] README badges work
- [ ] Installation instructions verified
- [ ] CLI examples tested
- [ ] Docker examples tested
- [ ] Python API examples tested
- [ ] Repository links valid
- [ ] License present

---

# Sign-off

Reviewer:

________________________

Date:

________________________

Version:

________________________

Result:

- [ ] PASS
- [ ] FAIL