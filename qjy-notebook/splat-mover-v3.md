```bash

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v2   20:24  
 conda create -n splat-mover-v3 python=3.10 -y
conda activate splat-mover-v3
python -m pip install -U pip uv
2 channel Terms of Service accepted
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3

  added / updated specs:
    - python=3.10


The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main 
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu 
  bzip2              pkgs/main/linux-64::bzip2-1.0.8-h5eee18b_6 
  ca-certificates    pkgs/main/linux-64::ca-certificates-2025.12.2-h06a4308_0 
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.44-h9e0c5a2_3 
  libexpat           pkgs/main/linux-64::libexpat-2.7.4-h7354ed3_0 
  libffi             pkgs/main/linux-64::libffi-3.4.4-h6a678d5_1 
  libgcc             pkgs/main/linux-64::libgcc-15.2.0-h69a1729_7 
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-15.2.0-h166f726_7 
  libgomp            pkgs/main/linux-64::libgomp-15.2.0-h4751f2c_7 
  libnsl             pkgs/main/linux-64::libnsl-2.0.0-h5eee18b_0 
  libstdcxx          pkgs/main/linux-64::libstdcxx-15.2.0-h39759b7_7 
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-15.2.0-hc03a8fd_7 
  libuuid            pkgs/main/linux-64::libuuid-1.41.5-h5eee18b_0 
  libxcb             pkgs/main/linux-64::libxcb-1.17.0-h9b100fa_0 
  libzlib            pkgs/main/linux-64::libzlib-1.3.1-hb25bd0a_0 
  ncurses            pkgs/main/linux-64::ncurses-6.5-h7934f7d_0 
  openssl            pkgs/main/linux-64::openssl-3.5.5-h1b28b03_0 
  packaging          pkgs/main/linux-64::packaging-25.0-py310h06a4308_1 
  pip                pkgs/main/noarch::pip-26.0.1-pyhc872135_0 
  pthread-stubs      pkgs/main/linux-64::pthread-stubs-0.3-h0ce48e5_1 
  python             pkgs/main/linux-64::python-3.10.20-h741d88c_0 
  readline           pkgs/main/linux-64::readline-8.3-hc2a1206_0 
  setuptools         pkgs/main/linux-64::setuptools-80.10.2-py310h06a4308_0 
  sqlite             pkgs/main/linux-64::sqlite-3.51.2-h3e8d24a_0 
  tk                 pkgs/main/linux-64::tk-8.6.15-h54e0aa7_0 
  tzdata             pkgs/main/noarch::tzdata-2026a-he532380_0 
  wheel              pkgs/main/linux-64::wheel-0.46.3-py310h06a4308_0 
  xorg-libx11        pkgs/main/linux-64::xorg-libx11-1.8.12-h9b100fa_1 
  xorg-libxau        pkgs/main/linux-64::xorg-libxau-1.0.12-h9b100fa_0 
  xorg-libxdmcp      pkgs/main/linux-64::xorg-libxdmcp-1.1.5-h9b100fa_0 
  xorg-xorgproto     pkgs/main/linux-64::xorg-xorgproto-2024.1-h5eee18b_1 
  xz                 pkgs/main/linux-64::xz-5.8.2-h448239c_0 
  zlib               pkgs/main/linux-64::zlib-1.3.1-hb25bd0a_0 



Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate splat-mover-v3                                                    unbound keyseq: paste_end
#
# To deactivate an active environment, use
#
#     $ conda deactivate

Requirement already satisfied: pip in /share3/home/qiujinyu/miniconda3/envs/splat-mover-v                         kages (26.0.1)
Collecting uv
  Using cached uv-0.11.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
Using cached uv-0.11.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (24.5 MB)
Installing collected packages: uv
Successfully installed uv-0.11.0
[ble: elapsed 20.725s (CPU 60.9%)] conda create -n splat-mover-v3 python=3.10 -y

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:25  
 uv pip install --index-url https://download.pytorch.org/whl/cu118 \
  torch==2.1.2 torchvision==0.16.2
uv pip install "numpy<2"
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 18 packages in 5.37s
Installed 18 packages in 172ms
 + certifi==2022.12.7
 + charset-normalizer==2.1.1
 + filelock==3.25.2
 + fsspec==2026.2.0
 + idna==3.4
 + jinja2==3.1.6
 + markupsafe==3.0.2
 + mpmath==1.3.0
 + networkx==3.4.2
 + numpy==2.2.6
 + pillow==12.1.1
 + requests==2.28.1
 + sympy==1.14.0
 + torch==2.1.2+cu118
 + torchvision==0.16.2+cu118
 + triton==2.1.0
 + typing-extensions==4.15.0
 + urllib3==1.26.13
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 1 package in 696ms
Uninstalled 1 package in 21ms
Installed 1 package in 37ms
 - numpy==2.2.6
 + numpy==1.26.4

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:26  
 python - <<'PY'
import torch
print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())
PY
2.1.2+cu118
11.8
True
[ble: elapsed 4.639s (CPU 251.1%)] python - <<'PY'

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:26  
 mkdir -p "$CONDA_PREFIX/etc/conda/activate.d"
cat > "$CONDA_PREFIX/etc/conda/activate.d/splat_mover_env.sh" <<'EOF'
export CUDA_HOME=/usr/local/cuda
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$CUDA_HOME/lib64:${LD_LIBRARY_PATH:-}"
export TORCH_CUDA_ARCH_LIST="8.9"
export TCNN_CUDA_ARCHITECTURES=89
EOF
conda deactivate
conda activate splat-mover-v3

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:27  
 echo $CUDA_HOME
which nvcc
nvcc --version
/usr/local/cuda
/usr/local/cuda/bin/nvcc
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Tue_Aug_15_22:02:13_PDT_2023
Cuda compilation tools, release 12.2, V12.2.140
Build cuda_12.2.r12.2/compiler.33191640_0

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:27  
 conda install -y -c nvidia/label/cuda-11.8.0 cuda-toolkit
2 channel Terms of Service accepted
Channels:
 - nvidia/label/cuda-11.8.0
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3

  added / updated specs:
    - cuda-toolkit


The following NEW packages will be INSTALLED:

  cuda-cccl          nvidia/label/cuda-11.8.0/linux-64::cuda-cccl-11.8.89-0 
  cuda-command-line~ nvidia/label/cuda-11.8.0/linux-64::cuda-command-line-tools-11.8.0-0 
  cuda-compiler      nvidia/label/cuda-11.8.0/linux-64::cuda-compiler-11.8.0-0 
  cuda-cudart        nvidia/label/cuda-11.8.0/linux-64::cuda-cudart-11.8.89-0 
  cuda-cudart-dev    nvidia/label/cuda-11.8.0/linux-64::cuda-cudart-dev-11.8.89-0 
  cuda-cuobjdump     nvidia/label/cuda-11.8.0/linux-64::cuda-cuobjdump-11.8.86-0 
  cuda-cupti         nvidia/label/cuda-11.8.0/linux-64::cuda-cupti-11.8.87-0 
  cuda-cuxxfilt      nvidia/label/cuda-11.8.0/linux-64::cuda-cuxxfilt-11.8.86-0 
  cuda-documentation nvidia/label/cuda-11.8.0/linux-64::cuda-documentation-11.8.86-0 
  cuda-driver-dev    nvidia/label/cuda-11.8.0/linux-64::cuda-driver-dev-11.8.89-0 
  cuda-gdb           nvidia/label/cuda-11.8.0/linux-64::cuda-gdb-11.8.86-0 
  cuda-libraries     nvidia/label/cuda-11.8.0/linux-64::cuda-libraries-11.8.0-0 
  cuda-libraries-dev nvidia/label/cuda-11.8.0/linux-64::cuda-libraries-dev-11.8.0-0 
  cuda-memcheck      nvidia/label/cuda-11.8.0/linux-64::cuda-memcheck-11.8.86-0 
  cuda-nsight        nvidia/label/cuda-11.8.0/linux-64::cuda-nsight-11.8.86-0 
  cuda-nsight-compu~ nvidia/label/cuda-11.8.0/linux-64::cuda-nsight-compute-11.8.0-0 
  cuda-nvcc          nvidia/label/cuda-11.8.0/linux-64::cuda-nvcc-11.8.89-0 
  cuda-nvdisasm      nvidia/label/cuda-11.8.0/linux-64::cuda-nvdisasm-11.8.86-0 
  cuda-nvml-dev      nvidia/label/cuda-11.8.0/linux-64::cuda-nvml-dev-11.8.86-0 
  cuda-nvprof        nvidia/label/cuda-11.8.0/linux-64::cuda-nvprof-11.8.87-0 
  cuda-nvprune       nvidia/label/cuda-11.8.0/linux-64::cuda-nvprune-11.8.86-0 
  cuda-nvrtc         nvidia/label/cuda-11.8.0/linux-64::cuda-nvrtc-11.8.89-0 
  cuda-nvrtc-dev     nvidia/label/cuda-11.8.0/linux-64::cuda-nvrtc-dev-11.8.89-0 
  cuda-nvtx          nvidia/label/cuda-11.8.0/linux-64::cuda-nvtx-11.8.86-0 
  cuda-nvvp          nvidia/label/cuda-11.8.0/linux-64::cuda-nvvp-11.8.87-0 
  cuda-profiler-api  nvidia/label/cuda-11.8.0/linux-64::cuda-profiler-api-11.8.86-0 
  cuda-sanitizer-api nvidia/label/cuda-11.8.0/linux-64::cuda-sanitizer-api-11.8.86-0 
  cuda-toolkit       nvidia/label/cuda-11.8.0/linux-64::cuda-toolkit-11.8.0-0 
  cuda-tools         nvidia/label/cuda-11.8.0/linux-64::cuda-tools-11.8.0-0 
  cuda-visual-tools  nvidia/label/cuda-11.8.0/linux-64::cuda-visual-tools-11.8.0-0 
  gds-tools          nvidia/label/cuda-11.8.0/linux-64::gds-tools-1.4.0.31-0 
  libcublas          nvidia/label/cuda-11.8.0/linux-64::libcublas-11.11.3.6-0 
  libcublas-dev      nvidia/label/cuda-11.8.0/linux-64::libcublas-dev-11.11.3.6-0 
  libcufft           nvidia/label/cuda-11.8.0/linux-64::libcufft-10.9.0.58-0 
  libcufft-dev       nvidia/label/cuda-11.8.0/linux-64::libcufft-dev-10.9.0.58-0 
  libcufile          nvidia/label/cuda-11.8.0/linux-64::libcufile-1.4.0.31-0 
  libcufile-dev      nvidia/label/cuda-11.8.0/linux-64::libcufile-dev-1.4.0.31-0 
  libcurand          nvidia/label/cuda-11.8.0/linux-64::libcurand-10.3.0.86-0 
  libcurand-dev      nvidia/label/cuda-11.8.0/linux-64::libcurand-dev-10.3.0.86-0 
  libcusolver        nvidia/label/cuda-11.8.0/linux-64::libcusolver-11.4.1.48-0 
  libcusolver-dev    nvidia/label/cuda-11.8.0/linux-64::libcusolver-dev-11.4.1.48-0 
  libcusparse        nvidia/label/cuda-11.8.0/linux-64::libcusparse-11.7.5.86-0 
  libcusparse-dev    nvidia/label/cuda-11.8.0/linux-64::libcusparse-dev-11.7.5.86-0 
  libnpp             nvidia/label/cuda-11.8.0/linux-64::libnpp-11.8.0.86-0 
  libnpp-dev         nvidia/label/cuda-11.8.0/linux-64::libnpp-dev-11.8.0.86-0 
  libnvjpeg          nvidia/label/cuda-11.8.0/linux-64::libnvjpeg-11.9.0.86-0 
  libnvjpeg-dev      nvidia/label/cuda-11.8.0/linux-64::libnvjpeg-dev-11.9.0.86-0 
  nsight-compute     nvidia/label/cuda-11.8.0/linux-64::nsight-compute-2022.3.0.22-0 



Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
[ble: elapsed 18.222s (CPU 88.2%)] conda install -y -c nvidia/label/cuda-11.8.0 cuda-toolkit

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:28  
 cat > "$CONDA_PREFIX/etc/conda/activate.d/splat_mover_env.sh" <<'EOF'
export CUDA_HOME="$CONDA_PREFIX"
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$CUDA_HOME/lib:${CUDA_HOME}/lib64:${LD_LIBRARY_PATH:-}"
export TORCH_CUDA_ARCH_LIST="8.9"
export TCNN_CUDA_ARCHITECTURES=89
EOF
conda deactivate
conda activate splat-mover-v3

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:29  
 echo $CUDA_HOME
which nvcc
nvcc --version
python - <<'PY'
import torch
print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())
PY
/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/bin/nvcc
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Sep_21_10:33:58_PDT_2022
Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0
2.1.2+cu118
11.8
True

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:29  
 uv pip install ninja
uv pip install --no-build-isolation \
  "git+ssh://git@github.com/NVlabs/tiny-cuda-nn.git#subdirectory=bindings/torch"
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 1 package in 702ms
Installed 1 package in 18ms
 + ninja==1.13.0
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 1 package in 1.16s
Installed 1 package in 18ms
 + tinycudann==2.0 (from git+ssh://git@github.com/NVlabs/tiny-cuda-nn.git@2e757bbe781db59c4980d389d7dccbf5edc09669#subdirectory=bindings/torch)

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:29  
 python - <<'PY'
import tinycudann as tcnn
print("tinycudann: OK")
PY
tinycudann: OK

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:29  
 uv pip install \
  "nerfstudio==1.1.0" \
  "numpy<2" \
  "open3d==0.18.0" \
  "scikit-learn==1.4.2" \
  "opencv-python-headless" \
  "roma" \
  "torchtyping" \
  "pytorch-msssim" \
  "torchmetrics" \
  "timm" \
  "ftfy" \
  "regex" \
  "tqdm" \
  "einops" \
  "gdown" \
  "matplotlib" \
  "pillow<10" \
  "transforms3d" \
  "trimesh" \
  "plotly" \
  "jaxtyping" \
  "pymeshlab"
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
  × No solution found when resolving dependencies:
  ╰─▶ Because nerfstudio==1.1.0 depends on pillow>=10.3.0 and you require nerfstudio==1.1.0, we can conclude that
      you require pillow>=10.3.0.
      And because you require pillow<10, we can conclude that your requirements are unsatisfiable.
[ble: exit 1]

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:30  
 uv pip install \
  "nerfstudio==1.1.0" \
  "numpy<2" \
  "open3d==0.18.0" \
  "scikit-learn==1.4.2" \
  "opencv-python-headless" \
  "roma" \
  "torchtyping" \
  "pytorch-msssim" \
  "torchmetrics" \
  "timm" \
  "ftfy" \
  "regex" \
  "tqdm" \
  "einops" \
  "gdown" \
  "matplotlib" \
  "transforms3d" \
  "trimesh" \
  "plotly" \
  "jaxtyping" \
  "pymeshlab"
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 244 packages in 2.87s
Prepared 4 packages in 29.41s
Installed 223 packages in 408ms
 + absl-py==2.4.0
 + addict==2.4.0
 + annotated-types==0.7.0
 + anyio==4.12.1
 + appdirs==1.4.4
 + argon2-cffi==25.1.0
 + argon2-cffi-bindings==25.1.0
 + arrow==1.4.0
 + asttokens==3.0.1
 + async-lru==2.3.0
 + attrs==26.1.0
 + av==17.0.0
 + awscli==1.44.64
 + babel==2.18.0
 + beautifulsoup4==4.14.3
 + bidict==0.23.1
 + bleach==6.3.0
 + blinker==1.9.0
 + botocore==1.42.74
 + cachetools==7.0.5
 + cffi==2.0.0
 + click==8.3.1
 + colorama==0.4.6
 + colorlog==6.10.1
 + comet-ml==3.57.3
 + comm==0.2.3
 + configargparse==1.7.5
 + configobj==5.0.9
 + contourpy==1.3.2
 + cryptography==46.0.5
 + cycler==0.12.1
 + dash==4.1.0
 + debugpy==1.8.20
 + decorator==5.2.1
 + defusedxml==0.7.1
 + descartes==1.1.0
 + dill==0.4.1
 + docstring-parser==0.17.0
 + docutils==0.19
 + dulwich==0.24.1
 + einops==0.8.2
 + embreex==2.17.7.post7
 + everett==3.1.0
 + exceptiongroup==1.3.1
 + executing==2.2.1
 + fastjsonschema==2.21.2
 + fire==0.7.1
 + flask==3.1.3
 + fonttools==4.62.1
 + fqdn==1.5.1
 + ftfy==6.3.1
 + gdown==5.2.1
 + gitdb==4.0.12
 + gitpython==3.1.46
 + grpcio==1.78.0
 + gsplat==1.5.3
 + h11==0.16.0
 + h5py==3.16.0
 + httpcore==1.0.9
 + httpx==0.28.1
 + imageio==2.37.3
 + importlib-metadata==9.0.0
 + ipykernel==7.2.0
 + ipython==8.38.0
 + ipywidgets==8.1.8
 + isoduration==20.11.0
 + itsdangerous==2.2.0
 + jaxtyping==0.3.7
 + jedi==0.19.2
 + jmespath==1.1.0
 + joblib==1.5.3
 + json5==0.13.0
 + jsonpointer==3.1.1
 + jsonschema==4.26.0
 + jsonschema-specifications==2025.9.1
 + jupyter-client==8.8.0
 + jupyter-core==5.9.1
 + jupyter-events==0.12.0
 + jupyter-lsp==2.3.0
 + jupyter-server==2.17.0
 + jupyter-server-terminals==0.5.4
 + jupyterlab==4.1.6
 + jupyterlab-pygments==0.3.0
 + jupyterlab-server==2.24.0
 + jupyterlab-widgets==3.0.16
 + kiwisolver==1.5.0
 + lark==1.3.1
 + lazy-loader==0.5
 + lightning-utilities==0.15.3
 + lxml==6.0.2
 + manifold3d==3.4.1
 + mapbox-earcut==2.0.0
 + markdown==3.10.2
 + markdown-it-py==4.0.0
 + matplotlib==3.10.8
 + matplotlib-inline==0.2.1
 + mdurl==0.1.2
 + mediapy==1.2.6
 + mistune==3.2.0
 + msgpack==1.1.2
 + msgpack-numpy==0.4.8
 + multiprocess==0.70.19
 + narwhals==2.18.0
 + nbclient==0.10.4
 + nbconvert==7.17.0
 + nbformat==5.10.4
 + nerfacc==0.5.2
 + nerfstudio==1.1.0
 + nest-asyncio==1.6.0
 + nodeenv==1.10.0
 + notebook-shim==0.2.4
 + nuscenes-devkit==1.2.0
 + open3d==0.18.0
 + opencv-python==4.8.0.76
 + opencv-python-headless==4.11.0.86
 + overrides==7.7.0
 + pandas==2.3.3
 + pandocfilters==1.5.1
 + parameterized==0.9.0
 + parso==0.8.6
 + pathos==0.3.5
 + pexpect==4.9.0
 + platformdirs==4.9.4
 + plotly==6.6.0
 + pox==0.3.7
 + ppft==1.7.8
 + prometheus-client==0.24.1
 + prompt-toolkit==3.0.52
 + protobuf==3.20.3
 + psutil==7.2.2
 + ptyprocess==0.7.0
 + pure-eval==0.2.3
 + pyasn1==0.6.3
 + pycocotools==2.0.11
 + pycollada==0.9.3
 + pycparser==3.0
 + pydantic==2.12.5
 + pydantic-core==2.41.5
 + pygments==2.19.2
 + pyliblzfse==0.4.1
 + pymeshlab==2025.7.post1
 + pyngrok==7.5.1
 + pyparsing==3.3.2
 + pyquaternion==0.9.9
 + pysocks==1.7.1
 + python-box==6.1.0
 + python-dateutil==2.9.0.post0
 + python-engineio==4.13.1
 + python-json-logger==4.0.0
 + python-socketio==5.16.1
 + pytorch-msssim==1.0.0
 + pytz==2026.1.post1
 + pyyaml==6.0.3
 + pyzmq==27.1.0
 + rawpy==0.26.1
 + referencing==0.37.0
 + regex==2026.2.28
 + requests-toolbelt==1.0.0
 + retrying==1.4.2
 + rfc3339-validator==0.1.4
 + rfc3986-validator==0.1.1
 + rfc3987-syntax==1.1.0
 + rich==14.3.3
 + roma==1.5.6
 + rpds-py==0.30.0
 + rsa==4.7.2
 + rtree==1.4.1
 + s3transfer==0.16.0
 + scikit-image==0.25.2
 + scikit-learn==1.4.2
 + scipy==1.15.3
 + semantic-version==2.10.0
 + send2trash==2.1.0
 + sentry-sdk==2.56.0
 + shapely==2.0.7
 + simple-websocket==1.1.0
 + simplejson==3.20.2
 + six==1.17.0
 + smmap==5.0.3
 + soupsieve==2.8.3
 + splines==0.3.0
 + stack-data==0.6.3
 + svg-path==7.0
 + tensorboard==2.20.0
 + tensorboard-data-server==0.7.2
 + termcolor==3.3.0
 + terminado==0.18.1
 + threadpoolctl==3.6.0
 + tifffile==2025.5.10
 + timm==0.6.7
 + tinycss2==1.4.0
 + tomli==2.4.0
 + torch-fidelity==0.4.0
 + torchmetrics==1.9.0
 + torchtyping==0.1.4
 + tornado==6.5.5
 + tqdm==4.67.3
 + traitlets==5.14.3
 + transforms3d==0.4.2
 + trimesh==4.11.4
 + typeguard==4.5.1
 + typing-inspection==0.4.2
 + tyro==1.0.10
 + tzdata==2025.3
 + uri-template==1.3.0
 + vhacdx==0.0.10
 + viser==0.1.27
 + wadler-lindig==0.1.7
 + wandb==0.25.0
 + wcwidth==0.6.0
 + webcolors==25.10.0
 + webencodings==0.5.1
 + websocket-client==1.9.0
 + websockets==16.0
 + werkzeug==3.1.7
 + widgetsnbextension==4.0.15
 + wrapt==2.1.2
 + wsproto==1.3.2
 + wurlitzer==3.1.1
 + xatlas==0.0.11
 + xxhash==3.6.0
 + yourdfpy==0.0.60
 + zipp==3.23.0

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:31  
 python - <<'PY'
import torch, numpy
print("torch:", torch.__version__)
print("torch cuda:", torch.version.cuda)
print("cuda available:", torch.cuda.is_available())
print("numpy:", numpy.__version__)
PY
torch: 2.1.2+cu118
torch cuda: 11.8
cuda available: True
numpy: 1.26.4

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:33  
 uv pip install "gsplat==1.5.3"
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Checked 1 package in 17ms

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:34  
 python - <<'PY'
import gsplat
print("gsplat:", gsplat.__version__)
from gsplat.rendering import rasterization
print("rendering: OK")
PY
gsplat: 1.5.3
rendering: OK


󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:34  
 ls
 assets                     INSTALL_LAB_SERVER.md   sagesplat            SPLAT_MOVER_code_reading.md         utils
 check_splat_mover_env.sh   pyproject.toml          sagesplat.egg-info   SPLAT_MOVER_method_explanation.md
 graspnet                   README.md               scripts             'tree 解析.txt'

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:35  
 uv pip install --no-deps -e .
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 1 package in 2ms
      Built sagesplat @ file:///share3/home/qiujinyu/Splat-MOVER
Prepared 1 package in 770ms
Installed 1 package in 1ms
 + sagesplat==0.1.1 (from file:///share3/home/qiujinyu/Splat-MOVER)

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:35  
 ns-train --help | grep -E 'segsplat|sagesplat'
Traceback (most recent call last):
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/bin/ns-train", line 4, in <module>
    from nerfstudio.scripts.train import entrypoint
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/site-packages/nerfstudio/scripts/train.py", line 62, in <module>
    from nerfstudio.configs.method_configs import AnnotatedBaseConfigUnion
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/site-packages/nerfstudio/configs/method_configs.py", line 50, in <module>
    from nerfstudio.engine.trainer import TrainerConfig
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/site-packages/nerfstudio/engine/trainer.py", line 46, in <module>
    from nerfstudio.viewer.viewer import Viewer as ViewerState
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/site-packages/nerfstudio/viewer/viewer.py", line 37, in <module>
    from nerfstudio.models.splatfacto import SplatfactoModel
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/site-packages/nerfstudio/models/splatfacto.py", line 28, in <module>
    from gsplat._torch_impl import quat_to_rotmat
ModuleNotFoundError: No module named 'gsplat._torch_impl'
[ble: exit 1][ble: elapsed 11.665s (CPU 254.7%)] ns-train --help | grep -E 'segsplat|sagesplat'

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:36  
 uv pip install "nerfstudio==1.1.2"
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 240 packages in 1.59s
Uninstalled 2 packages in 40ms
Installed 4 packages in 51ms
 + fpsample==1.0.2
 - gsplat==1.5.3
 + gsplat==1.0.0
 - nerfstudio==1.1.0
 + nerfstudio==1.1.2
 + pybind11==3.0.2

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:38  
 uv pip install "gsplat==1.3.0"
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 19 packages in 1.31s
Prepared 1 package in 5.24s
Uninstalled 1 package in 28ms
Installed 1 package in 52ms
 - gsplat==1.0.0
 + gsplat==1.3.0

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:39  
 ns-train --help | grep -E 'segsplat|sagesplat'
Traceback (most recent call last):
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/bin/ns-train", line 4, in <module>
    from nerfstudio.scripts.train import entrypoint
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/site-packages/nerfstudio/scripts/train.py", line 62, in <module>
    from nerfstudio.configs.method_configs import AnnotatedBaseConfigUnion
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/site-packages/nerfstudio/configs/method_configs.py", line 729, in <module>
    all_methods, all_descriptions = merge_methods(all_methods, all_descriptions, *discover_methods())
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/site-packages/nerfstudio/plugins/registry.py", line 43, in discover_methods
    spec = discovered_entry_points[name].load()
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/site-packages/importlib_metadata/__init__.py", line 226, in load
    module = import_module(self.module)
  File "/share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/share3/home/qiujinyu/Splat-MOVER/sagesplat/sagesplat_config.py", line 14, in <module>
    from sagesplat.data.sagesplat_datamanager import SageSplatDataManagerConfig
  File "/share3/home/qiujinyu/Splat-MOVER/sagesplat/data/sagesplat_datamanager.py", line 37, in <module>
    from sagesplat.data.utils.affordance_dataloader import AffordanceDataloader
  File "/share3/home/qiujinyu/Splat-MOVER/sagesplat/data/utils/affordance_dataloader.py", line 29, in <module>
    from lang_sam import LangSAM
ModuleNotFoundError: No module named 'lang_sam'
[ble: exit 1][ble: elapsed 8.866s (CPU 280.3%)] ns-train --help | grep -E 'segsplat|sagesplat'

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:40  
 python - <<'PY'
import torch, numpy, gsplat, nerfstudio
print("torch:", torch.__version__)
print("torch cuda:", torch.version.cuda)
print("cuda available:", torch.cuda.is_available())
print("numpy:", numpy.__version__)
print("gsplat:", gsplat.__version__)
print("nerfstudio:", getattr(nerfstudio, "__version__", "unknown"))
PY
torch: 2.1.2+cu118
torch cuda: 11.8
cuda available: True
numpy: 1.26.4
gsplat: 1.3.0
nerfstudio: unknown

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:41  
 uv pip install "numpy<2" "pillow>=9.4,<10"
env -u LD_LIBRARY_PATH uv pip install --no-build-isolation "git+ssh://git@github.com/IDEA-Research/GroundingDINO.git"
env -u LD_LIBRARY_PATH uv pip install "git+ssh://git@github.com/facebookresearch/segment-anything.git"
env -u LD_LIBRARY_PATH uv pip install --no-deps "git+ssh://git@github.com/luca-medeiros/lang-segment-anything.git@a1a9557"
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 2 packages in 650ms
Uninstalled 1 package in 4ms
Installed 1 package in 17ms
 - pillow==12.1.1
 + pillow==9.5.0
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 60 packages in 3.67s
Installed 12 packages in 63ms
 + annotated-doc==0.0.4
 + groundingdino==0.1.0 (from git+ssh://git@github.com/IDEA-Research/GroundingDINO.git@856dde20aee659246248e20734ef9ba5214f5e44)
 + hf-xet==1.4.2
 + huggingface-hub==1.7.2
 + pydeprecate==0.5.0
 + safetensors==0.7.0
 + shellingham==1.5.4
 + supervision==0.27.0.post2
 + tokenizers==0.22.2
 + transformers==5.3.0
 + typer==0.24.1
 + yapf==0.43.0
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 1 package in 43.14s
Installed 1 package in 17ms
 + segment-anything==1.0 (from git+ssh://git@github.com/facebookresearch/segment-anything.git@dca509fe793f601edb92606367a655c15ac00fdf)
Using Python 3.10.20 environment at: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3
Resolved 1 package in 1m 04s
Installed 1 package in 17ms
 + lang-sam==0.1.0 (from git+ssh://git@github.com/luca-medeiros/lang-segment-anything.git@a1a95572ba16b4661d8fb7b9388a998ce3391f95)

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:43  
 python - <<'PY'
from lang_sam import LangSAM
print("lang_sam: OK")
PY
Disabling PyTorch because PyTorch >= 2.4 is required but found 2.1.2+cu118
PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
lang_sam: OK
[ble: elapsed 8.033s (CPU 238.5%)] python - <<'PY'

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:43  
 python - <<'PY'
import torch, numpy, gsplat, nerfstudio
print("torch:", torch.__version__)
print("torch cuda:", torch.version.cuda)
print("cuda available:", torch.cuda.is_available())
print("numpy:", numpy.__version__)
print("gsplat:", gsplat.__version__)
print("nerfstudio:", getattr(nerfstudio, "__version__", "unknown"))
PY
torch: 2.1.2+cu118
torch cuda: 11.8
cuda available: True
numpy: 1.26.4
gsplat: 1.3.0
nerfstudio: unknown

󰕈 qiujinyu@server-03  …/Splat-MOVER   master !?   v3.10.20  🅒  splat-mover-v3   20:44  
 ns-train --help | grep -E 'segsplat|sagesplat'
Disabling PyTorch because PyTorch >= 2.4 is required but found 2.1.2+cu118
PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
usage: /share3/home/qiujinyu/miniconda3/envs/splat-mover-v3/bin/ns-train [-h] {depth-nerfacto,dnerf,generfacto,instant-ngp,instant-ngp-bounded,mipnerf,nerfacto,nerfacto-big,nerfacto-huge,neus,neus-facto,phototourism,sagesplat,semantic-nerfw,splatfacto,splatfacto-big,tensorf,vanilla-nerf,BioNeRF,igs2gs,in2n,in2n-small,in2n-tiny,kplanes,kplanes-dynamic,lerf,lerf-big,lerf-lite,nerfgs,nerfplayer-nerfacto,nerfplayer-ngp,nerfsh,pynerf,pynerf-occupancy-grid,pynerf-synthetic,seathru-nerf,seathru-nerf-lite,signerf,signerf_nerfacto,tetra-nerf,tetra-nerf-original,volinga,zipnerf}
│   • sagesplat   Config for SageSplat                                         │
[ble: elapsed 15.365s (CPU 189.7%)] ns-train --help | grep -E 'segsplat|sagesplat'
```

使用 的 时候可以暂时关闭警告

```bash
export TRANSFORMERS_VERBOSITY=error
export TRANSFORMERS_NO_ADVISORY_WARNINGS=1
```

```bash
ns-train sagesplat --help
```

