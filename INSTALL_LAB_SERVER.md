# Splat-MOVER 实验室服务器安装建议

这份文档以仓库当前代码为准，目标是给出一套在 Linux 实验室服务器上更稳妥的安装方案。核心原则是：

- 用 `conda` 隔离环境。
- 用 `uv` 安装 Python 依赖。
- 以仓库真实代码依赖为准，不直接照搬内置第三方子模块里的旧版 `requirements.txt`。

## 1. 推荐版本

建议使用下面这组版本：

| 组件 | 推荐版本 | 说明 |
| --- | --- | --- |
| OS | Ubuntu 20.04 / 22.04 | x86_64 + NVIDIA GPU |
| Python | `3.10` | 比仓库声明的 `>=3.8` 更稳；兼顾 `lang-sam` 与 `sklearn.cluster.HDBSCAN` |
| PyTorch | `2.1.2` | 与 Nerfstudio 1.1.0、VRB、CUDA 扩展更容易兼容 |
| torchvision | `0.16.2` | 与 `torch==2.1.2` 对应 |
| CUDA Toolkit | `11.8` | 兼顾 PyTorch wheel、`gsplat`、`pointnet2`、`knn` 编译 |
| Nerfstudio | `1.1.0` | 仓库 `README.md` 明确验证过 |
| gsplat | `0.1.13` | 仓库 `README.md` 明确验证过 |
| lang-segment-anything | `a1a9557` 提交 | 不建议装最新主干 |
| scikit-learn | `1.4.2` | 仓库 `utils/scene_editing_utils.py` 使用 `sklearn.cluster.HDBSCAN`，不能沿用 VRB 里的 `1.2.2` |
| Open3D | `0.18.0` | 兼容 Python 3.10，支持当前脚本用法 |

## 2. 先说几个关键坑

1. 不要直接照搬 `graspnet/graspnet_baseline/requirements.txt`。

它固定了 `torch==1.6`，这是上游旧基线环境，不适合当前项目的主环境。

2. 不要直接把 `graspnet/graspnetAPI/setup.py` 当成主安装入口。

它固定了 `numpy==1.20.3`，会和现代 Python / PyTorch 环境冲突；而本项目自己的抓取代码实际上是直接从仓库内路径导入 `graspnet` 代码，不需要先把这个旧包完整装成独立环境。

3. `lang-sam` 必须锁到仓库 README 指定的旧提交。

当前上游 `lang-segment-anything` 已经演化很大，直接装最新版本，和本仓库的训练/缓存逻辑不一定兼容。

4. `README.md` 里的训练命令名和 `pyproject.toml` 的插件键名不一致。

- `README.md` 写的是 `ns-train sagesplat`
- `pyproject.toml` 注册的是 `segsplat = 'sagesplat.sagesplat_config:sagesplat_method'`

实际使用前请先跑一次：

```bash
ns-train --help | grep -E 'segsplat|sagesplat'
```

以 CLI 真正列出来的方法名为准。大概率应该用 `segsplat`。

5. `scripts/eval.py`、`scripts/eval_scene_editing.py` 里的 `config_path = Path("<config.yml>")` 只是占位符。

训练后需要手动替换成实际生成的 Nerfstudio `config.yml` 路径。

6. `scripts/eval_scene_editing_left.py` 和 `scripts/eval_scene_editing_right.py` 带有作者本地绝对路径，且保留了 `pdb.set_trace()`，更适合作为参考脚本，不建议原样直接跑。

## 3. 系统依赖

先准备基础系统库：

```bash
sudo apt update
sudo apt install -y \
  build-essential \
  git \
  ffmpeg \
  libgl1 \
  libglib2.0-0 \
  libsm6 \
  libxext6 \
  libxrender1
```

说明：

- `build-essential`：编译 `pointnet2`、`knn`、`tiny-cuda-nn`
- `ffmpeg`：`utils/render_utils.py` 渲染视频时需要
- `libgl1` / `libglib2.0-0`：`opencv` / `open3d` 在服务器上常见缺失项

## 4. 创建 conda 环境

```bash
conda create -n splat-mover python=3.10 -y
conda activate splat-mover
python -m pip install -U pip uv
```

如果服务器已经有可用的 CUDA 11.8 Toolkit，并且 `nvcc --version` 正常，可以直接复用系统 CUDA。

如果服务器只有驱动、没有 `nvcc`，建议在环境里补一个 Toolkit：

```bash
conda install -y -c nvidia/label/cuda-11.8.0 cuda-toolkit
```

然后设置环境变量：

```bash
export CUDA_HOME="${CUDA_HOME:-$CONDA_PREFIX}"
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$CUDA_HOME/lib64:${LD_LIBRARY_PATH:-}"
```

如果你知道服务器 GPU 架构，也可以顺手设置：

```bash
export TORCH_CUDA_ARCH_LIST="8.0;8.6;8.9"
export TCNN_CUDA_ARCHITECTURES=86
```

上面两项不是强制，但能减少 `tiny-cuda-nn` / CUDA 扩展的编译歧义。

## 5. 用 uv 安装依赖

### 5.1 安装 PyTorch

```bash
uv pip install --index-url https://download.pytorch.org/whl/cu118 \
  torch==2.1.2 torchvision==0.16.2
```

### 5.2 安装 Nerfstudio / gsplat / 核心运行库

```bash
uv pip install \
  nerfstudio==1.1.0 \
  gsplat==0.1.13 \
  pytorch-msssim \
  torchmetrics \
  timm \
  ftfy \
  regex \
  tqdm \
  einops \
  gdown \
  matplotlib \
  numpy \
  pillow \
  torchtyping \
  pyyaml \
  scipy \
  scikit-learn==1.4.2 \
  open3d==0.18.0 \
  opencv-python-headless \
  transforms3d \
  trimesh \
  plotly \
  roma \
  jaxtyping \
  pymeshlab
```

