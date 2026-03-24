# Splat-MOVER 代码阅读与研究复现分析

本文以仓库中的实际代码实现为准，而不是以论文摘要或项目页表述为准。阅读顺序是 `README.md`、`pyproject.toml`、`sagesplat/sagesplat_config.py`、`sagesplat/sagesplat_pipeline.py`、`sagesplat/sagesplat.py`、`utils/nerf_utils.py`、`utils/scene_editing_utils.py`、`utils/render_utils.py`、`utils/grasp_utils.py`、`scripts/eval.py`、`scripts/eval_scene_editing.py`，并对 `scripts/eval_scene_editing_left.py`、`scripts/eval_scene_editing_right.py`、`sagesplat/data/utils/affordance_dataloader.py`、`sagesplat/vrb/*` 做了交叉核对。

先给出整体判断。仓库中没有直接命名为 ASK-Splat、SEE-Splat、Grasp-Splat 的目录、类或脚本，因此下面的映射是基于代码结构、真实调用关系、张量流和配置项推断得到的。最可能的对应关系是：ASK-Splat 对应 `sagesplat/*` 这一套训练与渲染代码，SEE-Splat 对应 `scripts/eval_scene_editing.py` 联合 `utils/scene_editing_utils.py`、`utils/render_utils.py` 的场景编辑流程，Grasp-Splat 对应 `scripts/eval.py` 与 `utils/grasp_utils.py` 联合 `graspnet/*` 的抓取生成与重排序流程。

### 代码定位总述

仓库的核心自定义部分只有两层。第一层是 `sagesplat` 包，它把高斯场景表示、CLIP 语义、affordance 监督、文本查询和 Nerfstudio 插件化训练组织在一起。第二层是 `utils` 与 `scripts`，前者把训练好的 `sagesplat` 模型包装成可导出点云、可做语义查询、可做场景编辑和可做抓取评估的工具，后者则把这些工具写成论文演示脚本。`graspnet` 与 `sagesplat/vrb` 基本是被集成的外部模块，前者提供抓取候选，后者提供 affordance 监督来源。

### ASK-Splat 代码定位

- 模块名称：ASK-Splat，对应 `sagesplat` 包。这是基于代码结构推断的映射。
- 对应目录：`sagesplat/`、`sagesplat/data/`、`sagesplat/data/utils/`、`sagesplat/encoders/`、`sagesplat/vrb/`。
- 核心文件：`sagesplat/sagesplat.py`、`sagesplat/sagesplat_config.py`、`sagesplat/sagesplat_pipeline.py`、`sagesplat/data/sagesplat_datamanager.py`、`sagesplat/data/utils/maskclip_dataloader.py`、`sagesplat/data/utils/affordance_dataloader.py`、`sagesplat/viewer_utils.py`。
- 核心类与函数：`SageSplatModel`、`SageSplatModel.populate_modules()`、`SageSplatModel.get_outputs()`、`SageSplatModel.get_semantic_outputs()`、`SageSplatModel.get_loss_dict()`、`SageSplatDataManager.next_train()`、`MaskCLIPDataloader.create()`、`AffordanceDataloader.create()`、`ViewerUtils.handle_language_queries()`。
- 训练入口：`README.md` 给出的 `ns-train sagesplat --data <scene>`，插件注册入口在 `pyproject.toml`，配置定义在 `sagesplat/sagesplat_config.py`。
- 推理入口：`utils/nerf_utils.py` 里的 `NeRF`、`NeRF.generate_point_cloud()`、`NeRF.get_semantic_point_cloud()`。
- 配置文件：仓库内真正定义方法配置的是 `sagesplat/sagesplat_config.py`，实验运行时的 `config.yml` 由 Nerfstudio 训练产出，不在仓库中提交。
- 被调用关系：`pyproject.toml` 注册方法配置，`sagesplat/sagesplat_config.py` 组装 `SageSplatPipeline`，`SageSplatPipeline` 再实例化 `SageSplatDataManager` 与 `SageSplatModel`；训练时 `SageSplatDataManager.next_train()` 产出 `clip` 与 `affordance` 监督，`SageSplatModel.get_loss_dict()` 消费这些监督；推理时 `NeRF.get_semantic_point_cloud()` 通过 `SageSplatModel.get_semantic_outputs()` 把高斯上的 latent CLIP 表示解码为文本相关性。

