# Security Policy

## Supported Versions & End of Life

| Version | Supported          | End of Life / Notes                                                          |
| ------- | ------------------ | ---------------------------------------------------------------------------- |
| 3.0.x   | :x:                | End of life. no security patches will be produced. Upgrade to 3.1.x or 3.2.x |
| 3.1.x   | :white_check_mark: | Security fixes will be backported for critical/high issues where feasible.   |
| 3.2.x   | :white_check_mark: | Current stable. Critical & high vulnerabilities will be patched in 3.3.x     |
| < 3.0   | :x:                | Unsupported.                                                                 |

**Upgrade recommendation:** Users should run the latest patch release in order to avoid issues (e.g. 3.2.(latest)). If you cannot upgrade, contact us in your report and include your impact statement so we can advise a course of action.

---

## Reporting a Vulnerability
If you discover a security vulnerability, please follow these steps:
1. **Do not open a public issue or public PR**: for a vulnerability. Public disclosure may put users at risk. - Instead, report the issue directly to us via our preferred reporting channels:

  Preferred reporting channels (in order):
  - **Email (encrypted preferred):** L00182374@atu.ie  
     - If you can encrypt with our PGP key, please do. See the PGP key block below.
     
  - **GitHub Security Advisories (private):** Use the repository's _Security_ -> _Advisories_ -> _New private report_ if available.
  
  - If both fail, send an email to L00182374@atu.ie unencrypted and mark it PRIVATE.

**PGP key**  
Use this PGP key to encrypt sensitive report details: 4CC1 D2FF 9237 29AF 22FC 6C29 6C64 F226 CA79 5B97

2. **Provide detailed information**: Include as much detail as possible to help us reproduce and resolve the issue, such as:
- Affected version(s)
- Steps to reproduce the vulnerability
- Any relevant code snippets or logs

3. **Expected Response Time**: We aim to respond to all security reports within **2 business days** and provide a resolution or mitigation plan within **5 business days**.

## Disclosure Policy
We follow a responsible disclosure process:

1. We will work with you to validate and resolve the vulnerability.

2. Once the issue is resolved, we will publicly disclose the details of the vulnerability.

---

# Security Best Practices

We enable GitHub Dependabot and secret scanning

We recommend all contributors and users to follow these best practices:
Use the latest version of the project.
- Regularly update dependencies.
- Report suspicious activities or vulnerabilities promptly.
