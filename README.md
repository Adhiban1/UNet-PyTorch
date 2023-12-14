# UNet-PyTorch

- OS: Windows
- Python-Version: 3.11
- Terminal: Git Bash
- Download: https://aka.ms/vs/16/release/vc_redist.x64.exe

requirements.txt is not provided. So I analyzed the python files and write requirements.txt

```
git clone https://github.com/hayashimasa/UNet-PyTorch.git

cd UNet-PyTorch/

python -m venv venv

source venv/Scripts/activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python train.py --epoch 50 --batch-size 3 --save
```

For Initial trial I use 5 epochs.

```
>python train.py --epoch 5 --batch-size 3 --save
 
 ...
  
Validation set: Average loss: 0.1511, Average IOU score: 0.61, Average pixel accuracy: 0.84

Train Epoch: 5 [3/27 (11%)]     Loss: 0.343738
Train Epoch: 5 [6/27 (22%)]     Loss: 0.345460
Train Epoch: 5 [9/27 (33%)]     Loss: 0.325542
Train Epoch: 5 [12/27 (44%)]    Loss: 0.280142
Train Epoch: 5 [15/27 (56%)]    Loss: 0.304326
Train Epoch: 5 [18/27 (67%)]    Loss: 0.307270
Train Epoch: 5 [21/27 (78%)]    Loss: 0.282833
Train Epoch: 5 [24/27 (89%)]    Loss: 0.312001
Train Epoch: 5 [27/27 (100%)]   Loss: 0.323002

Validation set: Average loss: 1.0269, Average IOU score: 0.11, Average pixel accuracy: 0.21

Best IOU: 0.6231045207358745
Pixel accuracy: 0.8319672346115112
```

This 5 epochs takes nearly 1 hour in my laptop.

I write [predict.py](predict.py)

```
python predict.py <input-path> <output-path>
```

```
python predict.py data/test-volume.tif data/test-labels.tif
```

![visualization/UNet50_2.png](visualization/UNet50_2.png)

# UNet-PyTorch-Predict

Files required:

- data/
- models/
- predict.py
- unet.py
- README2.md (renamed as README.md)

Installation:
```
python -m venv venv
source venv/Scripts/activate
pip install matplotlib
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

Prediction:
```
python predict.py data/test-volume.tif data/test-labels.tif
```

![visualization/UNet50_2.png](visualization/UNet50_2.png)

## Docker

Docker build:
```
docker build -t unet-pytorch-predict .
```

Docker run:
```
cd data
docker run -it --rm -v .:/images unet-pytorch-predict
```

test:
```
venv/bin/python predict.py /images/test-volume.tif /images/test-labels.tif
```

or

```
source venv/bin/activate
python predict.py /images/test-volume.tif /images/test-labels.tif
```

Save docker image:
```
docker save -o unet-pytorch-predict.tar unet-pytorch-predict
```

## Docker using Ubuntu

Docker build:
```
docker build -f Dockerfile-ubuntu -t unet-pytorch-predict:ubuntu .
```

run:
```
docker run -it --rm unet-pytorch-predict:ubuntu
```

test:
```
venv/bin/python predict.py data/test-volume.tif data/test-labels.tif
```

Docker save:
```
docker save -o unet-pytorch-predict-ubuntu.tar unet-pytorch-predict:ubuntu
```

## Docker push

```
docker tag unet-pytorch-predict adhiban/unet-pytorch-predict
docker tag unet-pytorch-predict:ubuntu adhiban/unet-pytorch-predict:ubuntu
docker push adhiban/unet-pytorch-predict
docker push adhiban/unet-pytorch-predict:ubuntu
```

# 20 Epochs

```
>python train.py --epoch 20 --batch-size 3 --save
...
Train Epoch: 20 [3/27 (11%)]    Loss: 0.235412
Train Epoch: 20 [6/27 (22%)]    Loss: 0.248010
Train Epoch: 20 [9/27 (33%)]    Loss: 0.260933
Train Epoch: 20 [12/27 (44%)]   Loss: 0.249919
Train Epoch: 20 [15/27 (56%)]   Loss: 0.234743
Train Epoch: 20 [18/27 (67%)]   Loss: 0.234228
Train Epoch: 20 [21/27 (78%)]   Loss: 0.244294
Train Epoch: 20 [24/27 (89%)]   Loss: 0.234752
Train Epoch: 20 [27/27 (100%)]  Loss: 0.244324

Validation set: Average loss: 0.1904, Average IOU score: 0.72, Average pixel accuracy: 0.90

Best IOU: 0.7274544850516571
Pixel accuracy: 0.8976467251777649
```