# Changelog

This document provides an overview of the project's release history and explains the versioning policy used by **mini-scanner**.

For the authoritative release history, see the repository's root `CHANGELOG.md`.

---

# Versioning Policy

This project follows **Semantic Versioning (SemVer)**.

Version format:

```
MAJOR.MINOR.PATCH
```

Example:

```
1.2.3
```

Where:

| Component | Meaning |
|-----------|---------|
| MAJOR | Breaking API or behavior changes |
| MINOR | New features added in a backward-compatible manner |
| PATCH | Bug fixes, documentation updates, and small improvements |

---

# Release Types

## Major Release

Examples:

- Breaking CLI changes
- Public API redesign
- Removal of deprecated functionality

Example:

```
1.x → 2.0.0
```

---

## Minor Release

Examples:

- New scan options
- New output formats
- Performance improvements
- New configuration options

Example:

```
1.3.0 → 1.4.0
```

---

## Patch Release

Examples:

- Bug fixes
- Documentation improvements
- Test updates
- Dependency updates
- Security fixes without breaking compatibility

Example:

```
1.4.1 → 1.4.2
```

---

# Release Process

Each release should include:

1. All tests passing.
2. Documentation updates.
3. Changelog updates.
4. CI passing successfully.
5. Version number updated.
6. Git tag created.
7. GitHub Release published.

---

# Release Checklist

Before publishing a release:

- [ ] Update version number
- [ ] Update `CHANGELOG.md`
- [ ] Run full test suite
- [ ] Run formatting tools
- [ ] Run linting
- [ ] Run type checking
- [ ] Build documentation
- [ ] Verify Docker build
- [ ] Verify GitHub Actions
- [ ] Create Git tag
- [ ] Publish release

---

# Release History

## Version 1.x

Current stable release.

Highlights include:

- Multithreaded TCP port scanning
- Banner grabbing
- JSON and text output
- Python API
- Command-line interface
- Docker support
- GitHub Actions CI/CD
- Documentation with MkDocs

For detailed changes, see the root `CHANGELOG.md`.

---

# Deprecation Policy

Deprecated features should:

- Be documented before removal.
- Remain available for at least one stable release whenever practical.
- Include migration guidance where appropriate.

Breaking removals should occur only in a new major release.

---

# Security Releases

Security-related releases may be published outside the normal release schedule.

Users should upgrade promptly when security fixes are announced.

---

# Documentation Updates

Documentation improvements may accompany any release, including patch releases.

---

# Compatibility

The project aims to maintain compatibility within the same major version whenever possible.

Breaking changes will be clearly documented.

---

# Git Tags

Releases should be tagged using Semantic Versioning.

Examples:

```
v1.0.0
v1.1.0
v1.2.3
```

---

# Future Releases

Potential future improvements include:

- IPv6 support
- UDP scanning
- Plugin architecture
- Additional output formats
- Performance optimizations
- Enhanced service detection
- Improved automation support

---

# Contributing

If your Pull Request changes user-visible behavior, adds features, fixes significant bugs, or introduces breaking changes, please update the root `CHANGELOG.md` as part of your contribution.

---

# Additional Resources

- Installation Guide
- Quick Start
- CLI Reference
- Configuration
- Examples
- API Reference
- Development Guide
- Security Guide