结论上，ASK-Splat 不是一个单独的脚本，而是整个 `sagesplat` 训练方法本身。证据链是：`pyproject.toml` 将 `sagesplat.sagesplat_config:sagesplat_method` 注册为 Nerfstudio 方法入口，`sagesplat/sagesplat_config.py` 用 `SageSplatPipelineConfig` 组合 `SageSplatDataManager`、`SageSplatModel` 与 `MaskCLIPNetworkConfig`，`sagesplat/data/sagesplat_datamanager.py` 在 `next_train()` 中显式写入 `data["clip"]` 与 `data["affordance"]`，`sagesplat/sagesplat.py` 在 `get_loss_dict()` 中对 `outputs["clip"]` 与 `outputs["affordance"]` 施加监督，因此可以判断这里实现了论文中“把语义与抓取 affordance 蒸馏进 GSplat 表示”的 ASK-Splat。

### SEE-Splat 代码定位

- 模块名称：SEE-Splat，最接近的实现是 `scripts/eval_scene_editing.py` 联合 `utils/scene_editing_utils.py`、`utils/render_utils.py`。这同样是基于代码结构推断的映射。
- 对应目录：`scripts/`、`utils/`。
- 核心文件：`scripts/eval_scene_editing.py`、`utils/scene_editing_utils.py`、`utils/render_utils.py`、`utils/nerf_utils.py`。
- 核心类与函数：`get_centroid()`、`get_interpolated_gaussians()`、`RenderInterpolated.main()`、`_render_trajectory_video()`、`NeRF.generate_point_cloud()`、`NeRF.get_semantic_point_cloud()`。
- 训练入口：未在仓库中找到 SEE-Splat 的独立训练代码。
- 推理入口：`scripts/eval_scene_editing.py` 是最完整的通用脚本，`scripts/eval_scene_editing_left.py` 与 `scripts/eval_scene_editing_right.py` 是后续为具体场景改写的分支。
- 配置文件：脚本依赖训练后生成的 Nerfstudio `config.yml`，但仓库里没有提交对应配置；`scripts/eval_scene_editing.py` 使用 `<config.yml>` 占位，`left`、`right` 脚本直接写死了外部绝对路径。
- 被调用关系：`scripts/eval_scene_editing.py` 先用 `NeRF.generate_point_cloud()` 取得环境高斯点云，再调用 `get_centroid()` 对目标与物体做 3D 语义定位，再把对象局部 mask 映射回全局 `comp_mask`，然后用 `get_interpolated_gaussians()` 生成高斯位姿序列，最后交给 `RenderInterpolated.main()`；后者进一步调用 `_render_trajectory_video()`，在每一帧中原地更新 `pipeline.model.means[gaussian_mask]` 与 `pipeline.model.quats[gaussian_mask]` 后再渲染。

这里最关键的判断是，SEE-Splat 在仓库里更像一个“基于当前高斯场景进行语义选取、刚体位姿编辑、逐帧重渲染”的推理流程，而不是一个单独可训练的子模块。证据链是：`scripts/eval_scene_editing.py` 调用 `get_centroid()` 取得 `similarity_mask`，再通过 `comp_mask[comp_mask == True] = torch.tensor(new_obj_mask)` 把局部对象点集映射回高斯索引，随后 `get_interpolated_gaussians()` 输出整个轨迹上的 `means` 与 `quats`，`utils/render_utils.py` 中的 `_render_trajectory_video()` 再把这些轨迹值写回 `pipeline.model.means` 与 `pipeline.model.quats` 并渲染视频，因此这里实现的是论文里“digital twin”更偏工程化的一版，即用可编辑高斯场景做阶段性状态可视化。

需要特别说明的是，README 把 SEE-Splat 说成“3D semantic masking and infilling”，但仓库里没有找到显式的 `inpaint`、`infill` 或几何补全模块。最接近的实现只有语义 masking、刚体平移与旋转、逐帧渲染。证据链是：全仓库检索 `inpaint`、`infill` 没有命中任何 SEE-Splat 相关实现，而 `scripts/eval_scene_editing.py` 与 `utils/render_utils.py` 的实际操作只有 mask、translation、quaternion interpolation 和 render，因此“显式 infilling”未在仓库中找到直接对应实现。

### Grasp-Splat 代码定位

