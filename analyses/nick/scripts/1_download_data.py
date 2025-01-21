import os
import sys
from pathlib import Path
import requests
import zipfile
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tqdm import tqdm




print('downloading data...')
cache_dir = Path(os.getcwd()) / 'cache/data.zip'
cache_dir.parent.mkdir(exist_ok=True, parents=True)
if not cache_dir.exists():
        response = requests.get("https://uni-bonn.sciebo.de/index.php/s/bIDNCBs37frcli8/download", stream=True)
        response.raise_for_status()
        with cache_dir.open(mode='wb') as f:
            for chunk in tqdm(response.iter_content(chunk_size=8192)):
                if chunk:
                    f.write(chunk)




root = Path(os.getcwd()) / 'data/raw'
root.mkdir(exist_ok=True, parents=True)
if not list(root.iterdir()):
    with zipfile.ZipFile(str(cache_dir), 'r') as zip_ref:
        zip_ref.extractall(root)