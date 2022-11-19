# python tools/train.py configs/custom/models/efficientnet_b0.py

_base_ = [
    "../helper/dataset.py",
    "../helper/runtime.py",
    "../helper/schedule.py",
    "../../_base_/models/efficientnet_b0.py"
]

model = dict(
    head=dict(
        num_classes=4,
        topk=1,
    ))

runner = dict(type="EpochBasedRunner", max_epochs=10)