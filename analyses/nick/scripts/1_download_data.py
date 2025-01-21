import os
from shutil import copytree
import sys
from pathlib import Path
import requests
import zipfile
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tqdm import tqdm
copytree


root = Path.cwd()

print('downloading data...')
cache_dir = root / 'cache'
cache_dir.mkdir(exist_ok=True, parents=True)
cache_archive = cache_dir / 'data.zip'
if not cache_archive.exists():
    response = requests.get("https://uni-bonn.sciebo.de/index.php/s/bIDNCBs37frcli8/download", stream=True)
    response.raise_for_status()
    with cache_archive.open(mode='wb') as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192)):
            if chunk:
                f.write(chunk)

print('extracting data...')
expected_folder = cache_dir / 'visual_coding_spiking_data'
if not expected_folder.exists():
    with zipfile.ZipFile(str(cache_archive), 'r') as zip_ref:
        zip_ref.extractall(cache_dir)
if not expected_folder.exists():
    raise FileNotFoundError("Folder wasn't created: " + str(expected_folder))


print('copying to data/raw...')
copytree(expected_folder, 'data/raw')