- 模块名称：Grasp-Splat，对应 `scripts/eval.py`、`utils/grasp_utils.py` 联合 `graspnet/*` 的抓取流程。这是基于代码结构推断的映射。
- 对应目录：`scripts/`、`utils/`、`graspnet/graspnet_baseline/`、`graspnet/model_checkpoints/`。
- 核心文件：`scripts/eval.py`、`scripts/eval_scene_editing.py` 中的抓取部分、`utils/grasp_utils.py`。
- 核心类与函数：`demo()`、`get_net()`、`get_and_process_data()`、`get_grasps()`、`rank_grasps()`、`reorient_grasps()`、`save_grasps()`，以及第三方 `GraspNet`、`pred_decode()`、`ModelFreeCollisionDetector`。
- 训练入口：仓库内没有 Splat-MOVER 自己的 Grasp-Splat 联合训练脚本；只有第三方 `graspnet/graspnet_baseline/train.py` 与其 shell 脚本。
- 推理入口：`scripts/eval.py` 是最直接的 Grasp-Splat 评估脚本，`scripts/eval_scene_editing.py` 把抓取生成嵌入到了多阶段编辑流程里。
- 配置文件：`utils/grasp_utils.py` 中的 `Args`，以及脚本里硬编码的 `graspnet/model_checkpoints/checkpoint-rs.tar`。
- 被调用关系：`scripts/eval.py` 先利用 `NeRF.get_semantic_point_cloud()` 得到语义相似度并筛出对象点云，再调用 `demo()`；`demo()` 会通过 `get_net()` 加载 GraspNet 检查点、通过 `get_grasps()` 调用 `pred_decode()` 生成候选抓取；之后 `rank_grasps()` 用环境 KDTree 和高斯 affordance 对候选抓取重排序，`reorient_grasps()` 再基于支撑面法向做启发式姿态修正，最后 `save_grasps()` 输出位姿。

这里的关键判断是，Grasp-Splat 在代码里不是新的抓取网络，而是“语义筛选后的点云 + 预训练 GraspNet + 高斯 affordance 重排序”的组合。证据链是：`scripts/eval.py` 先根据 `semantic_info["similarity"]` 构造 `similarity_mask` 和 `cloud_masked`，`utils/grasp_utils.py` 的 `demo()` 只负责加载 `checkpoint-rs.tar` 并调用 GraspNet baseline，随后 `rank_grasps()` 通过最近邻查询 `env_affordance` 对候选抓取重新排序，因此这里实现的是论文所说 Grasp-Splat 的工程化组合版本，而不是端到端的新模型。

### ASK-Splat 的论文功能描述与代码映射

从代码看，ASK-Splat 主要负责三件事。第一，它维持标准 GSplat 场景几何与外观，也就是 `means`、`scales`、`quats`、`features_dc`、`features_rest`、`opacities` 这些高斯参数。第二，它给每个高斯增加了两个与论文表述直接对应的附加场：一个是 `clip_embeds`，维度固定为 3，是高斯上的语义 latent；另一个是 `affordance`，维度为 1，是高斯上的 affordance 标量。第三，它把文本查询放到推理时做，通过 `clip_decoder` 把 3 维 latent 解码回 CLIP 维度，再与正负文本嵌入做相似度计算，输出 `similarity`、`raw_similarity`、`semantic_affordance` 等图像或点云级语义结果。

它的输入在训练时不是单一 RGB 图像，而是三路数据并行进入。`SageSplatDataManager.next_train()` 从 Nerfstudio 数据集中取 `image`，再从 `MaskCLIPDataloader` 取 CLIP patch 特征写入 `data["clip"]`，再从 `AffordanceDataloader` 取 affordance 热图写入 `data["affordance"]`。其中 `AffordanceDataloader.create()` 并不是直接读取人工标注，而是先用 `LangSAM` 找固定词表里的候选框，再调用 `VRBModel.inference()` 预测 contact point 与 trajectory，最后把 contact heatmap 与 contact direction 拼成缓存张量。这说明论文里的“affordance feature”在仓库里的直接监督形式更接近二维 contact heatmap。

ASK-Splat 内部真正保存的中间表示有四类。第一类是 GSplat 自身的几何与颜色。第二类是每高斯 3 维 `clip_embeds` latent，它在 `get_outputs()` 中被光栅化为三通道 latent image，再在 `get_semantic_outputs()` 中解码。第三类是每高斯 1 维 `affordance`，同样在 `get_outputs()` 中被光栅化为 `outputs["affordance"]`。第四类是推理时的文本嵌入，即 `ViewerUtils.pos_embed` 与 `ViewerUtils.neg_embed`。当存在负样本文本时，`get_semantic_outputs()` 的实现不是直接取余弦相似度，而是对每个负词计算一组二分类 softmax，再取所有负词上正类概率的最小值，形式上近似为 $ \min_j \mathrm{softmax}([s^+, s^-_j])_0 $；这比简单的正样本点积更接近“保守的开放词汇检索”。

它的输出在训练时是 `rgb`、`depth`、`clip`、`affordance`，在推理时还会额外产生 `similarity`、`raw_similarity`、`similarity_GUI`、`composited_similarity`、`semantic_affordance`。在三维接口上，`NeRF.generate_point_cloud()` 直接导出 `env_attr["clip_embeds"]` 与 `env_attr["affordance"]`，`NeRF.get_semantic_point_cloud()` 则直接拿这些 per-Gaussian latent 做文本查询，因此 ASK-Splat 不是把语义只停留在渲染图像上，而是把它落在了高斯集合本身。

