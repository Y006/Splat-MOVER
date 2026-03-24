#!/usr/bin/env bash
set -e

echo "===== Basic ====="
whoami || true
hostname || true
uname -a || true

echo
echo "===== Conda / Python ====="
which conda || true
conda --version || true
which python || true
python --version || true
which pip || true
pip --version || true

echo
echo "===== NVIDIA / CUDA ====="
nvidia-smi || true
which nvcc || true
nvcc --version || true

echo
echo "===== Build tools ====="
which gcc || true
gcc --version || true
which g++ || true
g++ --version || true
which make || true
make --version || true

echo
echo "===== Runtime tools ====="
which ffmpeg || true
ffmpeg -version || true

echo
echo "===== Env vars ====="
echo "CUDA_HOME=$CUDA_HOME"
echo "CONDA_PREFIX=$CONDA_PREFIX"
echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH"

echo
echo "===== Python imports ====="
python - <<'PY'
import ctypes.util
print("libGL:", ctypes.util.find_library("GL"))
print("glib-2.0:", ctypes.util.find_library("glib-2.0"))

mods = [
    "torch", "torchvision", "nerfstudio", "gsplat", "tinycudann",
    "lang_sam", "open3d", "sklearn", "cv2", "roma"
]
for m in mods:
    try:
        mod = __import__(m)
        ver = getattr(mod, "__version__", "unknown")
        print(f"{m}: OK ({ver})")
    except Exception as e:
        print(f"{m}: FAIL ({e})")

try:
    import torch
    print("torch.cuda.is_available:", torch.cuda.is_available())
    print("torch.version.cuda:", torch.version.cuda)
except Exception:
    pass
PY

echo
echo "===== Nerfstudio CLI ====="
which ns-train || true
ns-train --help | grep -E 'segsplat|sagesplat' || true