# MCP AI Assistant

MCP AI Assistant is an opinionated orchestration layer designed to help multi-agent workflows unlock human-like coding velocity. The assistant pairs planning, execution, and QA capabilities with extensible tools (search, terminal, agent tooling) to automate tasks inside the MCP developer platform.

### Key capabilities

- **Directed planning**: Uses structured reasoning to break down user requests into actionable steps while consulting the workspace state.
- **Safe tooling**: Routes operations through vetted subagents (code search, file readers, terminal commands) and obeys strict sandbox policies.
- **Adaptive communication**: Responds with concise summaries, highlights risks, and references relevant files/lines when executing developer commands.

### Technology snapshot

- **Node.js + TypeScript (workspace default)** for orchestrating tool responses.
- **ESLint + Prettier** for consistent formatting and quality.
- **Workspace-aware memory** for remembering user preferences or key project info when relevant.

### Getting started

1. Clone the repository and install dependencies with `npm install`.
2. Open a coding task by describing the desired change to the assistant.
3. Monitor status updates and review files the assistant modifies.

Because this assistant operates within the MCP UI, there is no standalone server to run locally; tasks are executed interactively via the provided agent stack.