它与其他两个模块的衔接方式也很清楚。SEE-Splat 的 `get_centroid()` 先调用 `NeRF.get_semantic_point_cloud()` 得到点云上的 `similarity` 与 `raw_similarity`，然后在三维点云上做阈值、去噪和几何过滤。Grasp-Splat 则先用 `similarity` 抠出对象点云，再直接读取 `nerf.pipeline.model.affordance` 做候选抓取重排序。换句话说，ASK-Splat 是后两个模块的共同底座。

证据链可以写成两条。第一条是训练链：`sagesplat/sagesplat_pipeline.py` 实例化 `SageSplatDataManager`，`SageSplatDataManager.next_train()` 调用 `MaskCLIPDataloader` 和 `AffordanceDataloader` 生成 `clip`、`affordance`，`SageSplatModel.get_loss_dict()` 用它们监督 `outputs["clip"]` 与 `outputs["affordance"]`，因此判断这里实现了 ASK-Splat 的特征蒸馏。第二条是推理链：`utils/nerf_utils.py` 的 `generate_point_cloud()` 导出 `clip_embeds`、`affordance`，`get_semantic_point_cloud()` 再调用 `SageSplatModel.get_semantic_outputs()` 生成点云级相似度，因此判断 ASK-Splat 的语义与 affordance 都确实附着在高斯表示上而不是外部后处理。

还有两个代码层面的实现特征值得单独指出。其一，`SageSplatModel.split_gaussians()` 在高斯增密时会复制 `clip_embeds` 与 `affordance`，说明这两个场被当作一等高斯属性维护。其二，`get_loss_dict()` 实际是两阶段训练：前半段主要训练 RGB、autoencoder 与 affordance，且显式冻结 `clip_embeds`；后半段在 `scene_train_max_iter = 28000` 之后冻结几何和 `clip_encoder`、`clip_decoder`，只用 `clip_img_loss` 回归 per-Gaussian latent。这一点直接决定了复现实验时的训练时序。

### SEE-Splat 的论文功能描述与代码映射

从代码看，SEE-Splat 主要负责的是“从 ASK-Splat 中把要操作的对象与目标区域抠出来、估计物体放置平移与旋转、把对应高斯在时间轴上做刚体运动、再用编辑后的高斯序列渲染视频”。这一流程集中写在 `scripts/eval_scene_editing.py` 中，脚本先识别桌面、目标物和操作物，再通过一系列基于平面拟合与法向的启发式计算得到 `translation` 与 `rot_origin`，最后构建编辑轨迹并渲染。

它的输入不是原始图像，而是 ASK-Splat 输出的环境点云 `env_pcd` 与其属性 `env_attr`，再加上文本正负词、场景相机、启发式目标点。`get_centroid()` 是这里的关键函数。它内部先调用 `nerf.get_semantic_point_cloud()` 取得 `semantic_info`，再根据 `similarity` 构造 `similarity_mask`，随后做半径去噪、可选的球形过滤、凸包扩张、聚类筛选，最后返回 `centroid`、`z_bounds`、对象 mask 以及 `raw_similarity`。这说明 SEE-Splat 的“3D semantic masking”在代码里确实是沿着真实高斯点云完成的，而不是在二维图像上完成后再投回三维。

SEE-Splat 内部保存和传递的中间表示主要有 `similarity_mask`、`new_obj_mask`、`comp_mask`、`translation`、`obj_outputs`、逐帧的 `means` 与 `quats` 序列。这里最关键的变量是 `comp_mask`。`scripts/eval_scene_editing.py` 先在对象局部点云里得到 `new_obj_mask`，再通过 `comp_mask = env_pcd_mask.clone()` 和 `comp_mask[comp_mask == True] = torch.tensor(new_obj_mask)` 把这个局部 mask 抬升回整个高斯集合的索引空间。此后所有编辑都发生在 `comp_mask` 对应的高斯上，而不是在外部复制的网格或点云上。

它的输出有两类。第一类是视频与中间状态点云，`RenderInterpolated.main()` 会生成 `render_results/.../*.mp4`，脚本还会在每个 manipulation stage 之后导出新的点云和可选 mesh。第二类是更新后的高斯场景本身。`_render_trajectory_video()` 在每一帧渲染前都原地写入 `pipeline.model.means[gaussian_mask]` 和 `pipeline.model.quats[gaussian_mask]`，而脚本不会在阶段结束后把模型状态恢复到编辑前，因此后续保存出来的点云反映的是最新阶段的场景状态。

