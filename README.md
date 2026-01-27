# Surrogate (代行者)

---

<p style="text-align: center;">
    <strong>生产准备的代理、技能、钩子、命令、规则和 MCP 配置。
</strong>
</p>

## 项目介绍


## 主要组成（仓库结构概览 + 参考清单）

## 核心作用/解决什么问题

## 目录内容介绍

```
surrogate/
|-- .claude-plugin/   # Plugin and marketplace manifests
|   |-- plugin.json         # Plugin metadata and component paths
|   |-- marketplace.json    # Marketplace catalog for /plugin marketplace add
|
|-- agents/           # Specialized subagents for delegation
|   |-- planner.md           # Feature implementation planning
|   |-- architect.md         # System design decisions
|   |-- tdd-guide.md         # Test-driven development
|   |-- code-reviewer.md     # Quality and security review
|   |-- security-reviewer.md # Vulnerability analysis
|   |-- build-error-resolver.md
|   |-- e2e-runner.md        # Playwright E2E testing
|   |-- refactor-cleaner.md  # Dead code cleanup
|   |-- doc-updater.md       # Documentation sync
|
|-- skills/           # 技能列表
|   |-- coding-standards/           # Language best practices
|   |-- backend-patterns/           # API, database, caching patterns
|   |-- frontend-patterns/          # React, Next.js patterns
|   |-- continuous-learning/        # Auto-extract patterns from sessions (Longform Guide)
|   |-- continuous-learning-v2/     # Instinct-based learning with confidence scoring
|   |-- iterative-retrieval/        # Progressive context refinement for subagents
|   |-- strategic-compact/          # Manual compaction suggestions (Longform Guide)
|   |-- tdd-workflow/               # TDD methodology
|   |-- security-review/            # Security checklist
|   |-- eval-harness/               # Verification loop evaluation (Longform Guide)
|   |-- verification-loop/          # Continuous verification (Longform Guide)
|
|-- commands/         # 命令列表
|   |-- tdd.md              # /tdd - Test-driven development
|   |-- plan.md             # /plan - Implementation planning
|   |-- e2e.md              # /e2e - E2E test generation
|   |-- code-review.md      # /code-review - Quality review
|   |-- build-fix.md        # /build-fix - Fix build errors
|   |-- refactor-clean.md   # /refactor-clean - Dead code removal
|   |-- learn.md            # /learn - Extract patterns mid-session (Longform Guide)
|   |-- checkpoint.md       # /checkpoint - Save verification state (Longform Guide)
|   |-- verify.md           # /verify - Run verification loop (Longform Guide)
|   |-- setup-pm.md         # /setup-pm - Configure package manager (NEW)
|
|-- rules/            # 固定规则
|   |-- security.md         # Mandatory security checks
|   |-- coding-style.md     # Immutability, file organization
|   |-- testing.md          # TDD, 80% coverage requirement
|   |-- git-workflow.md     # Commit format, PR process
|   |-- agents.md           # When to delegate to subagents
|   |-- performance.md      # Model selection, context management
|
|-- hooks/            # 钩子
|   |-- hooks.json                # All hooks config (PreToolUse, PostToolUse, Stop, etc.)
|   |-- memory-persistence/       # Session lifecycle hooks (Longform Guide)
|   |-- strategic-compact/        # Compaction suggestions (Longform Guide)
|
|-- scripts/          # Cross-platform Node.js scripts (NEW)
|   |-- lib/                     # Shared utilities
|   |   |-- utils.js             # Cross-platform file/path/system utilities
|   |   |-- package-manager.js   # Package manager detection and selection
|   |-- hooks/                   # Hook implementations
|   |   |-- session-start.js     # Load context on session start
|   |   |-- session-end.js       # Save state on session end
|   |   |-- pre-compact.js       # Pre-compaction state saving
|   |   |-- suggest-compact.js   # Strategic compaction suggestions
|   |   |-- evaluate-session.js  # Extract patterns from sessions
|   |-- setup-package-manager.js # Interactive PM setup
|
|-- tests/            # Test suite (NEW)
|   |-- lib/                     # Library tests
|   |-- hooks/                   # Hook tests
|   |-- run-all.js               # Run all tests
|
|-- contexts/         # 动态系统提示注入
|   |-- dev.md              # Development mode context
|   |-- review.md           # Code review mode context
|   |-- research.md         # Research/exploration mode context
|
|-- examples/         # 长期记忆 项目，用户级
|   |-- CLAUDE.md           # Example project-level config
|   |-- user-CLAUDE.md      # Example user-level config
|
|-- mcp-configs/      # mcp配置
|   |-- mcp-servers.json    # GitHub, Supabase, Vercel, Railway, etc.
|
|-- marketplace.json  # Self-hosted marketplace config (for /plugin marketplace add)
```


## hooks(钩子)

- Hook 事件类型

| 事件类型           | 触发时机                                          | 典型用途                                           |
|------------------|--------------------------------------------------|------------------------------------------------|
| PreToolUse       | 在工具成功完成后立即运行。                           | 创建工具参数之后和处理工具调用之前运行 , 来允许、拒绝或请求使用工具的权限         |
| PostToolUse      | tool_input 和 tool_response  的确切模式取决于工具    | 权限检查、参数验证 ~ 日志记录、结果处理                          |
| UserPromptSubmit | 输入  用户提交提示词前                               | 验证、修改提示词                                       |
| PreCompact       | /compact 的内容。对于 auto                         | 即将运行压缩操作之前运行                                   |
| SessionStart     | 会话开始                                           | 启动新会话或恢复现有会话时运行（目前在幕后启动新会话）                    |
| SessionEnd       | 会话结束                                           | 对于清理任务、记录会话统计信息或保存会话状态很有用                      |


- 环境变量
```
# 在 Hook 脚本中

echo "Project dir: $CLAUDE_PROJECT_DIR"
# /Users/john/projects/myapp

echo "Plugin root: $CLAUDE_PLUGIN_ROOT"
# /Users/john/.claude/plugins/security-hooks

echo "Env file: $CLAUDE_ENV_FILE"
# /tmp/claude-env-abc123 (SessionStart only)

echo "Remote mode: $CLAUDE_CODE_REMOTE"
# (空 或 "true")

```

## contexts        高级：动态系统提示注入
不要只把所有内容放进 CLAUDE.md（用户范围）或“.claude/rules/”（项目范围），这些文件每次会话都会加载，而是用 CLI 标志动态注入上下文。

```bash
claude --system-prompt "$(cat memory.md)"
```
这样你就能更精准地决定什么上下文什么时候加载。你可以根据你正在做的内容，每场会话注入不同的上下文。

```bash
# 日常开发
alias claude-dev='claude --system-prompt "$(cat ~/.claude/contexts/dev.md)"'

# PR审核模式
alias claude-review='claude --system-prompt "$(cat ~/.claude/contexts/review.md)"'

# 研究/探索模式
alias claude-research='claude --system-prompt "$(cat ~/.claude/contexts/research.md)"'
```
## 参考资料
* 上下文注入： https://x.com/affaanmustafa/status/2014040193557471352 
* hooks机制详解： https://blog.csdn.net/qq_44810930/article/details/156146071
