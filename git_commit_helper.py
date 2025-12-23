#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Git自动化提交脚本
用于简化Git提交和推送流程
"""

import subprocess
import sys
import os
from datetime import datetime


def run_command(cmd, cwd=None):
    """
    执行命令并返回结果
    :param cmd: 命令列表
    :param cwd: 工作目录
    :return: (success, output)
    """
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            shell=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def git_status_check():
    """检查Git仓库状态"""
    success, stdout, stderr = run_command("git status --porcelain")
    if not success:
        print(f"错误: 无法检查Git状态\n{stderr}")
        return False
    
    if not stdout.strip():
        print("提示: 没有发现任何变更，无需提交。")
        return False
    
    print("发现以下变更:")
    print(stdout)
    return True


def git_add_all():
    """添加所有变更到暂存区"""
    print("正在添加所有变更...")
    success, stdout, stderr = run_command("git add .")
    if not success:
        print(f"错误: git add 失败\n{stderr}")
        return False
    print("✓ 所有变更已添加")
    return True


def git_commit(message="auto commit"):
    """提交变更"""
    print(f"正在提交变更...")
    success, stdout, stderr = run_command(f'git commit -m "{message}"')
    if not success:
        if "nothing to commit" in stderr.lower():
            print("提示: 没有需要提交的变更。")
            return False
        else:
            print(f"错误: git commit 失败\n{stderr}")
            return False
    print("✓ 变更已提交")
    return True


def git_push():
    """推送到远程仓库"""
    print("正在推送变更到远程仓库...")
    success, stdout, stderr = run_command("git push origin master")
    if not success:
        print(f"错误: git push 失败\n{stderr}")
        print("\n可能的解决方案:")
        print("1. 检查网络连接")
        print("2. 确保SSH密钥配置正确")
        print("3. 验证您对仓库有推送权限")
        return False
    print("✓ 变更已推送")
    return True


def main():
    """主函数"""
    print("="*50)
    print("Git自动化提交脚本")
    print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)
    
    # 检查是否在Git仓库中
    if not os.path.exists(".git"):
        print("错误: 当前目录不是Git仓库")
        sys.exit(1)
    
    # 检查是否有变更
    if not git_status_check():
        print("没有发现变更，退出。")
        return
    
    # 获取提交信息
    commit_message = input("请输入提交信息 (直接回车使用默认信息 'auto commit'): ").strip()
    if not commit_message:
        commit_message = "auto commit"
    
    # 执行Git操作序列
    operations = [
        ("添加变更", git_add_all),
        ("提交变更", lambda: git_commit(commit_message)),
        ("推送变更", git_push)
    ]
    
    for operation_name, operation_func in operations:
        print(f"\n{operation_name}...")
        if not operation_func():
            print(f"{operation_name} 失败，停止执行。")
            sys.exit(1)
        print(f"✓ {operation_name} 完成")
    
    print("\n" + "="*50)
    print("所有操作成功完成！")
    print("="*50)


if __name__ == "__main__":
    main()