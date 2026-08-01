# Release Checklist

Use this checklist before publishing every release.

---

## Version

- [ ] Update version in `pyproject.toml`
- [ ] Update `mini_scanner/__init__.py`
- [ ] Verify `--version` output

---

## Documentation

- [ ] README updated
- [ ] CHANGELOG updated
- [ ] Documentation updated
- [ ] Examples verified
- [ ] API documentation current

---

## Testing

Run:

```bash
pytest -v
pytest --cov=mini_scanner
```

Verify:

- [ ] All tests pass
- [ ] Coverage acceptable
- [ ] No skipped tests without justification

---

## Code Quality

Run:

```bash
black --check .
isort --check-only .
ruff check .
mypy mini_scanner
```

Verify:

- [ ] Formatting passes
- [ ] Linting passes
- [ ] Type checking passes

---

## Security

Run:

```bash
pip-audit
```

Verify:

- [ ] No known vulnerabilities
- [ ] No secrets committed

---

## Docker

Build:

```bash
docker build -t mini-scanner .
```

Verify:

- [ ] Image builds successfully
- [ ] CLI functions correctly

---

## Documentation Build

```bash
mkdocs build --strict
```

Verify:

- [ ] No broken links
- [ ] Navigation complete

---

## Package Build

```bash
python -m build
twine check dist/*
```

Verify:

- [ ] Wheel builds
- [ ] Source distribution builds
- [ ] Metadata valid

---

## GitHub

- [ ] CI passing
- [ ] CodeQL passing
- [ ] Dependabot clean
- [ ] Dependency Review passing

---

## Release

Create a tag:

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

Publish a GitHub Release with:

- Summary of changes
- Installation instructions
- Upgrade notes
- Known issues (if any)

---

## Final Sign-off

- [ ] Repository audit completed
- [ ] Release approved
- [ ] Version published