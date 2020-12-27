# CNN Amateur to Pro


CV 4 top job
classification:
location:
detection: location+classification
segmentation (instantce-levele, sematic segmentation)

ways to achieve the aim:
traditional cv+ml
dl

# object detection
algrithms:
1. one stage: YOLO, SSD and RetinaNet
2. two stages:
    a) region proposal, RP --> b)cnn to classificate
    feature detection --> RP --> classification/regression
    ways: R-CNN, Fast R-CNN, Faster R-CNN and R-FCN

used data:
1. Pascal voc
2. ms coco
3. open images V6

critical parameter:
1. intersection over union(IoU)
2. mean average precision (mAP): the precision- recall curve of IoU, and 

# basic structure

conv-bn-ReLU-pooling

# Faster-RCNN
rust regresion(get roi)--> get the ratial of roi--> modify bounding boxes

Head --> RPN --> classification network