# RKNN-yolov5-videostream

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

基于 [leafqycc/rknn-multi-threaded](https://github.com/leafqycc/rknn-multi-threaded) 的改进版本，适配最新 RKNN-Toolkit2 并新增多项优化功能，专为 Rockchip NPU 设备设计的高效多线程推理框架。

## ✨ 主要特性

- ✅ **多线程推理优化**：充分利用 NPU 计算资源，提升吞吐量
- ✅ **支持 YOLOv5 系列模型**：包括 `yolov5s_relu`/`yolov5n`/`yolov5s`/`yolov5m`
- ✅ **自适应缩放优化**：改进等比例缩放算法，减少图像变形
- ✅ **原尺寸画面标注**：支持在原始分辨率画面直接绘制检测框
- ✅ **RKNN-Toolkit2 2.3.0 适配**：兼容最新版本工具链

## 🚀 更新亮点（相比原项目）

- **版本升级**：全面适配 `rknn-toolkit2-2.3.0`
- **视觉优化**：重构缩放算法，保持图像宽高比不变
- **标注增强**：检测框可直接映射到原始分辨率画面
- **模型扩展**：新增支持 4 种 YOLOv5 变体模型

## 📦 安装与使用

### 环境要求
- Python 3.8
- RKNN-Toolkit2 == 2.3.0
- OpenCV >= 4.5
- Rockchip NPU 设备（RK3588验证通过）

### 快速开始
```bash
# 构建python虚拟环境，开始步骤前确保板卡联网
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
./Miniconda3-latest-Linux-aarch64.sh -b -p /opt/miniconda3

# 新建虚拟环境，python3.8版本
source /opt/miniconda3/bin/activate
conda create -n rknnlite-env python=3.8
conda activate rknnlite-env

# 安装依赖
pip install opencv-python --index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install rknn_toolkit_lite2-2.3.0-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl --index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 克隆仓库
git clone https://github.com/hdydy/rknn-yolov5-videostream.git
cd rknn-yolov5-videostream

# 运行示例
python main.py
```

## 🎯 支持模型
| 模型名称        | 输入尺寸  | 适用场景          |
|----------------|-----------|-------------------|
| yolov5s_relu   | 640x640   | 低功耗设备        |
| yolov5n        | 640x640   | 极简模型          |
| yolov5s        | 640x640   | 平衡精度/速度     |
| yolov5m        | 640x640   | 高精度需求        |

## 📜 许可证
本项目基于 [Apache License 2.0](LICENSE) 授权，使用请遵守：
- 保留原始版权声明
- 修改文件需添加变更说明

## 🙏 致谢
- 原始项目作者 [leafqycc](https://github.com/leafqycc)
- RKNN-Toolkit2 开发团队