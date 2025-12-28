# WeLearnAuto 打包说明

## 生成的文件

- `dist/WeLearnAuto.exe` - 主程序exe文件
- `build/WeLearnAuto/` - 构建过程中的临时文件

## 使用说明

直接运行 `WeLearnAuto.exe` 即可启动应用程序。

## 注意事项

1. 由于使用了 --onefile 参数，exe文件是自包含的，运行时会解压到临时目录
2. 首次运行可能会被安全软件误报，这是正常现象
3. 程序需要网络连接以实现WeLearn平台的自动学习功能

## 重新打包

如果需要重新打包应用程序，可以使用以下方法之一：

### 方法1：使用增强版打包脚本（推荐）
```bash
python build_exe_enhanced.py
```

### 方法2：使用完整的spec文件（最全面，但文件较大）
```bash
pyinstaller WeLearnAuto_fixed2.spec
```

## 最新打包说明

使用 `WeLearnAuto_fixed2.spec` 文件成功解决了PyQt5模块缺失问题，生成的exe文件大小为66MB，包含了所有必要的PyQt5组件。

## 应用程序图标

应用程序现在使用自定义图标 `icon.ico`：
- 图标文件位于项目根目录
- 在spec文件和增强版打包脚本中都已配置图标
- 重新打包后exe文件将显示自定义图标







