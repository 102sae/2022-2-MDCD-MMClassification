checkpoint_config = dict(max_keep_ckpts=2, interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type="TextLoggerHook"),
    ],
)

# yapf:enable
dist_params = dict(backend="nccl")
log_level = "INFO"
load_from = None
resume_from = None
workflow = [('train', 1), ('val', 1)]

# Custom Addition
seed = 42
gpu_ids = [0]

evaluation = dict(
    interval=1,
    metric=['accuracy', 'f1_score'],
    metric_options=dict(
        topk=1,
    ),
    save_best="accuracy",
)