# Security

Security is a core goal of **mini-scanner**. This document describes the project's security practices, supported versions, responsible disclosure process, and recommendations for safely using the software.

---

# Supported Versions

The project maintains security updates for the latest stable release.

| Version | Supported |
|---------|:---------:|
| 1.x | ✅ Yes |
| < 1.0 | ❌ No |

Users are encouraged to upgrade to the latest release.

---

# Reporting a Vulnerability

If you believe you have discovered a security vulnerability in **mini-scanner**, **do not create a public GitHub Issue**.

Instead:

1. Review the project's `SECURITY.md`.
2. Contact the maintainer privately using the security contact listed in the repository.
3. Include sufficient information to reproduce and validate the issue.
4. Allow reasonable time for investigation and remediation before public disclosure.

Please include:

- mini-scanner version
- Operating system
- Python version
- Installation method
- Steps to reproduce
- Proof of concept (if available)
- Impact assessment
- Suggested mitigation (optional)

---

# Disclosure Process

When a vulnerability is reported:

1. The report is acknowledged.
2. The issue is reproduced and assessed.
3. A fix is developed and tested.
4. A patched release is prepared.
5. Users are advised to upgrade.
6. Public disclosure may follow once a fix is available.

---

# Secure Development Practices

The project aims to follow these practices:

- Code review before merging changes
- Automated CI testing
- Static analysis (Ruff, mypy)
- Dependency review
- CodeQL analysis
- Secret scanning
- Dependency auditing
- Reproducible builds where practical

---

# Dependency Management

Dependencies should:

- Come from trusted sources.
- Be kept up to date.
- Be reviewed before upgrades.
- Be monitored for known vulnerabilities.

Run a dependency audit:

```bash
pip-audit
```

---

# Secure Coding Guidelines

Contributors should:

- Validate all user input.
- Handle exceptions safely.
- Avoid exposing sensitive information in logs.
- Keep third-party dependencies to a minimum.
- Prefer standard library functionality where appropriate.
- Write tests for security-sensitive code paths.

---

# Safe Usage

Only scan systems that:

- You own, **or**
- You have explicit authorization to assess.

Unauthorized scanning may violate organizational policies or applicable laws.

---

# Network Safety

When scanning:

- Use reasonable timeout values.
- Avoid unnecessarily aggressive worker counts.
- Be aware that some intrusion detection systems may log or alert on port scans.
- Respect rate limits and operational constraints on target networks.

---

# Secrets

Never commit:

- API keys
- Passwords
- SSH private keys
- Access tokens
- Certificates
- `.env` files containing secrets

Use `.env.example` as a template and keep real secrets out of version control.

---

# Security Features

The project includes or supports:

- GitHub CodeQL
- Dependabot
- Dependency Review
- Secret Detection
- Pre-commit Hooks
- Automated Testing
- Continuous Integration

---

# Known Limitations

`mini-scanner` is a TCP port scanner. It does **not**:

- Exploit vulnerabilities.
- Bypass authentication.
- Evade firewalls or intrusion detection systems.
- Guarantee service identification from banners.
- Assess the security posture of detected services.

Banner information should be treated as informational and may be incomplete or intentionally misleading.

---

# Reporting False Positives

If you believe the scanner incorrectly reports a port state or banner:

- Record the command used.
- Capture relevant logs.
- Compare results with another trusted tool if appropriate.
- Open a GitHub Issue with reproduction details.

---

# Security Checklist for Contributors

Before submitting changes:

- [ ] Tests pass.
- [ ] New functionality includes tests.
- [ ] Dependencies reviewed.
- [ ] No secrets committed.
- [ ] Documentation updated.
- [ ] CI passes successfully.

---

# Contact

For responsible disclosure, follow the process described in the repository's root `SECURITY.md`. Please avoid discussing unpatched vulnerabilities in public Issues or Discussions.

---

# Acknowledgements

We appreciate responsible security research and coordinated disclosure that helps improve the safety and reliability of the project for everyone.