SEE-Splat 与 ASK-Splat 的衔接非常直接，因为对象定位完全依赖 ASK-Splat 的 `similarity` 与 `raw_similarity`。它与 Grasp-Splat 的衔接在代码里存在，但比论文叙述更弱。`scripts/eval_scene_editing.py` 会把对象的 `translation`、`comp_mask` 与抓取结果保存在同一条流水线里，说明场景编辑与抓取规划是在一个脚本中协同的；但抓取候选生成发生在真正的轨迹渲染之前，所以对于当前对象来说，抓取并不是直接在已编辑后的 twin 上生成的。更准确的说法是，SEE-Splat 提供了对象级高斯索引、目标位移和多阶段场景状态，而 Grasp-Splat 复用了这些中间结果。

证据链也有两条。第一条是对象选择链：`scripts/eval_scene_editing.py` 调用 `utils/scene_editing_utils.py` 的 `get_centroid()`，而 `get_centroid()` 又调用 `utils/nerf_utils.py` 的 `get_semantic_point_cloud()`，后者再调用 `SageSplatModel.get_semantic_outputs()`，因此判断 SEE-Splat 的输入语义来自 ASK-Splat 而非独立感知模块。第二条是编辑链：`scripts/eval_scene_editing.py` 生成 `comp_mask`、`translation` 与 `means/quats` 序列，再调用 `utils/render_utils.py` 的 `RenderInterpolated.main()`，`_render_trajectory_video()` 在每帧中直接改写 `pipeline.model.means/quats` 后调用 `pipeline.model.get_outputs_for_camera()` 渲染，因此判断 SEE-Splat 的“digital twin”实现方式是可编辑高斯场景的逐帧更新与重渲染。

不过，这一实现也存在需要谨慎理解的地方。脚本虽然在单个 `trial` 内只实例化一次 `nerf`，理论上允许多阶段状态累积，但 `env_pcd` 与 `env_attr` 是在对象循环外只生成一次的，后续 `get_centroid()` 仍继续使用这两个初始变量，而不是每个 stage 之后重新从更新后的模型中刷新。因此仓库代码已经实现了“场景可视化状态会累积更新”，但未完全证明“后续阶段的对象定位与语义查询也总是基于更新后的 twin”。这一点更适合在文末列为待验证问题。

### Grasp-Splat 的论文功能描述与代码映射

从代码看，Grasp-Splat 主要负责的是“先从 ASK-Splat 的语义相似度里筛出对象点云，再调用预训练 GraspNet 生成候选抓取，最后用 ASK-Splat 的 affordance 对抓取重排序，并用场景启发式修正姿态”。它不是一个新的抓取网络，真正的抓取 proposal 来自 `graspnet/graspnet_baseline/models/graspnet.py`，仓库自定义部分只在点云构造、affordance 融合和姿态后处理上。

它的输入在 `scripts/eval.py` 中非常清楚。脚本先从 `NeRF.generate_point_cloud()` 得到环境点云，再用 `NeRF.get_semantic_point_cloud()` 生成 `semantic_info`，再按阈值构造 `similarity_mask` 并截取 `cloud_masked`、`color_masked`。这一步说明 Grasp-Splat 的对象级输入来自 ASK-Splat 的开放词汇语义，而不是来自单独的实例分割器。在 `scripts/eval_scene_editing.py` 中，输入则是 `object_pcd_points_upd` 与 `object_pcd_colors_upd`，它们来自当前对象的 `comp_mask` 对应高斯集合。

它内部保存和预测的中间表示主要有 `GraspGroup` 候选集合、`env_tree`、`env_affordance`、`grasp_affordance`、`comp_score` 以及重定向后的 `reor_gp`。`utils/grasp_utils.py` 的实现特别值得注意。`rank_grasps()` 先收集 GraspNet 的 `gp.score`，但最后真正用于排序的 `comp_score = grasp_affordance.squeeze()`，而注释中把 `sigmoid(grasp_score) * grasp_affordance` 留成了备选实现。这说明仓库当前版本的“affordance-aware ranking”实际上只按 affordance 排序，并没有把 GraspNet 原始分数乘进去。

它的输出是保存到磁盘的抓取位姿，文件形式是 `*_graspnet.npy`、`*_w_affordance.npy`、`*_w_post_processing.npy`，以及在多阶段脚本里附带保存的 `translation.npy`。如果在 `scripts/eval_scene_editing.py` 中运行，Grasp-Splat 还会基于桌面法向调用 `reorient_grasps()`，让抓取坐标系与支撑面关系更合理。

