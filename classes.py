import os
from pathlib import Path
import logging

def find_usd_file(keyword, folder):
    path =  list(folder.glob(f"*{keyword}.usd"))[0]
    return str(path.as_posix())

class UsdEntity:
    """
    A class used to create a USD Entity

    ...

    Attributes
    ----------
    folder_path : str
        The path to the folder associated with this USD entity.

    Methods
    -------
    has_range(self)
        Returns False if it's a single or an asset, for ranges True
    path(self)
        Returns the path of the folder
    """
    def __init__(self, folder_path):
        self.folder_path = folder_path
        
    def has_range(self):
        return False

    def path(self):
        return self.folder_path
    
class UsdRange(UsdEntity):
    """
    A class used to create a USD Range that inherits from UsdEntity

    ...

    Attributes
    ----------
    folder_path : str
        The path to the folder associated with this USD entity.
        
    file_sequnce : list
        List of all frames of the folder

    Methods
    -------
    first(self)
        Returns the first frame number
        
    last(self)
        Returns the last frame number
        
    range(self)
        Returns the range
        
    has_range(self)
        overrides UsdEntity has_range to be true
    """
    
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.file_sequence = list(Path(f).parts[-1].split(".")[-2] for f in Path(folder_path).glob("*[0-9][0-9][0-9][0-9].usd"))
    
    def first(self):
        return self.file_sequence[0]    
        
    def last(self):
        return self.file_sequence[-1]
    
    def range(self):
        return len(self.file_sequence)
    
    def has_range(self):
        return True
        
class Single(UsdEntity):
    
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.type = "Single"
    
class FrameRange(UsdRange):
    
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.type = "FrameRange"
    
class Asset(UsdEntity):
    
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.type = "Asset"
    
    def payload(self):
        payload_path = find_usd_file("payload", self.folder_path)
        return payload_path
        
class USDVolume(UsdRange):
    
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.file_sequence = list(Path(f).parts[-1].split(".")[-2] for f in Path(folder_path).glob("*.vdb"))
        self.type = "USDVolume"

class StichClip(UsdRange):
    
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.type = "StichClip"
        
    def manifest(self):
        manifest_path = find_usd_file("manifest", self.folder_path)
        return manifest_path
    
    def topology(self):
        topology_path = find_usd_file("topology", self.folder_path)
        return topology_path            