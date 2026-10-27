# Lusona Skills privacy policy

Last updated: October 27, 2026

This policy describes data handling by Lusona Skills, the open-source workflow
plugin maintained by Lusona LLC. It covers the plugin and information you choose
to share with its maintainers for support. Your coding-agent provider, GitHub,
and any other services you use have their own privacy policies.

## Plugin operation

Lusona supplies workflow instructions, templates, reference documents, and local
Bash and PowerShell helpers. It does not operate a backend service or include
analytics, advertising, tracking cookies, or telemetry. The bundled helpers do not
make network requests. Installing or using the plugin does not, by itself, send
your prompts, source code, project records, or credentials to Lusona LLC.

When you use a skill, your host agent processes the task and any project context
it accesses under your permissions. That context may include source code, file
paths, requirements, decisions, and test results. Depending on your host and its
settings, this information may be processed by your agent provider or connected
services. Lusona's instructions do not replace those providers' privacy policies
or your host's access controls.

Within the work you authorize, skills can create or update project records under
`docs/lusona/`. The bundled helpers create and maintain those records locally.
They do not upload them. If you authorize an agent to use external tools, publish
changes, or send information, those actions may share data with the destinations
you choose. Plugin maintainers do not receive access to your workspace merely
because you install the plugin.

## Storage and retention

You control local project files and can inspect, edit, or delete them. Uninstalling
the plugin leaves project records in place. Copies may also remain in your version
control, backups, synchronized storage, or agent-provider history according to the
settings and retention policies of those systems. Lusona LLC does not keep a
separate copy of your local plugin activity.

## Support information

If you open a GitHub issue or pull request, maintainers can see the information
you submit, including your GitHub account name, message, attachments, and any logs
or project excerpts you include. We use this information to respond to requests,
investigate problems, and maintain the software. We do not sell support information
or use it for advertising.

This repository and its issues are public. Do not include credentials, personal
information, or confidential project content. Redact examples and logs before
posting. GitHub hosts support submissions, and their visibility and retention are
subject to GitHub's policies. Public copies, notifications, and repository history
may persist even after content is edited or removed.

## Questions and changes

For privacy questions, contact the maintainers through
[GitHub Issues](https://github.com/Lusona/ai-skills/issues). Keep the initial request
free of sensitive details; ask how to arrange follow-up if needed.

We will update this file when the plugin's data handling changes and revise the
date above. Review your host agent's and connected services' policies separately.
