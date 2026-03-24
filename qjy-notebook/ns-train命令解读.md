**You:**


╭─ options ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ -h, --help                                                                                                      │
│       show this help message and exit                                                                           │
│ --output-dir PATH                                                                                               │
│       relative or absolute output directory to save all checkpoints and logging (default: outputs)              │
│ --method-name {None}|STR                                                                                        │
│       Method name. Required to set in python or via cli (default: sagesplat)                                    │
│ --experiment-name {None}|STR                                                                                    │
│       Experiment name. If None, will automatically be set to dataset name (default: None)                       │
│ --project-name {None}|STR                                                                                       │
│       Project name. (default: nerfstudio-project)                                                               │
│ --timestamp STR                                                                                                 │
│       Experiment timestamp. (default: '{timestamp}')                                                            │
│ --vis {viewer,wandb,tensorboard,comet,viewer+wandb,viewer+tensorboard,viewer+comet,viewer_legacy}               │
│       Which visualizer to use. (default: viewer)                                                                │
│ --data {None}|PATH                                                                                              │
│       Alias for --pipeline.datamanager.data (default: None)                                                     │
│ --prompt {None}|STR                                                                                             │
│       Alias for --pipeline.model.prompt (default: None)                                                         │
│ --relative-model-dir PATH                                                                                       │
│       Relative path to save all checkpoints. (default: nerfstudio_models)                                       │
│ --load-scheduler {True,False}                                                                                   │
│       Whether to load the scheduler state_dict to resume training, if it exists. (default: True)                │
│ --steps-per-save INT                                                                                            │
│       Number of steps between saves. (default: 2000)                                                            │
│ --steps-per-eval-batch INT                                                                                      │
│       Number of steps between randomly sampled batches of rays. (default: 0)                                    │
│ --steps-per-eval-image INT                                                                                      │
│       Number of steps between single eval images. (default: 100)                                                │
│ --steps-per-eval-all-images INT                                                                                 │
│       Number of steps between eval all images. (default: 1000)                                                  │
│ --max-num-iterations INT                                                                                        │
│       Maximum number of iterations to run. (default: 56000)                                                     │
│ --mixed-precision {True,False}                                                                                  │
│       Whether or not to use mixed precision for training. (default: False)                                      │
│ --use-grad-scaler {True,False}                                                                                  │
│       Use gradient scaler even if the automatic mixed precision is disabled. (default: False)                   │
│ --save-only-latest-checkpoint {True,False}                                                                      │
│       Whether to only save the latest checkpoint or all checkpoints. (default: True)                            │
│ --load-dir {None}|PATH                                                                                          │
│       Optionally specify a pre-trained model directory to load from. (default: None)                            │
│ --load-step {None}|INT                                                                                          │
│       Optionally specify model step to load from; if none, will find most recent model in load_dir. (default:   │
│       None)                                                                                                     │
│ --load-config {None}|PATH                                                                                       │
│       Path to config YAML file. (default: None)                                                                 │
│ --load-checkpoint {None}|PATH                                                                                   │
│       Path to checkpoint file. (default: None)                                                                  │
│ --log-gradients {True,False}                                                                                    │
│       Optionally log gradients during training (default: False)                                                 │
│ --gradient-accumulation-steps [STR INT [STR INT ...]]                                                           │
│       Number of steps to accumulate gradients over. Contains a mapping of {param_group:num} (default: )         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ machine options ───────────────────────────────────────────────────────────────────────────────────────────────╮
│ Machine configuration                                                                                           │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --machine.seed INT                                                                                              │
│       random seed initialization (default: 42)                                                                  │
│ --machine.num-devices INT                                                                                       │
│       total number of devices (e.g., gpus) available for train/eval (default: 1)                                │
│ --machine.num-machines INT                                                                                      │
│       total number of distributed machines available (for DDP) (default: 1)                                     │
│ --machine.machine-rank INT                                                                                      │
│       current machine's rank (for DDP) (default: 0)                                                             │
│ --machine.dist-url STR                                                                                          │
│       distributed connection point (for DDP) (default: auto)                                                    │
│ --machine.device-type {cpu,cuda,mps}                                                                            │
│       device type to use for training (default: cuda)                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ logging options ───────────────────────────────────────────────────────────────────────────────────────────────╮
│ Logging configuration                                                                                           │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --logging.relative-log-dir PATH                                                                                 │
│       relative path to save all logged events (default: .)                                                      │
│ --logging.steps-per-log INT                                                                                     │
│       number of steps between logging stats (default: 10)                                                       │
│ --logging.max-buffer-size INT                                                                                   │
│       maximum history size to keep for computing running averages of stats.                                     │
│       e.g. if 20, averages will be computed over past 20 occurrences. (default: 20)                             │
│ --logging.profiler {none,basic,pytorch}                                                                         │
│       how to profile the code;                                                                                  │
│       "basic" - prints speed of all decorated functions at the end of a program.                                │
│       "pytorch" - same as basic, but it also traces few training steps. (default: basic)                        │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ logging.local-writer options ──────────────────────────────────────────────────────────────────────────────────╮
│ if provided, will print stats locally. if None, will disable printing                                           │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --logging.local-writer.enable {True,False}                                                                      │
│       if True enables local logging, else disables (default: True)                                              │
│ --logging.local-writer.stats-to-track [{ITER_TRAIN_TIME,TOTAL_TRAIN_TIME,ETA,TRAIN_RAYS_PER_SEC,                │
│ TEST_RAYS_PER_SEC,VIS_RAYS_PER_SEC,CURR_TEST_PSNR} [...]]                                                       │
│       specifies which stats will be logged/printed to terminal (default: ITER_TRAIN_TIME TRAIN_RAYS_PER_SEC     │
│       CURR_TEST_PSNR VIS_RAYS_PER_SEC TEST_RAYS_PER_SEC ETA)                                                    │
│ --logging.local-writer.max-log-size INT                                                                         │
│       maximum number of rows to print before wrapping. if 0, will print everything. (default: 10)               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ viewer options ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Viewer configuration                                                                                            │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --viewer.relative-log-filename STR                                                                              │
│       Filename to use for the log file. (default: viewer_log_filename.txt)                                      │
│ --viewer.websocket-port {None}|INT                                                                              │
│       The websocket port to connect to. If None, find an available port. (default: None)                        │
│ --viewer.websocket-port-default INT                                                                             │
│       The default websocket port to connect to if websocket_port is not specified (default: 7007)               │
│ --viewer.websocket-host STR                                                                                     │
│       The host address to bind the websocket server to. (default: 0.0.0.0)                                      │
│ --viewer.num-rays-per-chunk INT                                                                                 │
│       number of rays per chunk to render with viewer (default: 32768)                                           │
│ --viewer.max-num-display-images INT                                                                             │
│       Maximum number of training images to display in the viewer, to avoid lag. This does not change which      │
│       images are                                                                                                │
│       actually used in training/evaluation. If -1, display all. (default: 512)                                  │
│ --viewer.quit-on-train-completion {True,False}                                                                  │
│       Whether to kill the training job when it has completed. Note this will stop rendering in the viewer.      │
│       (default: False)                                                                                          │
│ --viewer.image-format {jpeg,png}                                                                                │
│       Image format viewer should use; jpeg is lossy compression, while png is lossless. (default: jpeg)         │
│ --viewer.jpeg-quality INT                                                                                       │
│       Quality tradeoff to use for jpeg compression. (default: 75)                                               │
│ --viewer.make-share-url {True,False}                                                                            │
│       Viewer beta feature: print a shareable URL. This flag is ignored in the legacy version of the viewer.     │
│       (default: False)                                                                                          │
│ --viewer.camera-frustum-scale FLOAT                                                                             │
│       Scale for the camera frustums in the viewer. (default: 0.1)                                               │
│ --viewer.default-composite-depth {True,False}                                                                   │
│       The default value for compositing depth. Turn off if you want to see the camera frustums without          │
│       occlusions. (default: True)                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ pipeline.datamanager options ──────────────────────────────────────────────────────────────────────────────────╮
│ specifies the datamanager config                                                                                │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --pipeline.datamanager.data {None}|PATH                                                                         │
│       Source of data, may not be used by all models. (default: None)                                            │
│ --pipeline.datamanager.masks-on-gpu {True,False}                                                                │
│       Process masks on GPU for speed at the expense of memory, if True. (default: False)                        │
│ --pipeline.datamanager.images-on-gpu {True,False}                                                               │
│       Process images on GPU for speed at the expense of memory, if True. (default: False)                       │
│ --pipeline.datamanager.camera-res-scale-factor FLOAT                                                            │
│       The scale factor for scaling spatial data such as images, mask, semantics                                 │
│       along with relevant information about camera intrinsics (default: 1.0)                                    │
│ --pipeline.datamanager.eval-num-images-to-sample-from INT                                                       │
│       Number of images to sample during eval iteration. (default: -1)                                           │
│ --pipeline.datamanager.eval-num-times-to-repeat-images INT                                                      │
│       When not evaluating on all images, number of iterations before picking                                    │
│       new images. If -1, never pick new images. (default: -1)                                                   │
│ --pipeline.datamanager.eval-image-indices {None}|{[INT [INT ...]]}                                              │
│       Specifies the image indices to use during eval; if None, uses all. (default: 0)                           │
│ --pipeline.datamanager.cache-images {cpu,gpu}                                                                   │
│       Whether to cache images in memory. If "cpu", caches on cpu. If "gpu", caches on device. (default: gpu)    │
│ --pipeline.datamanager.cache-images-type {uint8,float32}                                                        │
│       The image type returned from manager, caching images in uint8 saves memory (default: uint8)               │
│ --pipeline.datamanager.max-thread-workers {None}|INT                                                            │
│       The maximum number of threads to use for caching images. If None, uses all available threads. (default:   │
│       None)                                                                                                     │
│ --pipeline.datamanager.train-cameras-sampling-strategy {random,fps}                                             │
│       Specifies which sampling strategy is used to generate train cameras, 'random' means sampling              │
│       uniformly random without replacement, 'fps' means farthest point sampling which is helpful to reduce the  │
│       artifacts                                                                                                 │
│       due to oversampling subsets of cameras that are very close to each other. (default: random)               │
│ --pipeline.datamanager.train-cameras-sampling-seed INT                                                          │
│       Random seed for sampling train cameras. Fixing seed may help reduce variance of trained models across     │
│       different runs. (default: 42)                                                                             │
│ --pipeline.datamanager.fps-reset-every INT                                                                      │
│       The number of iterations before one resets fps sampler repeatly, which is essentially drawing             │
│       fps_reset_every                                                                                           │
│       samples from the pool of all training cameras without replacement before a new round of sampling starts.  │
│       (default: 100)                                                                                            │
│ --pipeline.datamanager.train-num-images-to-sample-from INT                                                      │
│       Number of images to sample during training iteration. (default: -1)                                       │
│ --pipeline.datamanager.train-num-times-to-repeat-images INT                                                     │
│       When not training on all images, number of iterations before picking new                                  │
│       images. If -1, never pick new images. (default: -1)                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ pipeline.model options ────────────────────────────────────────────────────────────────────────────────────────╮
│ specifies the model config                                                                                      │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --pipeline.model.enable-collider {True,False}                                                                   │
│       Whether to create a scene collider to filter rays. (default: True)                                        │
│ --pipeline.model.collider-params {None}|{[STR FLOAT [STR FLOAT ...]]}                                           │
│       parameters to instantiate scene collider with (default: near_plane 2.0 far_plane 6.0)                     │
│ --pipeline.model.eval-num-rays-per-chunk INT                                                                    │
│       specifies number of rays per chunk during eval (default: 4096)                                            │
│ --pipeline.model.prompt {None}|STR                                                                              │
│       A prompt to be used in text to NeRF models (default: None)                                                │
│ --pipeline.model.warmup-length INT                                                                              │
│       period of steps where refinement is turned off (default: 500)                                             │
│ --pipeline.model.refine-every INT                                                                               │
│       period of steps where gaussians are culled and densified (default: 100)                                   │
│ --pipeline.model.resolution-schedule INT                                                                        │
│       training starts at 1/d resolution, every n steps this is doubled (default: 3000)                          │
│ --pipeline.model.background-color {random,black,white}                                                          │
│       Whether to randomize the background color. (default: random)                                              │
│ --pipeline.model.num-downscales INT                                                                             │
│       at the beginning, resolution is 1/2^d, where d is this number (default: 2)                                │
│ --pipeline.model.cull-alpha-thresh FLOAT                                                                        │
│       threshold of opacity for culling gaussians. One can set it to a lower value (e.g. 0.005) for higher       │
│       quality. (default: 0.1)                                                                                   │
│ --pipeline.model.cull-scale-thresh FLOAT                                                                        │
│       threshold of scale for culling huge gaussians (default: 0.5)                                              │
│ --pipeline.model.continue-cull-post-densification {True,False}                                                  │
│       If True, continue to cull gaussians post refinement (default: True)                                       │
│ --pipeline.model.reset-alpha-every INT                                                                          │
│       Every this many refinement steps, reset the alpha (default: 30)                                           │
│ --pipeline.model.densify-grad-thresh FLOAT                                                                      │
│       threshold of positional gradient norm for densifying gaussians (default: 0.0002)                          │
│ --pipeline.model.densify-size-thresh FLOAT                                                                      │
│       below this size, gaussians are *duplicated*, otherwise split (default: 0.01)                              │
│ --pipeline.model.n-split-samples INT                                                                            │
│       number of samples to split gaussians into (default: 2)                                                    │
│ --pipeline.model.sh-degree-interval INT                                                                         │
│       every n intervals turn on another sh degree (default: 1000)                                               │
│ --pipeline.model.split-screen-size FLOAT                                                                        │
│       if a gaussian is more than this percent of screen space, split it (default: 0.05)                         │
│ --pipeline.model.stop-screen-size-at INT                                                                        │
│       stop culling/splitting at this step WRT screen size of gaussians (default: 4000)                          │
│ --pipeline.model.random-init {True,False}                                                                       │
│       whether to initialize the positions uniformly randomly (not SFM points) (default: False)                  │
│ --pipeline.model.num-random INT                                                                                 │
│       Number of gaussians to initialize if random init is used (default: 50000)                                 │
│ --pipeline.model.random-scale FLOAT                                                                             │
│       Size of the cube to initialize random gaussians within (default: 10.0)                                    │
│ --pipeline.model.ssim-lambda FLOAT                                                                              │
│       weight of ssim loss (default: 0.2)                                                                        │
│ --pipeline.model.stop-split-at INT                                                                              │
│       stop splitting at this step (default: 15000)                                                              │
│ --pipeline.model.sh-degree INT                                                                                  │
│       maximum degree of spherical harmonics to use (default: 3)                                                 │
│ --pipeline.model.use-scale-regularization {True,False}                                                          │
│       If enabled, a scale regularization introduced in PhysGauss (https://xpandora.github.io/PhysGaussian/) is  │
│       used for reducing huge spikey gaussians. (default: False)                                                 │
│ --pipeline.model.max-gauss-ratio FLOAT                                                                          │
│       threshold of ratio of gaussian max to min scale before applying regularization                            │
│       loss from the PhysGaussian paper (default: 10.0)                                                          │
│ --pipeline.model.output-depth-during-training {True,False}                                                      │
│       If True, output depth during training. Otherwise, only output depth during evaluation. (default: True)    │
│ --pipeline.model.rasterize-mode {classic,antialiased}                                                           │
│       Classic mode of rendering will use the EWA volume splatting with a [0.3, 0.3] screen space blurring       │
│       kernel. This                                                                                              │
│       approach is however not suitable to render tiny gaussians at higher or lower resolution than the          │
│       captured, which                                                                                           │
│       results "aliasing-like" artifacts. The antialiased mode overcomes this limitation by calculating          │
│       compensation factors                                                                                      │
│       and apply them to the opacities of gaussians to preserve the total integrated density of splats.          │
│                                                                                                                 │
│                                                                                                                 │
│       However, PLY exported with antialiased rasterize mode is not compatible with classic mode. Thus many web  │
│       viewers that                                                                                              │
│       were implemented for classic mode can not render antialiased mode PLY properly without modifications.     │
│       (default: classic)                                                                                        │
│ --pipeline.model.cull-screen-size FLOAT                                                                         │
│       if a gaussian is more than this percent of screen space, cull it (default: 0.15)                          │
│ --pipeline.model.output-semantics-during-training {True,False}                                                  │
│       If True, output semantic-scene information during training. Otherwise, only output semantic-scene         │
│       information during evaluation. (default: False)                                                           │
│ --pipeline.model.clip-img-loss-weight FLOAT                                                                     │
│       weight for the CLIP-related term in the loss function. (default: 0.1)                                     │
│ --pipeline.model.clip-network-cosine-sim-loss-weight FLOAT                                                      │
│       cosine-similarity weight for the CLIP-related term in the loss function. (default: 9.0)                   │
│ --pipeline.model.clip-network-loss-weight FLOAT                                                                 │
│       weight for the CLIP-related term in the loss function. (default: 5.0)                                     │
│ --pipeline.model.affordance-loss-weight FLOAT                                                                   │
│       weight for the affordance-related term in the loss function. (default: 0.1)                               │
│ --pipeline.model.use-depth-loss {True,False}                                                                    │
│       Depth supervision configuration (default: False)                                                          │
│ --pipeline.model.depth-loss-type STR                                                                            │
│       Depth supervision configuration (default: EdgeAwareLogL1)                                                 │
│ --pipeline.model.depth-lambda FLOAT                                                                             │
│       Depth supervision configuration (default: 0.1)                                                            │
│ --pipeline.model.use-depth-smooth-loss {True,False}                                                             │
│       Depth supervision configuration (default: False)                                                          │
│ --pipeline.model.smooth-loss-type STR                                                                           │
│       one of ["TV", "EdgeAwareTV"] (default: EdgeAwareTV)                                                       │
│ --pipeline.model.smooth-loss-lambda FLOAT                                                                       │
│       (default: 0.05)                                                                                           │
│ --pipeline.model.hidden-dim INT                                                                                 │
│       MLP head (default: 128)                                                                                   │
│ --pipeline.model.num-layers INT                                                                                 │
│       MLP head (default: 5)                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ pipeline.model.loss-coefficients options ──────────────────────────────────────────────────────────────────────╮
│ parameters to instantiate density field with                                                                    │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --pipeline.model.loss-coefficients.rgb-loss-coarse FLOAT                                                        │
│       (default: 1.0)                                                                                            │
│ --pipeline.model.loss-coefficients.rgb-loss-fine FLOAT                                                          │
│       (default: 1.0)                                                                                            │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ pipeline.model.camera-optimizer options ───────────────────────────────────────────────────────────────────────╮
│ Config of the camera optimizer to use                                                                           │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --pipeline.model.camera-optimizer.mode {off,SO3xR3,SE3}                                                         │
│       Pose optimization strategy to use. If enabled, we recommend SO3xR3. (default: off)                        │
│ --pipeline.model.camera-optimizer.trans-l2-penalty FLOAT                                                        │
│       L2 penalty on translation parameters. (default: 0.01)                                                     │
│ --pipeline.model.camera-optimizer.rot-l2-penalty FLOAT                                                          │
│       L2 penalty on rotation parameters. (default: 0.001)                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ pipeline.network options ──────────────────────────────────────────────────────────────────────────────────────╮
│ specifies the vision-language network config                                                                    │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --pipeline.network.clip-model-type STR                                                                          │
│       (default: RN50x64)                                                                                        │
│ --pipeline.network.clip-n-dims INT                                                                              │
│       (default: 512)                                                                                            │
│ --pipeline.network.skip-center-crop {True,False}                                                                │
│       negatives: Tuple[str] = ("object", "things", "stuff", "texture") (default: True)                          │
│ --pipeline.network.batch-size INT                                                                               │
│       negatives: Tuple[str] = ("object", "things", "stuff", "texture") (default: 1)                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.means.optimizer options ────────────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with Adam                                                                                │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.means.optimizer.lr FLOAT                                                                           │
│       The learning rate to use. (default: 0.00016)                                                              │
│ --optimizers.means.optimizer.eps FLOAT                                                                          │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.means.optimizer.max-norm {None}|FLOAT                                                              │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.means.optimizer.weight-decay FLOAT                                                                 │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.means.scheduler options ────────────────────────────────────────────────────────────────────────────╮
│ Config for exponential decay scheduler with warmup                                                              │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.means.scheduler.lr-pre-warmup FLOAT                                                                │
│       Learning rate before warmup. (default: 1e-08)                                                             │
│ --optimizers.means.scheduler.lr-final {None}|FLOAT                                                              │
│       Final learning rate. If not provided, it will be set to the optimizers learning rate. (default: 1.6e-06)  │
│ --optimizers.means.scheduler.warmup-steps INT                                                                   │
│       Number of warmup steps. (default: 0)                                                                      │
│ --optimizers.means.scheduler.max-steps INT                                                                      │
│       The maximum number of steps. (default: 30000)                                                             │
│ --optimizers.means.scheduler.ramp {linear,cosine}                                                               │
│       The ramp function to use during the warmup. (default: cosine)                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.features-dc options ────────────────────────────────────────────────────────────────────────────────╮
│ --optimizers.features-dc.scheduler {None}                                                                       │
│       (default: None)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.features-dc.optimizer options ──────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with Adam                                                                                │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.features-dc.optimizer.lr FLOAT                                                                     │
│       The learning rate to use. (default: 0.0025)                                                               │
│ --optimizers.features-dc.optimizer.eps FLOAT                                                                    │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.features-dc.optimizer.max-norm {None}|FLOAT                                                        │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.features-dc.optimizer.weight-decay FLOAT                                                           │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.features-rest options ──────────────────────────────────────────────────────────────────────────────╮
│ --optimizers.features-rest.scheduler {None}                                                                     │
│       (default: None)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.features-rest.optimizer options ────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with Adam                                                                                │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.features-rest.optimizer.lr FLOAT                                                                   │
│       The learning rate to use. (default: 0.000125)                                                             │
│ --optimizers.features-rest.optimizer.eps FLOAT                                                                  │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.features-rest.optimizer.max-norm {None}|FLOAT                                                      │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.features-rest.optimizer.weight-decay FLOAT                                                         │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.opacities options ──────────────────────────────────────────────────────────────────────────────────╮
│ --optimizers.opacities.scheduler {None}                                                                         │
│       (default: None)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.opacities.optimizer options ────────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with Adam                                                                                │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.opacities.optimizer.lr FLOAT                                                                       │
│       The learning rate to use. (default: 0.05)                                                                 │
│ --optimizers.opacities.optimizer.eps FLOAT                                                                      │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.opacities.optimizer.max-norm {None}|FLOAT                                                          │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.opacities.optimizer.weight-decay FLOAT                                                             │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.scales options ─────────────────────────────────────────────────────────────────────────────────────╮
│ --optimizers.scales.scheduler {None}                                                                            │
│       (default: None)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.scales.optimizer options ───────────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with Adam                                                                                │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.scales.optimizer.lr FLOAT                                                                          │
│       The learning rate to use. (default: 0.005)                                                                │
│ --optimizers.scales.optimizer.eps FLOAT                                                                         │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.scales.optimizer.max-norm {None}|FLOAT                                                             │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.scales.optimizer.weight-decay FLOAT                                                                │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.quats options ──────────────────────────────────────────────────────────────────────────────────────╮
│ --optimizers.quats.scheduler {None}                                                                             │
│       (default: None)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.quats.optimizer options ────────────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with Adam                                                                                │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.quats.optimizer.lr FLOAT                                                                           │
│       The learning rate to use. (default: 0.001)                                                                │
│ --optimizers.quats.optimizer.eps FLOAT                                                                          │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.quats.optimizer.max-norm {None}|FLOAT                                                              │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.quats.optimizer.weight-decay FLOAT                                                                 │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.camera-opt.optimizer options ───────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with Adam                                                                                │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.camera-opt.optimizer.lr FLOAT                                                                      │
│       The learning rate to use. (default: 0.0001)                                                               │
│ --optimizers.camera-opt.optimizer.eps FLOAT                                                                     │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.camera-opt.optimizer.max-norm {None}|FLOAT                                                         │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.camera-opt.optimizer.weight-decay FLOAT                                                            │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.camera-opt.scheduler options ───────────────────────────────────────────────────────────────────────╮
│ Config for exponential decay scheduler with warmup                                                              │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.camera-opt.scheduler.lr-pre-warmup FLOAT                                                           │
│       Learning rate before warmup. (default: 0)                                                                 │
│ --optimizers.camera-opt.scheduler.lr-final {None}|FLOAT                                                         │
│       Final learning rate. If not provided, it will be set to the optimizers learning rate. (default: 5e-07)    │
│ --optimizers.camera-opt.scheduler.warmup-steps INT                                                              │
│       Number of warmup steps. (default: 1000)                                                                   │
│ --optimizers.camera-opt.scheduler.max-steps INT                                                                 │
│       The maximum number of steps. (default: 30000)                                                             │
│ --optimizers.camera-opt.scheduler.ramp {linear,cosine}                                                          │
│       The ramp function to use during the warmup. (default: cosine)                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.clip-embeds options ────────────────────────────────────────────────────────────────────────────────╮
│ --optimizers.clip-embeds.scheduler {None}                                                                       │
│       (default: None)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.clip-embeds.optimizer options ──────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with RAdam                                                                               │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.clip-embeds.optimizer.lr FLOAT                                                                     │
│       The learning rate to use. (default: 0.01)                                                                 │
│ --optimizers.clip-embeds.optimizer.eps FLOAT                                                                    │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.clip-embeds.optimizer.max-norm {None}|FLOAT                                                        │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.clip-embeds.optimizer.weight-decay FLOAT                                                           │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.clip-encoder.optimizer options ─────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with RAdam                                                                               │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.clip-encoder.optimizer.lr FLOAT                                                                    │
│       The learning rate to use. (default: 0.005)                                                                │
│ --optimizers.clip-encoder.optimizer.eps FLOAT                                                                   │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.clip-encoder.optimizer.max-norm {None}|FLOAT                                                       │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.clip-encoder.optimizer.weight-decay FLOAT                                                          │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.clip-encoder.scheduler options ─────────────────────────────────────────────────────────────────────╮
│ Config for exponential decay scheduler with warmup                                                              │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.clip-encoder.scheduler.lr-pre-warmup FLOAT                                                         │
│       Learning rate before warmup. (default: 1e-08)                                                             │
│ --optimizers.clip-encoder.scheduler.lr-final {None}|FLOAT                                                       │
│       Final learning rate. If not provided, it will be set to the optimizers learning rate. (default: 1e-06)    │
│ --optimizers.clip-encoder.scheduler.warmup-steps INT                                                            │
│       Number of warmup steps. (default: 0)                                                                      │
│ --optimizers.clip-encoder.scheduler.max-steps INT                                                               │
│       The maximum number of steps. (default: 30000)                                                             │
│ --optimizers.clip-encoder.scheduler.ramp {linear,cosine}                                                        │
│       The ramp function to use during the warmup. (default: cosine)                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.clip-decoder.optimizer options ─────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with RAdam                                                                               │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.clip-decoder.optimizer.lr FLOAT                                                                    │
│       The learning rate to use. (default: 0.005)                                                                │
│ --optimizers.clip-decoder.optimizer.eps FLOAT                                                                   │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.clip-decoder.optimizer.max-norm {None}|FLOAT                                                       │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.clip-decoder.optimizer.weight-decay FLOAT                                                          │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.clip-decoder.scheduler options ─────────────────────────────────────────────────────────────────────╮
│ Config for exponential decay scheduler with warmup                                                              │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.clip-decoder.scheduler.lr-pre-warmup FLOAT                                                         │
│       Learning rate before warmup. (default: 1e-08)                                                             │
│ --optimizers.clip-decoder.scheduler.lr-final {None}|FLOAT                                                       │
│       Final learning rate. If not provided, it will be set to the optimizers learning rate. (default: 1e-06)    │
│ --optimizers.clip-decoder.scheduler.warmup-steps INT                                                            │
│       Number of warmup steps. (default: 0)                                                                      │
│ --optimizers.clip-decoder.scheduler.max-steps INT                                                               │
│       The maximum number of steps. (default: 30000)                                                             │
│ --optimizers.clip-decoder.scheduler.ramp {linear,cosine}                                                        │
│       The ramp function to use during the warmup. (default: cosine)                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.affordance options ─────────────────────────────────────────────────────────────────────────────────╮
│ --optimizers.affordance.scheduler {None}                                                                        │
│       (default: None)                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ optimizers.affordance.optimizer options ───────────────────────────────────────────────────────────────────────╮
│ Basic optimizer config with Adam                                                                                │
│ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│ --optimizers.affordance.optimizer.lr FLOAT                                                                      │
│       The learning rate to use. (default: 0.0005)                                                               │
│ --optimizers.affordance.optimizer.eps FLOAT                                                                     │
│       The epsilon value to use. (default: 1e-15)                                                                │
│ --optimizers.affordance.optimizer.max-norm {None}|FLOAT                                                         │
│       The max norm to use for gradient clipping. (default: None)                                                │
│ --optimizers.affordance.optimizer.weight-decay FLOAT                                                            │
│       The weight decay to use. (default: 0)                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ subcommands ───────────────────────────────────────────────────────────────────────────────────────────────────╮
│ (default: nerfstudio-data)                                                                                      │
│   • nerfstudio-data                                                                                             │
│   • minimal-parser                                                                                              │
│   • arkit-data                                                                                                  │
│   • blender-data                                                                                                │
│   • instant-ngp-data                                                                                            │
│   • nuscenes-data                                                                                               │
│   • dnerf-data                                                                                                  │
│   • phototourism-data                                                                                           │
│   • dycheck-data                                                                                                │
│   • scannet-data                                                                                                │
│   • sdfstudio-data                                                                                              │
│   • nerfosr-data                                                                                                │
│   • sitcoms3d-data                                                                                              │
│   • scannetpp-data                                                                                              │
│   • colmap                                                                                                      │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
[ble: elapsed 15.217s (CPU 209.9%)] ns-train sagesplat --help

详细解读上面的 help 手册，用表格的样式给出，使用中文

* * *

**ChatGPT:**

下面按模块对这份 `ns-train sagesplat --help` 做系统解读。你贴出的内容本质上是：

`ns-train sagesplat [全局参数] [数据子命令] [子命令参数]`

也就是用 `ns-train` 启动 `sagesplat` 方法训练，并通过一大批参数控制实验命名、日志、可视化、数据读入、模型结构、损失、优化器和调度器等。

我先给你一个整体认识，再逐块拆解。

---

## 一、命令整体结构

| 部分 | 作用 | 说明 |
| --- | --- | --- |
| `ns-train` | Nerfstudio 的训练入口 | 用来启动训练任务 |
| `sagesplat` | 训练方法名 | 指定当前使用的 method，是一个基于 Gaussian Splatting / 视觉语言扩展的配置 |
| 全局参数 | 控制实验、日志、设备、训练流程 | 例如输出目录、最大迭代数、混合精度 |
| 数据子命令 | 指定数据类型与解析方式 | 如 `nerfstudio-data`、`colmap`、`blender-data` 等 |
| 分层参数名 | 对应配置树 | 如 `pipeline.model.xxx`、`optimizers.xxx.xxx` 表示配置对象的层级 |

---

## 二、最重要的理解方式

这份 help 不是“平铺参数列表”，而是“配置树展开”。可以理解成类似下面的层级：

| 层级前缀 | 含义 |
| --- | --- |
| 顶层无前缀 | 实验全局设置 |
| `machine.*` | 机器与分布式训练设置 |
| `logging.*` | 日志设置 |
| `viewer.*` | 可视化 viewer 设置 |
| `pipeline.datamanager.*` | 数据加载与采样策略 |
| `pipeline.model.*` | 模型本体参数 |
| `pipeline.network.*` | 视觉语言网络参数 |
| `optimizers.*` | 不同参数组的优化器配置 |
| `optimizers.*.scheduler.*` | 对应参数组的学习率调度器 |

---

## 三、顶层 options 详解

### 1）实验与输出管理

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--output-dir PATH` | 输出根目录 | `outputs` | 所有 checkpoint、日志、配置等都会存在这里 |
| `--method-name {None}|STR` | 方法名 | `sagesplat` | 一般不用改，除非你在代码里动态指定 |
| `--experiment-name {None}|STR` | 实验名 | `None` | 不填时通常自动用数据集名；建议手动设，便于管理多个实验 |
| `--project-name {None}|STR` | 项目名 | `nerfstudio-project` | 常用于日志平台分组，如 wandb/comet |
| `--timestamp STR` | 时间戳 | `'{timestamp}'` | 用于区分同一实验不同运行 |
| `--relative-model-dir PATH` | checkpoint 子目录 | `nerfstudio_models` | 相对 `output-dir/experiment/timestamp` 的模型保存目录 |

### 2）可视化与输入快捷参数

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--vis {...}` | 可视化方式 | `viewer` | 可选 `viewer`、`wandb`、`tensorboard`、`comet` 或组合 |
| `--data PATH` | 数据路径快捷别名 | `None` | 等价于 `--pipeline.datamanager.data` |
| `--prompt STR` | 文本提示快捷别名 | `None` | 等价于 `--pipeline.model.prompt`，用于 text-to-NeRF 或视觉语言相关任务 |

### 3）断点恢复与保存策略

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--load-scheduler {True,False}` | 恢复时是否加载 scheduler 状态 | `True` | 恢复训练时通常应该保持 True，否则学习率曲线会断裂 |
| `--steps-per-save INT` | 每多少步保存一次 | `2000` | 训练较长时很关键 |
| `--save-only-latest-checkpoint {True,False}` | 是否只保留最新 checkpoint | `True` | 节省磁盘，但无法回滚到更早 step |
| `--load-dir PATH` | 从某个模型目录恢复 | `None` | 指定已有实验目录 |
| `--load-step INT` | 恢复指定 step | `None` | 不填通常自动找最近 checkpoint |
| `--load-config PATH` | 加载某个 config YAML | `None` | 常用于复现实验 |
| `--load-checkpoint PATH` | 直接加载 checkpoint 文件 | `None` | 比 `load-dir` 更直接 |

### 4）评估与训练流程频率

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--steps-per-eval-batch INT` | 每多少步做一次随机 ray eval | `0` | 0 表示关闭 |
| `--steps-per-eval-image INT` | 每多少步评估单张图像 | `100` | 用于快速监控视觉效果 |
| `--steps-per-eval-all-images INT` | 每多少步评估全部图像 | `1000` | 更全面，但更耗时 |
| `--max-num-iterations INT` | 最大训练步数 | `56000` | 训练总长度的核心参数 |
| `--gradient-accumulation-steps [...]` | 梯度累积设置 | 空 | 用于显存不足时模拟更大 batch |

### 5）数值计算与调试

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--mixed-precision {True,False}` | 是否使用混合精度 | `False` | 能省显存、提速，但有时影响稳定性 |
| `--use-grad-scaler {True,False}` | 即使不启用 AMP 也用梯度缩放 | `False` | 比较少见，通常配合数值稳定性实验 |
| `--log-gradients {True,False}` | 是否记录梯度 | `False` | 调试训练异常时有用，但会更慢 |

---

## 四、machine options：机器与分布式配置

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--machine.seed INT` | 随机种子 | `42` | 保证实验可复现的基础设置 |
| `--machine.num-devices INT` | 设备数量 | `1` | 单机多卡时改为 GPU 数 |
| `--machine.num-machines INT` | 分布式机器数 | `1` | 多机训练时使用 |
| `--machine.machine-rank INT` | 当前机器 rank | `0` | DDP 多机训练必需 |
| `--machine.dist-url STR` | 分布式连接地址 | `auto` | 多机通信地址 |
| `--machine.device-type {cpu,cuda,mps}` | 设备类型 | `cuda` | 一般是 NVIDIA GPU；Apple Silicon 可用 `mps` |

### 实战理解

| 场景 | 推荐设置 |
| --- | --- |
| 单卡训练 | 保持默认即可 |
| 单机多卡 | `num-devices` 改成 GPU 数量 |
| 多机训练 | 同时设置 `num-machines`、`machine-rank`、`dist-url` |
| Mac 本地实验 | 可尝试 `--machine.device-type mps` |

---

## 五、logging options：日志配置

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--logging.relative-log-dir PATH` | 日志保存相对目录 | `.` | 日志路径 |
| `--logging.steps-per-log INT` | 每多少步记录一次 | `10` | 太小会频繁刷日志，太大会丢细节 |
| `--logging.max-buffer-size INT` | 统计平滑窗口大小 | `20` | 用过去多少次记录计算 running average |
| `--logging.profiler {none,basic,pytorch}` | 性能分析模式 | `basic` | `pytorch` 更重，适合定位性能瓶颈 |

### profiler 解读

| 模式 | 含义 | 适用场景 |
| --- | --- | --- |
| `none` | 不做 profiling | 正常训练 |
| `basic` | 打印被装饰函数速度统计 | 默认调试 |
| `pytorch` | 更深入 tracing 若干训练步 | 定位性能瓶颈 |

---

## 六、logging.local-writer：终端本地打印

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--logging.local-writer.enable {True,False}` | 是否在本地终端打印统计 | `True` | 关闭后终端会安静很多 |
| `--logging.local-writer.stats-to-track [...]` | 打印哪些统计项 | 若干默认指标 | 例如训练耗时、PSNR、ETA |
| `--logging.local-writer.max-log-size INT` | 打印最大行数 | `10` | 超过后会换行或截断展示 |

### 默认跟踪指标含义

| 指标 | 含义 |
| --- | --- |
| `ITER_TRAIN_TIME` | 单次训练迭代耗时 |
| `TOTAL_TRAIN_TIME` | 总训练时间 |
| `ETA` | 预计剩余时间 |
| `TRAIN_RAYS_PER_SEC` | 训练时每秒处理 ray 数 |
| `TEST_RAYS_PER_SEC` | 测试时每秒处理 ray 数 |
| `VIS_RAYS_PER_SEC` | 可视化时每秒处理 ray 数 |
| `CURR_TEST_PSNR` | 当前测试 PSNR |

---

## 七、viewer options：可视化查看器

这一块控制 Nerfstudio viewer。

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--viewer.relative-log-filename STR` | viewer 日志文件名 | `viewer_log_filename.txt` | 一般不用改 |
| `--viewer.websocket-port INT` | websocket 端口 | `None` | 不指定时自动找 |
| `--viewer.websocket-port-default INT` | 默认端口 | `7007` | 常见 viewer 端口 |
| `--viewer.websocket-host STR` | 绑定地址 | `0.0.0.0` | 允许外部访问；本机限制可改成 `127.0.0.1` |
| `--viewer.num-rays-per-chunk INT` | 每块渲染 ray 数 | `32768` | 越大可能更快，但占显存更多 |
| `--viewer.max-num-display-images INT` | viewer 中最多显示多少训练图 | `512` | 数据集很大时避免卡顿 |
| `--viewer.quit-on-train-completion {True,False}` | 训练结束是否退出 viewer | `False` | 若想训练完就关闭可设 True |
| `--viewer.image-format {jpeg,png}` | viewer 图像格式 | `jpeg` | `jpeg` 更省带宽，`png` 更清晰 |
| `--viewer.jpeg-quality INT` | JPEG 质量 | `75` | 数值越高越清晰，带宽占用越大 |
| `--viewer.make-share-url {True,False}` | 是否生成分享 URL | `False` | beta 功能 |
| `--viewer.camera-frustum-scale FLOAT` | 相机视锥缩放 | `0.1` | 调 viewer 里的相机显示尺寸 |
| `--viewer.default-composite-depth {True,False}` | 默认是否做深度合成 | `True` | 关闭后更容易看清相机 frustum |

### 常见关注点

| 需求 | 相关参数 |
| --- | --- |
| viewer 打不开 | `websocket-port`、`websocket-host` |
| 远程服务器访问 | `websocket-host 0.0.0.0` |
| 画质更好 | `image-format png` 或提高 `jpeg-quality` |
| viewer 更流畅 | 降低 `max-num-display-images`，调小 `num-rays-per-chunk` |

---

## 八、pipeline.datamanager：数据管理与采样

这一部分决定数据如何被加载、缓存、采样。

### 1）基础数据路径与载入

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.datamanager.data PATH` | 数据源路径 | `None` | 最核心的数据输入参数 |
| `--pipeline.datamanager.masks-on-gpu {True,False}` | mask 是否放 GPU | `False` | 更快但更占显存 |
| `--pipeline.datamanager.images-on-gpu {True,False}` | 图像是否放 GPU | `False` | 大幅提速但显存开销明显 |
| `--pipeline.datamanager.camera-res-scale-factor FLOAT` | 图像/相机分辨率缩放因子 | `1.0` | 小于 1 可降分辨率节省算力 |

### 2）评估集采样

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.datamanager.eval-num-images-to-sample-from INT` | eval 时抽样图像数 | `-1` | `-1` 通常表示全部 |
| `--pipeline.datamanager.eval-num-times-to-repeat-images INT` | eval 图像重复使用次数 | `-1` | `-1` 表示不换新 |
| `--pipeline.datamanager.eval-image-indices` | eval 指定图像索引 | `0` | help 显示有点怪，通常用于只评估指定图像 |

### 3）缓存策略

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.datamanager.cache-images {cpu,gpu}` | 图像缓存位置 | `gpu` | 默认直接缓存到 GPU，速度快但吃显存 |
| `--pipeline.datamanager.cache-images-type {uint8,float32}` | 缓存图像数据类型 | `uint8` | `uint8` 更省内存；`float32` 处理更直接但大很多 |
| `--pipeline.datamanager.max-thread-workers INT` | 缓存线程数 | `None` | 不设则尽量使用可用线程 |

### 4）训练图像采样策略

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.datamanager.train-cameras-sampling-strategy {random,fps}` | 训练相机采样策略 | `random` | `fps` 是 farthest point sampling，适合减少相近视角过采样 |
| `--pipeline.datamanager.train-cameras-sampling-seed INT` | 采样随机种子 | `42` | 影响训练图像选择顺序 |
| `--pipeline.datamanager.fps-reset-every INT` | FPS 采样多久重置一次 | `100` | 控制无放回采样轮换频率 |
| `--pipeline.datamanager.train-num-images-to-sample-from INT` | 每轮训练考虑多少图像 | `-1` | `-1` 通常表示全部 |
| `--pipeline.datamanager.train-num-times-to-repeat-images INT` | 训练图像重复使用次数 | `-1` | `-1` 表示不换 |

### datamanager 核心理解

| 参数方向 | 影响 |
| --- | --- |
| `images-on-gpu` / `cache-images gpu` | 速度快，但显存压力大 |
| `camera-res-scale-factor` | 降低图像分辨率，能显著减轻训练负担 |
| `train-cameras-sampling-strategy=fps` | 对视角分布不均的数据更稳 |
| `train-num-images-to-sample-from` | 可做子集训练或加快早期实验 |

---

## 九、pipeline.model：模型主体参数

这部分最关键。它控制 Gaussian 的初始化、密化、裁剪、SH、深度损失、CLIP 相关项等。

---

### 1）基础渲染与碰撞器

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.enable-collider {True,False}` | 是否启用 scene collider | `True` | 过滤无效 ray，提高训练效率 |
| `--pipeline.model.collider-params` | collider 参数 | `near_plane 2.0 far_plane 6.0` | 控制近平面和远平面 |
| `--pipeline.model.eval-num-rays-per-chunk INT` | eval 时每块 ray 数 | `4096` | 太大可能爆显存，太小会变慢 |
| `--pipeline.model.prompt STR` | 模型文本提示 | `None` | 视觉语言/文本引导场景时使用 |

### 2）训练调度与分辨率

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.warmup-length INT` | refinement 关闭的 warmup 步数 | `500` | 前期先稳定训练 |
| `--pipeline.model.refine-every INT` | 每多少步执行一次 refine | `100` | 对 Gaussian 做 densify/cull |
| `--pipeline.model.resolution-schedule INT` | 每多少步提升分辨率 | `3000` | 从低分辨率逐步到高分辨率训练 |
| `--pipeline.model.num-downscales INT` | 初始下采样层数 | `2` | 初始训练分辨率为原图的 `1/2^d` |

### 3）背景与基本外观

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.background-color {random,black,white}` | 背景色策略 | `random` | 随机背景可提高鲁棒性，但视数据情况而定 |

### 4）Gaussian 裁剪与密化

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.cull-alpha-thresh FLOAT` | 按透明度裁剪阈值 | `0.1` | 越低保留越多点，质量可能更高但更重 |
| `--pipeline.model.cull-scale-thresh FLOAT` | 大尺度 Gaussian 裁剪阈值 | `0.5` | 防止超大点破坏渲染 |
| `--pipeline.model.continue-cull-post-densification {True,False}` | densify 后是否继续裁剪 | `True` | 一般保持开启 |
| `--pipeline.model.reset-alpha-every INT` | 每多少次 refinement 重置 alpha | `30` | 控制透明度重新分配 |
| `--pipeline.model.densify-grad-thresh FLOAT` | 根据位置梯度进行 densify 的阈值 | `0.0002` | 越低越容易 densify |
| `--pipeline.model.densify-size-thresh FLOAT` | 小于此尺寸时复制，否则 split | `0.01` | 小 Gaussian 倾向 duplicate，大 Gaussian 倾向 split |
| `--pipeline.model.n-split-samples INT` | split 成几个样本 | `2` | 拆分粒度 |
| `--pipeline.model.split-screen-size FLOAT` | 屏幕占比超过此值则 split | `0.05` | 防止某个 Gaussian 太大 |
| `--pipeline.model.stop-screen-size-at INT` | 到此 step 后停止基于屏幕大小的裁剪/切分 | `4000` | 后期不再做此类形变 |
| `--pipeline.model.stop-split-at INT` | 到此 step 后停止 split | `15000` | 后期结构趋于稳定 |

### 5）随机初始化与规模

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.random-init {True,False}` | 是否随机初始化位置 | `False` | 否则通常依赖 SfM 点 |
| `--pipeline.model.num-random INT` | 随机初始化 Gaussian 数量 | `50000` | 随机初始化时很关键 |
| `--pipeline.model.random-scale FLOAT` | 随机初始化立方体范围 | `10.0` | 决定初始点云分布空间大小 |

### 6）SH 与渲染相关

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.sh-degree-interval INT` | 每多少步开启更高一阶 SH | `1000` | 渐进式提高颜色表达能力 |
| `--pipeline.model.sh-degree INT` | 最大 SH 阶数 | `3` | 阶数越高表达越强，但更重 |
| `--pipeline.model.rasterize-mode {classic,antialiased}` | 栅格化模式 | `classic` | `antialiased` 更抗锯齿，但导出的 PLY 兼容性差 |
| `--pipeline.model.output-depth-during-training {True,False}` | 训练时是否输出深度 | `True` | 对监控深度很方便 |
| `--pipeline.model.output-semantics-during-training {True,False}` | 训练时是否输出语义信息 | `False` | 若有语义/affordance 任务才重要 |

### 7）正则化与结构控制

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.use-scale-regularization {True,False}` | 是否启用尺度正则 | `False` | 来自 PhysGaussian，用于减少尖刺型大 Gaussian |
| `--pipeline.model.max-gauss-ratio FLOAT` | 尺度比阈值 | `10.0` | 超过此比率才更强惩罚 |
| `--pipeline.model.cull-screen-size FLOAT` | 屏幕占比超过该值则 cull | `0.15` | 太大的 Gaussian 直接删掉 |

### 8）损失项

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.ssim-lambda FLOAT` | SSIM 损失权重 | `0.2` | 平衡像素误差与结构相似性 |
| `--pipeline.model.clip-img-loss-weight FLOAT` | CLIP 图像相关损失权重 | `0.1` | 视觉语言监督 |
| `--pipeline.model.clip-network-cosine-sim-loss-weight FLOAT` | CLIP 余弦相似度损失权重 | `9.0` | 视觉语义约束较强 |
| `--pipeline.model.clip-network-loss-weight FLOAT` | CLIP 网络损失权重 | `5.0` | 配合 encoder/decoder 使用 |
| `--pipeline.model.affordance-loss-weight FLOAT` | affordance 损失权重 | `0.1` | 物体可供性/交互相关任务 |

### 9）深度监督

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.use-depth-loss {True,False}` | 是否启用深度监督 | `False` | 有深度 GT 时才建议开 |
| `--pipeline.model.depth-loss-type STR` | 深度损失类型 | `EdgeAwareLogL1` | 对边缘更友好 |
| `--pipeline.model.depth-lambda FLOAT` | 深度损失权重 | `0.1` | 太大会压制 RGB 学习 |
| `--pipeline.model.use-depth-smooth-loss {True,False}` | 是否启用深度平滑损失 | `False` | 深度图更平滑，但可能损失细节 |
| `--pipeline.model.smooth-loss-type STR` | 平滑损失类型 | `EdgeAwareTV` | 边缘保留的总变分 |
| `--pipeline.model.smooth-loss-lambda FLOAT` | 平滑损失权重 | `0.05` | 需要谨慎调节 |

### 10）MLP head

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.hidden-dim INT` | MLP 隐层维度 | `128` | 控制附加头部容量 |
| `--pipeline.model.num-layers INT` | MLP 层数 | `5` | 更深表达更强，但更慢 |

---

## 十、pipeline.model.loss-coefficients

这里只有两个参数：

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.loss-coefficients.rgb-loss-coarse FLOAT` | coarse RGB loss 权重 | `1.0` | 粗阶段图像重建损失系数 |
| `--pipeline.model.loss-coefficients.rgb-loss-fine FLOAT` | fine RGB loss 权重 | `1.0` | 精阶段图像重建损失系数 |

这两个一般用于控制不同阶段的 RGB 重建损失平衡。

---

## 十一、camera-optimizer：相机位姿优化

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.model.camera-optimizer.mode {off,SO3xR3,SE3}` | 位姿优化模式 | `off` | 不优化 / 分开旋转平移 / 整体 SE3 |
| `--pipeline.model.camera-optimizer.trans-l2-penalty FLOAT` | 平移 L2 正则 | `0.01` | 防止平移漂移太大 |
| `--pipeline.model.camera-optimizer.rot-l2-penalty FLOAT` | 旋转 L2 正则 | `0.001` | 防止旋转漂移太大 |

### 模式区别

| 模式 | 含义 | 适用场景 |
| --- | --- | --- |
| `off` | 不做相机优化 | 相机姿态已可靠 |
| `SO3xR3` | 旋转和平移分开优化 | 官方提示推荐模式 |
| `SE3` | 统一刚体变换优化 | 更整体，但有时不如 `SO3xR3` 稳 |

---

## 十二、pipeline.network：视觉语言网络配置

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--pipeline.network.clip-model-type STR` | CLIP 模型类型 | `RN50x64` | 比较大的 ResNet CLIP |
| `--pipeline.network.clip-n-dims INT` | CLIP embedding 维度 | `512` | 特征维度 |
| `--pipeline.network.skip-center-crop {True,False}` | 是否跳过中心裁剪 | `True` | 数据预处理策略，影响输入到 CLIP 的图像区域 |
| `--pipeline.network.batch-size INT` | 网络 batch 大小 | `1` | CLIP 分支的 batch size |

这说明 `sagesplat` 并不只是纯几何重建，还结合了视觉语言信号。

---

## 十三、optimizers：优化器整体逻辑

这是这份 help 里最容易“看花”的部分。核心理解如下：

模型的不同参数组分别用不同优化器和学习率。例如：

* `means`：Gaussian 中心位置
* `features-dc`：颜色/低阶特征
* `features-rest`：其他特征
* `opacities`：透明度
* `scales`：尺度
* `quats`：旋转四元数
* `camera-opt`：相机优化参数
* `clip-embeds` / `clip-encoder` / `clip-decoder`
* `affordance`

也就是说，这是“多参数组、多学习率”设计。

---

## 十四、各优化器参数组详解

### 1）means：Gaussian 位置

#### optimizer

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.means.optimizer.lr FLOAT` | 位置学习率 | `0.00016` | 控制 Gaussian 中心移动速度 |
| `--optimizers.means.optimizer.eps FLOAT` | Adam epsilon | `1e-15` | 数值稳定项 |
| `--optimizers.means.optimizer.max-norm FLOAT` | 梯度裁剪阈值 | `None` | 防止梯度爆炸 |
| `--optimizers.means.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 通常位置参数不加 decay |

#### scheduler

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.means.scheduler.lr-pre-warmup FLOAT` | warmup 前学习率 | `1e-08` | 非常小的起步 |
| `--optimizers.means.scheduler.lr-final FLOAT` | 最终学习率 | `1.6e-06` | 后期收敛更稳 |
| `--optimizers.means.scheduler.warmup-steps INT` | warmup 步数 | `0` | 默认不开 warmup |
| `--optimizers.means.scheduler.max-steps INT` | 调度总步数 | `30000` | 学习率下降时长 |
| `--optimizers.means.scheduler.ramp {linear,cosine}` | warmup 曲线 | `cosine` | 更平滑 |

---

### 2）features-dc：低频/直流特征

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.features-dc.optimizer.lr FLOAT` | 学习率 | `0.0025` | 比 means 高很多，颜色特征通常更快学习 |
| `--optimizers.features-dc.optimizer.eps FLOAT` | epsilon | `1e-15` | Adam 稳定项 |
| `--optimizers.features-dc.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.features-dc.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |
| `--optimizers.features-dc.scheduler {None}` | 调度器 | `None` | 默认不单独调度 |

---

### 3）features-rest：其余特征

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.features-rest.optimizer.lr FLOAT` | 学习率 | `0.000125` | 比 DC 特征小，说明高阶特征更新更谨慎 |
| `--optimizers.features-rest.optimizer.eps FLOAT` | epsilon | `1e-15` | 数值稳定 |
| `--optimizers.features-rest.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.features-rest.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |
| `--optimizers.features-rest.scheduler {None}` | 调度器 | `None` | 默认无 |

---

### 4）opacities：透明度

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.opacities.optimizer.lr FLOAT` | 学习率 | `0.05` | 很高，透明度参数通常需要快速调整 |
| `--optimizers.opacities.optimizer.eps FLOAT` | epsilon | `1e-15` | 数值稳定 |
| `--optimizers.opacities.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.opacities.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |
| `--optimizers.opacities.scheduler {None}` | 调度器 | `None` | 默认无 |

---

### 5）scales：尺度

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.scales.optimizer.lr FLOAT` | 学习率 | `0.005` | 控制 Gaussian 大小变化 |
| `--optimizers.scales.optimizer.eps FLOAT` | epsilon | `1e-15` | 数值稳定 |
| `--optimizers.scales.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.scales.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |
| `--optimizers.scales.scheduler {None}` | 调度器 | `None` | 默认无 |

---

### 6）quats：旋转四元数

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.quats.optimizer.lr FLOAT` | 学习率 | `0.001` | 调整 Gaussian 方向 |
| `--optimizers.quats.optimizer.eps FLOAT` | epsilon | `1e-15` | 数值稳定 |
| `--optimizers.quats.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.quats.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |
| `--optimizers.quats.scheduler {None}` | 调度器 | `None` | 默认无 |

---

### 7）camera-opt：相机优化器

#### optimizer

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.camera-opt.optimizer.lr FLOAT` | 相机参数学习率 | `0.0001` | 位姿优化步子较小 |
| `--optimizers.camera-opt.optimizer.eps FLOAT` | epsilon | `1e-15` | 数值稳定 |
| `--optimizers.camera-opt.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.camera-opt.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |

#### scheduler

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.camera-opt.scheduler.lr-pre-warmup FLOAT` | warmup 前学习率 | `0` | 初始冻结或近似冻结 |
| `--optimizers.camera-opt.scheduler.lr-final FLOAT` | 最终学习率 | `5e-07` | 后期极小步优化 |
| `--optimizers.camera-opt.scheduler.warmup-steps INT` | warmup 步数 | `1000` | 说明相机优化是渐进开启的 |
| `--optimizers.camera-opt.scheduler.max-steps INT` | 最大步数 | `30000` | 调度持续长度 |
| `--optimizers.camera-opt.scheduler.ramp {linear,cosine}` | warmup 曲线 | `cosine` | 平滑 |

---

### 8）clip-embeds：CLIP embedding 参数

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.clip-embeds.optimizer.lr FLOAT` | 学习率 | `0.01` | 较高 |
| `--optimizers.clip-embeds.optimizer.eps FLOAT` | epsilon | `1e-15` | 稳定项 |
| `--optimizers.clip-embeds.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.clip-embeds.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |
| `--optimizers.clip-embeds.scheduler {None}` | 调度器 | `None` | 默认无 |

优化器类型这里是 **RAdam**，不是 Adam。

---

### 9）clip-encoder：CLIP 编码器

#### optimizer

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.clip-encoder.optimizer.lr FLOAT` | 学习率 | `0.005` | 编码器微调学习率 |
| `--optimizers.clip-encoder.optimizer.eps FLOAT` | epsilon | `1e-15` | 稳定项 |
| `--optimizers.clip-encoder.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.clip-encoder.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |

#### scheduler

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.clip-encoder.scheduler.lr-pre-warmup FLOAT` | warmup 前 lr | `1e-08` | 初始极小 |
| `--optimizers.clip-encoder.scheduler.lr-final FLOAT` | 最终 lr | `1e-06` | 后期收敛 |
| `--optimizers.clip-encoder.scheduler.warmup-steps INT` | warmup 步数 | `0` | 默认无 |
| `--optimizers.clip-encoder.scheduler.max-steps INT` | 调度总步数 | `30000` | 学习率衰减时长 |
| `--optimizers.clip-encoder.scheduler.ramp {linear,cosine}` | ramp | `cosine` | 平滑衰减 |

---

### 10）clip-decoder：CLIP 解码器

参数和 `clip-encoder` 基本对称：

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.clip-decoder.optimizer.lr FLOAT` | 学习率 | `0.005` | 解码器更新速度 |
| `--optimizers.clip-decoder.optimizer.eps FLOAT` | epsilon | `1e-15` | 稳定项 |
| `--optimizers.clip-decoder.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.clip-decoder.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |
| `--optimizers.clip-decoder.scheduler.lr-pre-warmup FLOAT` | warmup 前 lr | `1e-08` | 初始低学习率 |
| `--optimizers.clip-decoder.scheduler.lr-final FLOAT` | 最终 lr | `1e-06` | 后期收敛 |
| `--optimizers.clip-decoder.scheduler.warmup-steps INT` | warmup 步数 | `0` | 默认无 |
| `--optimizers.clip-decoder.scheduler.max-steps INT` | 总步数 | `30000` | 学习率调度长度 |
| `--optimizers.clip-decoder.scheduler.ramp {linear,cosine}` | ramp | `cosine` | 平滑 |

---

### 11）affordance：可供性模块

| 参数 | 含义 | 默认值 | 解读 |
| --- | --- | --- | --- |
| `--optimizers.affordance.optimizer.lr FLOAT` | 学习率 | `0.0005` | affordance 分支更新速度 |
| `--optimizers.affordance.optimizer.eps FLOAT` | epsilon | `1e-15` | 稳定项 |
| `--optimizers.affordance.optimizer.max-norm FLOAT` | 梯度裁剪 | `None` | 可选 |
| `--optimizers.affordance.optimizer.weight-decay FLOAT` | 权重衰减 | `0` | 默认无 |
| `--optimizers.affordance.scheduler {None}` | 调度器 | `None` | 默认无 |

---

## 十五、subcommands：数据解析子命令

help 最后一块：

| 子命令 | 作用 | 适用场景 |
| --- | --- | --- |
| `nerfstudio-data` | Nerfstudio 标准数据格式 | 最常见默认方式 |
| `minimal-parser` | 最小解析器 | 简化格式或自定义轻量输入 |
| `arkit-data` | Apple ARKit 数据 | iPhone/iPad AR 采集数据 |
| `blender-data` | Blender 合成数据 | 合成场景 |
| `instant-ngp-data` | instant-ngp 风格数据 | 与 NGP 生态兼容 |
| `nuscenes-data` | nuScenes 数据 | 自动驾驶数据 |
| `dnerf-data` | 动态 NeRF 数据 | 动态场景 |
| `phototourism-data` | Phototourism 数据 | 大规模旅游照片场景 |
| `dycheck-data` | 动态检查数据 | 动态场景实验 |
| `scannet-data` | ScanNet 数据 | 室内 RGB-D |
| `sdfstudio-data` | SDFStudio 数据 | SDF / 几何相关 |
| `nerfosr-data` | NeRF-OSR 数据 | 开放场景重建 |
| `sitcoms3d-data` | Sitcoms3D 数据 | 特定研究数据集 |
| `scannetpp-data` | ScanNet++ 数据 | 扩展室内数据 |
| `colmap` | COLMAP 重建结果 | 最常见的真实照片训练入口之一 |

### 关键理解

默认子命令是：

| 默认值 | 含义 |
| --- | --- |
| `nerfstudio-data` | 如果你不显式写子命令，通常默认按此格式解析 |

很多时候实际命令会像这样：

Bashns-train sagesplat --data data/scene01 nerfstudio-data

或者：

Bashns-train sagesplat --data data/scene01 colmap

具体取决于你的数据组织方式。

---

## 十六、这份 help 反映出的 `sagesplat` 方法特征

从参数设计看，`sagesplat` 不是纯粹的基础 3DGS，而是带有扩展模块的方法。可以概括为：

| 特征 | 证据 |
| --- | --- |
| 基于 Gaussian Splatting | 有 means、scales、quats、opacities、densify、cull 等典型参数 |
| 支持逐步 refinement | `refine-every`、`stop-split-at`、`densify-grad-thresh` |
| 支持视觉语言监督 | `prompt`、`pipeline.network.clip-*`、`clip-loss-weight` |
| 支持深度监督 | `use-depth-loss`、`depth-loss-type` |
| 支持相机位姿优化 | `camera-optimizer.mode` |
| 支持 affordance/语义信息 | `affordance-loss-weight`、`output-semantics-during-training` |

---

## 十七、常用参数优先级：新手最该关注哪些

如果你不是要改论文方法，而是先把训练跑起来，优先关注这些。

### 1）必须会改的参数

| 参数 | 为什么重要 |
| --- | --- |
| `--data` | 指定数据路径 |
| 子命令如 `colmap` / `nerfstudio-data` | 指定数据解析方式 |
| `--experiment-name` | 方便区分实验 |
| `--output-dir` | 管理输出目录 |
| `--max-num-iterations` | 控制训练时长 |
| `--vis` | 控制是否开 viewer / wandb |
| `--machine.device-type` | 确保设备正确 |
| `--pipeline.datamanager.camera-res-scale-factor` | 显存不够时先改它 |
| `--mixed-precision` | 提升速度和降低显存 |

### 2）显存不够时优先调的参数

| 参数 | 作用 |
| --- | --- |
| `--pipeline.datamanager.camera-res-scale-factor 0.5` | 降低输入分辨率 |
| `--pipeline.model.eval-num-rays-per-chunk` | 降低 eval chunk |
| `--viewer.num-rays-per-chunk` | 降低 viewer chunk |
| `--pipeline.datamanager.images-on-gpu False` | 不把图像常驻显存 |
| `--pipeline.datamanager.cache-images cpu` | 改缓存到 CPU |
| `--mixed-precision True` | 降显存 |

### 3）效果不好时优先排查的参数

| 参数 | 可能影响 |
| --- | --- |
| `cull-alpha-thresh` | 太高会删掉过多 Gaussian |
| `densify-grad-thresh` | 太高 densify 不够，细节不足 |
| `stop-split-at` | 太早停止细化会影响质量 |
| `sh-degree` | 太低颜色表达不足 |
| `camera-optimizer.mode` | 相机有误差时影响很大 |
| `use-depth-loss` / `depth-lambda` | 有深度监督时可改善几何 |

---

## 十八、一个典型命令示例

### 基础训练命令

Bashns-train sagesplat \  
  --data ./data/scene01 \  
  --experiment-name scene01_sagesplat \  
  --output-dir ./outputs \  
  --vis viewer \  
  --max-num-iterations 30000 \  
  nerfstudio-data

### 含义拆解

| 片段 | 含义 |
| --- | --- |
| `ns-train sagesplat` | 用 sagesplat 方法训练 |
| `--data ./data/scene01` | 数据路径 |
| `--experiment-name scene01_sagesplat` | 实验名称 |
| `--output-dir ./outputs` | 输出目录 |
| `--vis viewer` | 开启 viewer |
| `--max-num-iterations 30000` | 训练 3 万步 |
| `nerfstudio-data` | 用 nerfstudio 标准数据解析器 |

---

## 十九、如果按“用途”重新归类，可以这样记

| 用途类别 | 代表参数 |
| --- | --- |
| 实验命名与保存 | `output-dir`、`experiment-name`、`project-name`、`timestamp` |
| 训练流程 | `max-num-iterations`、`steps-per-save`、`steps-per-eval-*` |
| 设备与并行 | `machine.*` |
| 日志与可视化 | `logging.*`、`viewer.*`、`vis` |
| 数据加载 | `pipeline.datamanager.*` |
| 模型结构 | `pipeline.model.*` |
| 附加视觉语言网络 | `pipeline.network.*` |
| 相机优化 | `pipeline.model.camera-optimizer.*` |
| 损失权重 | `ssim-lambda`、`clip-*`、`depth-*`、`affordance-*` |
| 优化超参 | `optimizers.*` |

---

## 二十、简明结论

| 结论 | 说明 |
| --- | --- |
| 这是一个高度可配置的训练命令 | 不只是基础 NeRF/3DGS，包含视觉语言、深度、affordance、相机优化等扩展 |
| 参数树结构很重要 | 看懂前缀比死记单个参数更重要 |
| 新手先抓主线 | `data`、子命令、训练步数、显存相关参数、viewer |
| 高阶调参集中在三块 | `pipeline.model.*`、`camera-optimizer.*`、`optimizers.*` |
| `sagesplat` 明显是多分支训练框架 | 既有 Gaussian 表达，又有 CLIP/语义/affordance 相关模块 |

如果你需要，我可以下一步直接把这份 help 再整理成一版“更适合收藏的中文速查表”，按“必改参数 / 常改参数 / 高级参数”三层表格重排。