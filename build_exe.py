"""
打包脚本 - 将WeLearn自动学习工具打包成exe文件
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

    # 收集PyQt5的所有子模块
    pyqt5_hidden_imports = []
    for module in ['QtCore', 'QtGui', 'QtWidgets', 'QtNetwork', 'QtPrintSupport', 'QtSvg', 'QtWebEngineWidgets']:
        pyqt5_hidden_imports.append(f'--hidden-import=PyQt5.{module}')
    
    # PyInstaller参数
    args = [
        '--name=WeLearnAuto',  # 应用程序名称
        '--windowed',  # 创建窗口应用程序（无控制台）
        '--onefile',  # 打包成单个exe文件
        '--clean',  # 清理临时文件
        '--collect-all=PyQt5',  # 收集所有PyQt5相关模块
        '--collect-all=requests',  # 收集所有requests相关模块
        f'--add-data={os.path.join(project_dir, "ui")};ui',
        f'--add-data={os.path.join(project_dir, "core")};core',
        f'--hidden-import=PyQt5',
        f'--hidden-import=requests',
        f'--hidden-import=PyQt5.sip',
        f'--hidden-import=PyQt5.QtCore',
        f'--hidden-import=PyQt5.QtGui',
        f'--hidden-import=PyQt5.QtWidgets',
        *pyqt5_hidden_imports,  # 展开PyQt5子模块导入
        '--noconsole',  # 不显示控制台窗口
        os.path.join(project_dir, 'main.py'),  # 主程序路径
    ]

    # 如果存在README.md，也添加进去
    readme_path = os.path.join(project_dir, 'README.md')
    if os.path.exists(readme_path):
        args.append(f'--add-data={readme_path};.')

    print("开始打包 WeLearnAuto 应用程序...")
    print("参数:", " ".join(args))
    
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