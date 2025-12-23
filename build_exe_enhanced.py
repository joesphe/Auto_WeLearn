"""
增强版打包脚本 - 专门针对PyQt5应用程序进行优化
"""
import os
import sys
import shutil
from PyInstaller.utils.hooks import collect_submodules, collect_data_files
import PyInstaller.__main__

def build_exe():
    # 获取项目根目录
    project_dir = os.path.dirname(os.path.abspath(__file__))

    # 清理之前的构建文件
    build_dir = os.path.join(project_dir, 'build')
    dist_dir = os.path.join(project_dir, 'dist')
    
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
        print("已清理旧的build目录")
    
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
        print("已清理旧的dist目录")

    # 为PyQt5添加所有可能需要的模块
    hidden_imports = [
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'PyQt5.QtNetwork',
        'PyQt5.QtPrintSupport',
        'PyQt5.QtSvg',
        'PyQt5.QtWebEngineWidgets',  # 可能需要
        'PyQt5.sip',
        'requests',
        'urllib3',
        'chardet',
        'certifi',
        'idna',
        'charset_normalizer',
        # 项目特定模块
        'core',
        'ui',
        'core.account_manager',
        'core.api',
        'core.batch_manager',
        'core.crypto',
        'ui.main_window',
        'ui.account_view',
        'ui.account_detail',
        'ui.workers',
    ]

    # 收集ui和core包的所有子模块
    hidden_imports.extend(collect_submodules('ui'))
    hidden_imports.extend(collect_submodules('core'))

    # 构建参数列表
    args = [
        '--name=WeLearnAuto',  # 应用程序名称
        '--windowed',  # 创建窗口应用程序（无控制台）
        '--onefile',  # 打包成单个exe文件
        '--clean',  # 清理临时文件
        '--noconsole',  # 不显示控制台窗口
        '--icon=icon.ico',  # 应用程序图标
    ]

    # 添加所有隐藏导入
    for imp in hidden_imports:
        args.append(f'--hidden-import={imp}')

    # 添加数据文件
    args.extend([
        f'--add-data={os.path.join(project_dir, "ui")};ui',
        f'--add-data={os.path.join(project_dir, "core")};core',
    ])

    # 如果存在README.md，也添加进去
    readme_path = os.path.join(project_dir, 'README.md')
    if os.path.exists(readme_path):
        args.append(f'--add-data={readme_path};.')

    args.append(os.path.join(project_dir, 'main.py'))  # 主程序路径

    print("开始打包 WeLearnAuto 应用程序...")
    print(f"总共添加了 {len([arg for arg in args if arg.startswith('--hidden-import')])} 个隐藏导入")
    
    try:
        # 运行PyInstaller
        PyInstaller.__main__.run(args)
        print("\n打包成功完成！")
        print(f"生成的exe文件位于: {os.path.join(dist_dir, 'WeLearnAuto.exe')}")
    except Exception as e:
        print(f"打包过程中出现错误: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    build_exe()