它与 ASK-Splat 的衔接是最明确的，因为对象点云来自 ASK-Splat 的 `similarity`，affordance 重排序直接读取 `nerf.pipeline.model.affordance`。它与 SEE-Splat 的衔接在代码里主要表现为共用对象 mask、共用目标位移与共用同一条 task script，而不是一个独立的“从已编辑场景读出新抓取 proposal”的 API。换句话说，Grasp-Splat 在仓库里确实依赖 ASK-Splat，而对 SEE-Splat 的依赖更多体现在多阶段任务组织上。

证据链可以写成三步。首先，`scripts/eval.py` 调用 `NeRF.get_semantic_point_cloud()` 并基于 `semantic_info["similarity"]` 构造 `similarity_mask`，因此判断 Grasp-Splat 的对象输入来自 ASK-Splat。其次，`utils/grasp_utils.py` 的 `demo()` 调用 `get_net()` 载入 `checkpoint-rs.tar` 并调用 `GraspNet`、`pred_decode()`，因此判断候选抓取来自第三方 GraspNet baseline。最后，`rank_grasps()` 用 KDTree 查询 `env_affordance` 并重排抓取，因此判断仓库中的 Grasp-Splat 关键增量在于 affordance-aware reranking，而不是 proposal 本身。

### ASK-Splat 的调用链解释与伪代码

1. 入口在 Nerfstudio 训练命令。`README.md` 给出 `ns-train sagesplat --data ...`，`pyproject.toml` 把方法配置注册到 Nerfstudio，`sagesplat/sagesplat_config.py` 组装 `SageSplatPipeline`。
2. `SageSplatPipeline` 实例化 `SageSplatDataManager` 与 `SageSplatModel`。前者读取图像并构建 CLIP 与 affordance 缓存，后者建立带有 `clip_embeds` 与 `affordance` 的高斯参数集合。
3. 训练时，`SageSplatDataManager.next_train()` 取出 `image`、`clip`、`affordance`，`SageSplatModel.get_outputs()` 同时渲染 `rgb`、`clip`、`affordance`，`get_loss_dict()` 再按训练阶段计算 RGB、CLIP、affordance 损失。
4. 推理时，`NeRF.get_semantic_point_cloud()` 把点云上的 `clip_embeds` 送进 `SageSplatModel.get_semantic_outputs()`，该函数用 `ViewerUtils` 中的文本嵌入解码相似度并返回 `similarity` 与 `raw_similarity`，供下游模块消费。

下面这段伪代码主要对应 `pyproject.toml`、`sagesplat/sagesplat_config.py`、`sagesplat/sagesplat_pipeline.py`、`sagesplat/data/sagesplat_datamanager.py`、`sagesplat/sagesplat.py`、`sagesplat/viewer_utils.py`。

```python
# ASK-Splat 的实际代码骨架
method = register_method("sagesplat", config=SageSplatPipelineConfig(...))

pipeline = SageSplatPipeline(
    datamanager=SageSplatDataManager(image_encoder=MaskCLIPNetwork),
    model=SageSplatModel(...)
)

class SageSplatDataManager:
    clip_cache = MaskCLIPDataloader(images, encoder=MaskCLIPNetwork)
    affordance_cache = AffordanceDataloader(images, model=VRBModel, detector=LangSAM)

    def next_train(image_idx):
        batch["image"] = dataset[image_idx]["image"]
        batch["clip"] = clip_cache(image_idx)
        batch["affordance"] = affordance_cache(image_idx)[..., 0:1]
        return camera, batch

class SageSplatModel:
    gaussians = {
        "means", "scales", "quats", "features_dc", "features_rest", "opacities",
        "clip_embeds", "affordance"
    }
    clip_encoder = MLP(full_clip_dim -> 3)
    clip_decoder = MLP(3 -> full_clip_dim)

    def get_outputs(camera):
        rgb = rasterize(colors=gaussian_rgb)
        clip = rasterize(colors=clip_embeds)
        affordance = rasterize(colors=affordance)
        return {"rgb": rgb, "clip": clip, "affordance": affordance, ...}

    def get_loss_dict(outputs, batch):
        clip_latent = clip_encoder(batch["clip"])
        clip_recon = clip_decoder(clip_latent)
        loss = rgb_loss + clip_recon_loss + affordance_loss
        if late_stage:
            freeze_geometry_and_decoder()
            optimize_only_gaussian_clip_embeds()

    def get_semantic_outputs(clip_field):
        decoded_clip = clip_decoder(clip_field["clip"])
        text_embed = ViewerUtils.handle_language_queries(...)
        similarity = compare(decoded_clip, text_embed)
        return {"similarity": similarity, "raw_similarity": similarity_raw}
```

### SEE-Splat 的调用链解释与伪代码

