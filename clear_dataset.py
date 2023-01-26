import os
from pathlib import Path

from PIL import Image
from tqdm import tqdm

TRAIN_DATASET = Path("./data/train/")
TEST_DATASET = Path("./data/test/")
IMG_SIZE = 384

new_train = TRAIN_DATASET.parent / f"train_{IMG_SIZE}"
new_test = TEST_DATASET.parent / f"test_{IMG_SIZE}"

new_train.mkdir(parents=True, exist_ok=True)
new_test.mkdir(parents=True, exist_ok=True)

for path in tqdm(list(TRAIN_DATASET.iterdir())):
    filepath = new_train/f'{path.stem}.jpg'
    if not os.path.exists(filepath):
        img = Image.open(path).convert('RGB')
        img = img.resize((IMG_SIZE, IMG_SIZE))
        img.save(filepath)

for path in tqdm(list(TEST_DATASET.iterdir())):
    filepath = new_test / f"{path.stem}.jpg"
    if not os.path.exists(filepath):
        img = Image.open(path).convert("RGB")
        img = img.resize((IMG_SIZE, IMG_SIZE))
        img.save(filepath)
