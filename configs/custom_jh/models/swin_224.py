# python tools/train.py configs/custom/models/swin_transformer/swin_224.py

_base_ = [
    "../helper/dataset.py",
    "../helper/runtime.py",
    "../helper/schedule.py",
    "../../_base_/models/swin_transformer/base_224.py"
]

model = dict(
    head=dict(
        num_classes=2,
        topk=1,
    ))

runner = dict(type="EpochBasedRunner", max_epochs=10)