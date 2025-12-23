#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Git快速提交脚本
执行 git add . && git commit -m "auto commit" && git push origin master
"""

import subprocess
import sys
import os


def run_cmd(cmd):
    """执行命令并打印输出"""
    print(f"执行: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=os.getcwd())
    return result.returncode == 0


def main():
    """执行Git提交序列"""
    print("开始Git提交流程...")
    
    # 检查是否在Git仓库中
    if not os.path.exists(".git"):
        print("错误: 当前目录不是Git仓库")
        sys.exit(1)
    
    commands = [
        "git add .",
        'git commit -m "auto commit"',
        "git push origin master"
    ]
    
    for cmd in commands:
        success = run_cmd(cmd)
        if not success:
            print(f"命令 '{cmd}' 执行失败")
            sys.exit(1)
        print()  # 空行分隔
    
    print("Git提交流程完成！")


if __name__ == "__main__":
    main()