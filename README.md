# Tkinter/QT

## QT安裝方式

### Windows

#### Step1. 下載

[請選最新版](https://download.qt.io/archive/qt/)

#### Step2. 安裝

記得選 QT

![](https://github.com/grand-coder/stmicro3/raw/master/qtstep1.png)

### MAC

#### Step0. 安裝homebrew

終端機輸入

> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#### Step1. 安裝QT5

> brew install qt5

#### Step2. 安裝QT creator

> brew cask install qt-creator

## PyQT

### 安裝方式

請使用 PyCharm Settings 或者 命令列 安裝 PyQT5

## Pyuic5

Pyuic可以幫你把.ui檔轉換成.py檔案

### 指令

> pyuic5 xxxx.ui -o xxxx.py

## PyInstaller

### 指令

windows -add-data請把:換成;

#### 普通

> pyinstaller --add-data "command.ui:." commandapp.py

#### 無console

> pyinstaller --noconsole -add-data "command.ui:." commandapp.py

#### 一隻檔案

> pyinstaller --noconsole --onefile -add-data "command.ui:." commandapp.py

