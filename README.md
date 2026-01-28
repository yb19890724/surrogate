# Surrogate (代行者)

---

<p style="text-align: center;">
    <strong>生产准备的代理、技能、钩子、命令、规则和 MCP 配置。
</strong>
</p>

## 项目介绍

Ai编程助手 的“全家桶”配置仓库/插件：把常用的 agents（子代理）、skills（工作流技能）、slash commands（斜杠命令）、rules（规则约束）、hooks（事件钩子自动化）、以及 MCP server 配置示例集中在一起，提供一套可直接复用的工程化工作流。

> README 的定位： —— 仓库提供的是配置与代码本体，配套指南负责讲清楚方法论与使用方式。

## 核心作用/解决什么问题

1. 把高频工程能力产品化：将规划、架构评审、代码评审、安全审查、TDD 等能力沉淀为可调用的 agents/skills/commands。
2. 固化为流程：通过 rules + commands + hooks，将“先计划/先测试/再实现/再验证”的做事方式变成工具行为，而不是依赖使用者记忆。
3. 减少跨项目迁移成本：提供一套通用的目录结构与可拷贝配置（手动安装）或插件安装方式（推荐）。
4. 统一工具链与脚本习惯：内置包管理器选择/配置逻辑（自动探测），以及测试运行脚本与示例。

## 主要组成（仓库结构概览 + 参考清单）

> 说明：以下清单主要依据该仓库 README 与目录命名进行盘点，用于“我该什么时候用什么”的速查。若你需要更精确的行为细节，建议再打开对应 .md 文件看提示词/约束原文。

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
### plugin/（插件包装）


### agents/（子代理：把任务委派给专职角色）
| Agent 文件                    | 什么时候用                                          | 你会得到什么                          |
|------------------------------|----------------------------------------------------|---------------------------------|
| planner.md                   | 需求不清晰、要做一个功能/改造，且涉及多步实现时            | 分步骤实现计划、关键文件定位、风险点与验收口径         |
| architect.md                 | 需要做架构取舍（模块边界、扩展性、性能、技术选型）时         | 设计方案、权衡点、建议的目录/接口形态             |
| tdd-guide.md                 | 想用 TDD 写新功能/修 bug（先测试后实现）时                | 测试优先的落地步骤与覆盖率/边界用例建议            |
| code-reviewer.md             | 写完一段代码（提交/PR 前）想做质量审查时                  | 可维护性/一致性/潜在 bug/风格问题清单与修改建议     |
| refactor-cleaner.md          | 想删死代码、合并重复实现、降低维护成本时                    | 基于工具的死代码扫描与安全删改建议               |
| doc-updater.md               | 改了代码想同步文档/README/codemap 时                    | 更新文档、补齐使用说明/变更点                 |


### skills/（技能：把方法论沉淀成可复用流程）

| Skill 目录                   | 适用场景（怎么选）                       | 覆盖内容                                  |
|----------------------------|----------------------------------------|---------------------------------------|
| coding-standards/          | 你希望团队/项目有一致的编码规范                       | TypeScript/JS/通用代码规范与最佳实践             |
| backend-patterns/          | 做 API、服务端逻辑、数据库/缓存/队列等                 | 后端架构模式、API 设计、性能与可维护性建议               |
| tdd-workflow/              | 想严格执行"测试先行"                            | TDD 流程、测试分层、覆盖率目标/策略                  |
| security-review/           | 做安全评估/上线前安全检查                          | 安全检查清单、常见漏洞与修复建议                      |
| strategic-compact/         | 上下文变长、模型开始"遗忘/跑偏"                      | 何时手动压缩、如何保留关键信息                       |
| continuous-learning/       | 想把一次次会话产出沉淀成可复用模式                      | 从会话提炼规则/技能的流程（偏方法论）                   |
| verification-loop/         | 想避免"说改好了但没验证"                          | 验证闭环（跑测试/检查输出/给证据）流程                  |
| eval-harness/              | 需要做更系统的评估/回归框架                         | 会话/修改的评估方法与框架化建议                      |


### commands/（斜杠命令：一键触发预设工作流）

| Command 文件            | 适用场景                                      | 功能                             |
|-----------------------|-----------------------------------------------|--------------------------------|
| tdd.md                | 想用 TDD 写新功能/修 bug（先测试后实现）时          | 测试优先的落地步骤与覆盖率/边界用例建议           |
| plan.md               | 需求不清晰、要做一个功能/改造，且涉及多步实现时        | 分步骤实现计划、关键文件定位、风险点与验收口径        |
| e2e.md                | 关键用户路径需要端到端回归（Playwright）时           | 生成/维护/执行 E2E 用例与产物（截图/trace 等） |
| code-review.md        | 写完一段代码（提交/PR 前）想做质量审查时            | 可维护性/一致性/潜在 bug/风格问题清单与修改建议    |
| build-fix.md          | CI/本地 build 报错（TS/依赖/构建链路）时           | 最小改动修复编译/构建错误、定位原因             |
| refactor-clean.md     | 想删死代码、合并重复实现、降低维护成本时             | 基于工具的死代码扫描与安全删改建议              |
| learn.md              | 想从会话中提炼模式/技能时                           | 从会话中提炼模式/技能的流程                 |
| checkpoint.md         | 想保存当前验证状态时                               | 保存验证状态                         |
| verify.md             | 想运行验证循环时                                   | 运行验证循环                         |
| setup-pm.md           | 想配置包管理器时                                   | 配置包管理器                         |


### rules/（规则：常驻约束，限制助手行为）

| Rule 文件              | 作用                  | 典型内容                        |
|-----------------------|-----------------------|-----------------------------|
| security.md           | 安全底线                  | 禁止泄漏密钥、避免注入/不安全操作等          |
| coding-style.md       | 代码风格一致性              | 目录组织、命名、可读性等                |
| testing.md            | 测试纪律                  | TDD/覆盖率目标/测试要求              |
| git-workflow.md       | Git 流程规范              | 提交信息、分支/PR 习惯               |
| agents.md             | 代理使用策略               | 何时委派、如何拆任务                  |
| performance.md        | 性能与上下文管理            | 工具/模型选择、上下文窗口管理建议           |


### hooks/ (钩子)

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

### contexts        高级：动态系统提示注入
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

### 安装/使用方式（README 提供的两种路线）

### 参考资料
* 工程理解： https://github.com/affaan-m/everything-claude-code 
* 汉化 https://mp.weixin.qq.com/s/BkqigXb1ugP4IBjiwRAGOA
* 上下文注入： https://x.com/affaanmustafa/status/2014040193557471352 
* hooks机制详解： https://blog.csdn.net/qq_44810930/article/details/156146071