1. 入口文件是 `scripts/eval_scene_editing.py`。脚本先通过 `NeRF(config_path)` 载入训练好的 `sagesplat` 模型，然后通过 `generate_point_cloud()` 得到环境点云与高斯属性。
2. 对每个目标与待操作物体，脚本调用 `get_centroid()`。这个函数内部先调用 `nerf.get_semantic_point_cloud()` 做文本查询，再对点云上的 `similarity` 做阈值、去噪、球形过滤、凸包扩张与聚类筛选，输出对象三维 mask。
3. 脚本把对象局部 mask 提升为全局 `comp_mask`，根据平面拟合与目标点计算 `translation`，再用 `get_interpolated_gaussians()` 生成物体对应高斯在整个时间轴上的 `means` 与 `quats`。
4. `RenderInterpolated.main()` 调用 `_render_trajectory_video()`。后者在每一帧中原地写入 `pipeline.model.means[gaussian_mask]` 与 `pipeline.model.quats[gaussian_mask]`，然后调用 `pipeline.model.get_outputs_for_camera()` 渲染，从而生成可视化 twin 视频。阶段结束后，脚本再从当前模型导出点云和 mesh，形成阶段性场景状态。

下面这段伪代码主要对应 `scripts/eval_scene_editing.py`、`utils/scene_editing_utils.py`、`utils/render_utils.py`、`utils/nerf_utils.py`。

```python
# SEE-Splat 的实际代码骨架
nerf = NeRF(config_path)
env_pcd, env_pcd_mask, env_attr = nerf.generate_point_cloud(use_bounding_box=True)

table_centroid = get_centroid(
    nerf=nerf, env_pcd=env_pcd, pcd_attr=env_attr, positives="table"
)
target_centroid = get_centroid(...)
object_centroid, _, scene_pcd, similarity_mask, other_attr = get_centroid(
    nerf=nerf, env_pcd=env_pcd, pcd_attr=env_attr, positives=obj_name
)

new_obj_mask = refine_with_plane_fit_and_outlier_removal(similarity_mask)
comp_mask = lift_local_mask_to_gaussian_mask(env_pcd_mask, new_obj_mask)
translation = target_place_point - object_base

rel_means_a = pipeline.model.means.clone()
rel_means_b = rel_means_a.clone()
rel_means_b[comp_mask] += translation

means_seq[:, comp_mask], quats_seq[:, comp_mask] = get_interpolated_gaussians(
    means_a=rel_means_a[comp_mask],
    means_b=rel_means_b[comp_mask],
    quats_a=pipeline.model.quats[comp_mask],
    quats_b=desired_quats[comp_mask],
    steps=num_pose_interp_steps,
)

RenderInterpolated.main(
    gaussian_means=means_seq,
    gaussian_quats=quats_seq,
    gaussian_mask=comp_mask,
    pipeline=nerf.pipeline,
)

# _render_trajectory_video 内部
for frame_idx in camera_path:
    pipeline.model.means[comp_mask] = means_seq[frame_idx]
    pipeline.model.quats[comp_mask] = quats_seq[frame_idx]
    outputs = pipeline.model.get_outputs_for_camera(camera)
    write_video_frame(outputs["rgb"])
```

这里还需要额外强调一个实现层面的判断。仓库中没有看到显式的几何 inpainting，而是通过“从当前高斯集合中挑出对象子集、对这一子集做位姿编辑、其余高斯保持不动”来构造 twin。因此它更接近可编辑场景图层，而不是显式补洞重建。

### Grasp-Splat 的调用链解释与伪代码

1. 入口文件是 `scripts/eval.py`，多阶段版本则嵌在 `scripts/eval_scene_editing.py` 中。脚本先从 `nerf.generate_point_cloud()` 与 `nerf.get_semantic_point_cloud()` 得到语义筛选后的对象点云。
2. `utils/grasp_utils.py` 的 `demo()` 会加载 `checkpoint-rs.tar`，调用 `GraspNet` 前向与 `pred_decode()`，生成 `GraspGroup` 候选抓取，并可选地做碰撞检测。
3. `rank_grasps()` 用环境点云 KDTree 对每个 grasp translation 查询最近的高斯 affordance，并据此重排序。`scripts/eval_scene_editing.py` 还会调用 `reorient_grasps()`，把抓取姿态与桌面法向对齐。
4. `save_grasps()` 将抓取位姿导出到 `npy` 文件；多阶段脚本还会额外保存对象 `translation.npy`，把抓取和编辑任务关联起来。

下面这段伪代码主要对应 `scripts/eval.py`、`scripts/eval_scene_editing.py`、`utils/grasp_utils.py`、`utils/nerf_utils.py`。