说明：

- `pytorch-msssim`、`torchmetrics`、`tinycudann` 是 `sagesplat/sagesplat.py` 直接依赖。
- `scikit-learn==1.4.2` 是为了满足 `HDBSCAN`。
- `plotly` 主要给点云可视化脚本用。
- `roma` 用于场景编辑脚本中的四元数插值。
- `pymeshlab` 只在导出/后处理 mesh 时用到，但提前装好更省事。

### 5.3 安装 tiny-cuda-nn

`sagesplat/sagesplat.py` 直接 `import tinycudann as tcnn`，所以这一步不要省。

```bash
uv pip install ninja
uv pip install --no-build-isolation \
  "git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch"
```

### 5.4 安装 lang-sam（锁定旧提交）

```bash
uv pip install "git+https://github.com/luca-medeiros/lang-segment-anything.git@a1a9557"
```

不要安装最新主干版本替代这个提交。

补充一句：即使你只是加载已经训练好的 `config.yml` 做评估，当前自定义 `datamanager` 在初始化时也会导入 `AffordanceDataloader`，所以 `lang-sam` 仍然需要能被正常 `import`。

### 5.5 安装项目本体

这里建议用 `--no-deps`，原因是仓库 `pyproject.toml` 里包含一个额外的 `clip @ git+...` 依赖，但当前代码真正使用的是仓库内自带的 `sagesplat/clip` 改造版，不值得让安装过程再拉一套额外依赖树。

```bash
uv pip install --no-deps -e .
ns-install-cli
```

## 6. 编译 GraspNet 需要的本地 CUDA 扩展

本项目抓取部分真正需要的是 `graspnet_baseline` 里的两个扩展：`pointnet2` 和 `knn`。

直接用 `uv` 装本地包即可，不要再手工跑 `python setup.py install`：

```bash
uv pip install --no-build-isolation ./graspnet/graspnet_baseline/pointnet2
uv pip install --no-build-isolation ./graspnet/graspnet_baseline/knn
```

## 7. 安装后检查

先做 import 自检：

```bash
python - <<'PY'
import torch
import nerfstudio
import gsplat
import tinycudann
import lang_sam
import open3d
import sklearn
import roma
import pointnet2._ext
import knn_pytorch.knn_pytorch
print("torch:", torch.__version__)
print("cuda:", torch.version.cuda)
print("nerfstudio:", getattr(nerfstudio, "__version__", "unknown"))
print("gsplat: ok")
print("tinycudann: ok")
print("lang_sam: ok")
print("open3d:", open3d.__version__)
print("sklearn:", sklearn.__version__)
print("pointnet2: ok")
print("knn: ok")
PY
```

再检查 Nerfstudio 方法是否注册成功：

```bash
ns-train --help | grep -E 'segsplat|sagesplat'
```

如果这里没有看到方法名，优先检查两件事：

- 当前 shell 是否仍在 `splat-mover` 环境中
- `uv pip install --no-deps -e .` 和 `ns-install-cli` 是否执行成功

## 8. 训练与运行

### 8.1 训练

假设 `ns-train --help` 里列出的是 `segsplat`，训练命令应写成：

```bash
ns-train segsplat --data /path/to/scene
```

如果实际列出的是 `sagesplat`，就把命令里的方法名替换成 `sagesplat`。

第一次训练时，`SageSplatDataManager` 会为数据集建立缓存：

- `outputs/<scene_name>/dataloader/clip_*.npy`
- `outputs/<scene_name>/dataloader/affordance.npy`

这一步会调用 `LangSAM` 和仓库内置的 VRB 权重，首次运行较慢，属于正常现象。

仓库里已经自带两个关键权重文件：

- `sagesplat/vrb/models/model_checkpoint_1249.pth.tar`
- `graspnet/model_checkpoints/checkpoint-rs.tar`

因此通常不需要再单独下载这两份模型。

### 8.2 抓取评估 / 场景编辑脚本

训练结束后，把脚本里的占位路径改成真实 `config.yml`：

- `scripts/eval.py`
- `scripts/eval_scene_editing.py`

常见的 `config.yml` 路径形式类似：

```text
outputs/<scene_name>/sagesplat/<timestamp>/config.yml
```

注意：

- `scripts/eval_scene_editing.py` 额外依赖 `roma`
- `utils/render_utils.py` 额外依赖 `ffmpeg`
- `scripts/eval_scene_editing.py` 里保留了一条未使用的 `pytorch3d` 导入；若你确实要运行这个脚本，又不想额外装 `pytorch3d`，最省事的做法是先把那一行注释掉

## 9. 我建议的最小可执行路径

如果你的目标是“先把项目跑起来”，建议按下面顺序验证：

1. 完成环境安装与 import 自检。
2. 用 `ns-train --help` 确认方法名。
3. 先跑一次训练：`ns-train <method_name> --data /path/to/scene`
4. 训练完成后，把 `scripts/eval.py` 的 `config_path` 改成真实 `config.yml`
5. 再跑抓取评估脚本

这条路径最短，也最容易定位问题。

## 10. 一句话总结

最稳妥的做法是：`Python 3.10 + CUDA 11.8 + torch 2.1.2 + nerfstudio 1.1.0 + gsplat 0.1.13 + lang-sam@a1a9557`，然后只编译 `graspnet_baseline` 里的 `pointnet2/knn`，不要把 `graspnet` 自带的旧 requirements 当作主环境标准。
