import sys
import os
from pathlib import Path

# add current working directory to sys path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import classes

folder_path = "L:/rauchertofu/00_pipeline/scripts/mac/files"

def analyze_folder(subfolder):
    """
    Analyzes the contents of a given subfolder and determines its USD entity type.

    Based on the files found within the folder, it returns an instance of one of the
    following classes:
        - Single: A folder with a single file.
        - Asset: A folder containing a `payload.usd` file.
        - StichClip: A folder containing frame-based USDs and a `*.manifest.usd`.
        - FrameRange: A folder with numbered USD files but no manifest.
        - USDVolume: A folder containing `.vdb` files (volumetric data).

    Args:
        subfolder (Path or str): Path to the folder to analyze.

    Returns:
        UsdEntity: An instance of one of the entity classes (Single, Asset, StichClip, etc.),
                   or None if the folder does not match any known pattern.
    """
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
    """
    Iterates over subfolders within the given directory and classifies each one
    as a specific USD entity type.

    Uses `analyze_folder` to detect the type of each subfolder and organizes the results
    into a dictionary grouped by type.

    Args:
        path (Path or str): Path to the root directory containing subfolders to analyze.

    Returns:
        dict: A dictionary with keys as USD types ('Single', 'Asset', 'StichClip', 'FrameRange', 'USDVolume')
              and values as lists of class instances corresponding to each type.
    """
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
        
dict = iterate_folder(folder_path)

print(dict["StichClip"][0].manifest())