```python
# Grasp-Splat 的实际代码骨架
env_pcd, env_pcd_mask, env_attr = nerf.generate_point_cloud()
semantic_info = nerf.get_semantic_point_cloud(
    positives=query_text,
    negatives="object, things, stuff, texture",
    pcd_attr=env_attr,
)

similarity_mask = semantic_info["similarity"] > threshold
cloud_masked = env_pcd.points[similarity_mask]
color_masked = env_pcd.colors[similarity_mask]

def demo(cloud_masked, color_masked, cfgs):
    net = load_graspnet_checkpoint(cfgs.checkpoint_path)
    end_points = preprocess_point_cloud(cloud_masked, color_masked)
    cand_grasps = pred_decode(net(end_points))
    cand_grasps = collision_detection(cand_grasps)
    return cand_grasps

cand_grasps = demo(cloud_masked, color_masked, cfgs)
env_tree = KDTree(env_pcd.points)
env_affordance = pipeline.model.affordance[env_pcd_mask]
ranked_grasps = rank_grasps(cand_grasps, env_tree, env_affordance)
post_processed = reorient_grasps(ranked_grasps, table_normal)
save_grasps("result.npy", post_processed)
```

这里需要特别指出代码与论文描述的一个差异。`rank_grasps()` 虽然读入了 `gp.score`，但当前实现真正排序时只用了 `grasp_affordance`，并没有把 GraspNet 原始置信度乘进去。也就是说，代码里的“composite score”是一个简化版。

### 未确定点与待验证问题

- 仓库中没有直接使用 ASK-Splat、SEE-Splat、Grasp-Splat 这些命名，本文所有模块映射都属于基于代码结构、真实调用关系与数据流的推断，需要结合作者运行脚本再做最终确认。
- `pyproject.toml` 的插件键名是 `segsplat`，但 `README.md` 给出的训练命令是 `ns-train sagesplat`。两者是否都可用，或者只是哪一个在当前 Nerfstudio 版本下生效，需要实际运行确认。
- `AffordanceDataloader.create()` 会把 contact heatmap 与 contact direction 拼成多通道缓存，但 `SageSplatDataManager.next_train()` 实际只把 `affordance_outputs[..., 0:1]` 同时写给 `data["affordance"]` 与 `data["contact_direction"]`，而 `SageSplatModel.get_loss_dict()` 只消费 `batch["affordance"]`。因此 contact direction 在当前提交版本里看起来并未真正参与 ASK-Splat 训练。
- `sagesplat/data/utils/affordance_dataloader.py` 的 `run_inference()` 使用了固定物体词表 `knife`、`fruit`、`orange`、`chopping board`、`cutting board`。这说明 affordance 监督的生成流程在代码里仍带有强场景先验，并不完全等于开放词汇。
- README 把 SEE-Splat 描述成“3D semantic masking and infilling”，但仓库中未找到直接对应的 inpainting 或 infilling 实现。最接近的候选实现只有 `get_centroid()` 的 3D 语义 mask 与 `RenderInterpolated` 的高斯位姿编辑。
- `scripts/eval_scene_editing.py` 的确会在渲染阶段原地修改 `pipeline.model.means` 与 `pipeline.model.quats`，但 `env_pcd` 与 `env_attr` 只在对象循环外构造一次，后续 `get_centroid()` 仍继续使用初始点云和初始 `clip_embeds`。这意味着“可视化 twin 的状态会更新”已经实现，但“后续阶段的语义定位和规划是否始终基于更新后的 twin”仍需人工验证。
- `scripts/eval_scene_editing_left.py` 与 `scripts/eval_scene_editing_right.py` 是相似但并不等价的实现。两者包含大量针对具体场景的硬编码与注释掉的逻辑，尤其是 translation、`RenderInterpolated` 和 affordance-aware reranking 的部分被部分禁用，因此更像实验分支而不是论文主流程的最终实现。
- `scripts/eval_scene_editing.py` 中当前提交版本只处理 `objects` 列表中的后两个对象，因为循环开头有 `if idx < 2: continue`。这与论文中的泛化多阶段操作描述并不完全一致，更像一次具体 demo。
- Grasp-Splat 在 `scripts/eval_scene_editing.py` 里的当前对象抓取发生在 twin 渲染之前，因此“当前对象的 grasp 是否直接依赖 SEE-Splat 的更新后状态”并不充分；更强的依赖关系可能只会出现在后续 stage，如果作者在实际运行时额外刷新了 `env_pcd` 与 `env_attr`。
- 仓库中没有提交可直接复现实验的 Nerfstudio `config.yml` 与场景数据，`scripts/eval_scene_editing_left.py`、`scripts/eval_scene_editing_right.py` 还依赖外部绝对路径。因此要做完整复现，仍需要作者训练输出目录、数据集与检查点配套提供。
