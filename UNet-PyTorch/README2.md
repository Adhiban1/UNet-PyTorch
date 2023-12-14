# UNet-PyTorch

- OS: Windows
- Python-Version: 3.11
- Terminal: Git Bash
- Download: https://aka.ms/vs/16/release/vc_redist.x64.exe

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

I write [predict.py](predict.py)

```
python predict.py <input-path> <output-path>
```

```
python predict.py data/test-volume.tif data/test-labels.tif
```