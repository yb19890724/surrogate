#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UserPromptSubmit Hook - 用户提交时触发，评估当前技能
"""

import json
import sys

prompt = """## 指令：强制技能激活流程(必须执行)
### 步骤 1- 评估(必须在响应中明确展示)
针对以下每个技能，陈述:[技能名]- 是/否 -[理由]

可用技能列表:
- api-doc：生成 API 文档
- load-rpc：加载新的 jsonrpc 接口文件
- p-g：代码生成/PHP代码规范/重构PHP代码/优化代码
- p-t：PHP测试/PHP单元测试/phpunit测试/rpc接口测试/函数测试

### 步骤 2- 激活技能(紧接着步骤1立即执行)
### 步骤 3- 实现
**关键规则**:
1. 你必须在步骤2 调用 SKills() 工具，不要跳过直接实现
2. 评估(步骤 1)如果不激活(步骤 2)就毫无价值
3. 多个技能相关时，全部激活

**正确流程示例**:

评估结果:
- p-g：设计代码开发等                 ✅
- p-t: 用户代码单元测试开发            ✅
- load-rpc：加载新的 jsonrpc 接口文件  ✅

激活技能
Skills(p-t)
Skills(p-g)
Skills(load-rpc)

"""

def main():
    # 读取标准输入的 JSON 数据
    if not sys.stdin.isatty():
        try:
            input_data = sys.stdin.read()
            if input_data.strip():
                jsonData = json.loads(input_data)

                user_prompt = jsonData.get("prompt", "")
                if user_prompt.strip().startswith("/"):
                    sys.exit(0)
        except json.JSONDecodeError as e:
            sys.exit(0)
    
    # 输出预定义的提示内容
    print(prompt)

if __name__ == '__main__':
    main()
