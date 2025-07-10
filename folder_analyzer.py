import sys
import os
import re
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import classes

folder_path = "L:/rauchertofu/00_pipeline/scripts/mac/files"

def analyze_folder(subfolder):
    s = Path(subfolder)
    
    # Case of a single USD
    if len(list(s.glob("*"))) == 1:
        single = classes.Single(subfolder)
        return single
    
    # Case Of USD Asset
    if list(s.glob("payload.usd")):
        asset = classes.Asset(subfolder)
        return asset
    
    # Case of Stich
    if list(s.glob("*.[0-9][0-9][0-9][0-9].usd")):
        if list(s.glob("*.manifest.usd")):
            stich = classes.StichClip(subfolder)
            return stich
        
        # Case of Frame Range    
        else:
            range = classes.FrameRange(subfolder)
            return range
    
    # Case Of USD Volume
    if list(s.glob("*.vdb")):
        vdb = classes.USDVolume(subfolder)
        return vdb
    return None

def iterate_folder(path):
    p = Path(path)
    
    contents = {
        "Single":[],
        "Asset":[],
        "StichClip":[],
        "FrameRange":[],
        "USDVolume":[]
    }
    
    for subfolder in [s for s in p.iterdir() if s.is_dir()]:
        class_object = analyze_folder(subfolder=subfolder)
        contents[class_object.type].append(class_object)
    return contents
        
iterate_folder(folder_path)