# Security Policy

## About this project

mini-scanner is an open-source TCP port scanner built as a learning
project — a small-scale exploration of the ideas behind tools like `nmap`.
Because it's a network scanning tool, security matters here in two
distinct senses: the security of the codebase itself, and the responsible
use of what it does. Both are covered below.

## Supported versions

This is an actively developed learning project without a long-term
support matrix yet. Security fixes are applied to the latest version on
`main`. If you're running an older tagged release, please upgrade to the
latest before reporting an issue, if possible.

| Version | Supported |
| ------- | --------- |
| latest (`main`) | ✅ |
| older tags | ⚠️ best-effort |

## Reporting a vulnerability

If you find a security issue in mini-scanner itself (for example: a bug
that could let scan input trigger unintended code execution, a dependency
with a known CVE, or a flaw in the web UI's input handling), please report
it privately rather than opening a public issue:

- Preferred: use GitHub's [private vulnerability reporting](https://github.com/Rohit30Confluence/mini-scanner/security/advisories/new)
  for this repository (Security tab → "Report a vulnerability").
- Alternative: contact the maintainer directly via the contact info on
  their GitHub profile.

Please include:
- A description of the issue and its potential impact
- Steps to reproduce, or a minimal proof of concept
- Any suggested fix, if you have one (not required)

You should get an acknowledgment within a few days. Please allow a
reasonable window to investigate and release a fix before any public
disclosure.

## Responsible use of this tool

mini-scanner performs real TCP connection attempts against hosts and
ports it's pointed at. Scanning a system you do not own or do not have
explicit authorization to test may violate laws such as the U.S. Computer
Fraud and Abuse Act, the UK Computer Misuse Act, or equivalent laws in
other jurisdictions, as well as the terms of service of many networks and
cloud providers.

- Only scan hosts you own or have explicit written permission to test.
- If you're learning, use a target designed for this purpose, such as
  [scanme.nmap.org](https://nmap.org/book/testing.html) (subject to its
  own usage policy) or a local VM/lab environment you control.
- Contributions that add capability intended to evade detection, spoof
  identity, or otherwise facilitate unauthorized access will not be
  accepted — see [CONTRIBUTING.md](CONTRIBUTING.md).

This policy exists to keep the project usable for learning and legitimate
security work without becoming a liability for its users.
