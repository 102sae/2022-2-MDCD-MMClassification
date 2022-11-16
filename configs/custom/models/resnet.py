# python tools/train.py configs/custom/models/resnet.py

_base_ = [
    "../helper/dataset.py",
    "../helper/runtime.py",
    "../helper/schedule.py",
    "../../_base_/models/resnet50.py"
]

model = dict(
    backbone=dict(
      in_channels=3,
    ),
    head=dict(
        num_classes=4,
        topk=1,
    ))

runner = dict(type="EpochBasedRunner", max_epochs=10)