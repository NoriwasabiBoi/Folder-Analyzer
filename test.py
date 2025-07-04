import os
import pathlib
#from pxr import Usd, UsdGeom, Vt, Sdf

class FolderAnalyzer:
    
Expand
classes.py
3 KB
﻿
import os
import pathlib
#from pxr import Usd, UsdGeom, Vt, Sdf

class FolderAnalyzer:
    
    def __init__(self, folder_path) -> None:
        self.folder_path = folder_path

class UsdEntity:
    """
    A class used to create a USD Entity

    ...

    Attributes
    ----------
    files : list
        list of files in the folder

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    path()
        Returns the path of the folder
    """
    def __init__(self, folder_path, files):
        self.folder_path = folder_path
        self.files = files
        
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
    files : list
        list of files in the folder

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    first()
        Returns the first frame
    """
    def __init__(self, folder_path, files):
        self.folder_path = folder_path
        self.framerange = files
       
    def first(self):
        return self.files[0]    
        
    def last(self):
        return self.files[-1]
    
    def range(self):
        return len(self.files)
    
    def has_range(self):
        return True
        
class Single(UsdEntity):
    pass
    
class FrameRange(UsdEntity):
    def first(self):
        return self.files[0]
    
class Asset(UsdEntity):
    def has_range(self):
        return False
    
    def payload(self):
        # dunno what this should return? I guess the payload?
        payload_path = 0
        return payload_path
        
            
    
a = FolderAnalyzer("L:/rauchertofu/00_pipeline/scripts/mac/folder")
u = UsdEntity("L:/rauchertofu/00_pipeline/scripts/mac/folder",[1,2,3,4])
s = Single("L:/rauchertofu/00_pipeline/scripts/mac/folder",[1,2,3,4])
r = FrameRange("L:/rauchertofu/00_pipeline/scripts/mac/folder",[1,2,3,4])
asset = Asset("L:/rauchertofu/00_pipeline/scripts/mac/folder",[1,2,3,4])
print(u.path())
print(u.has_range(), s.has_range())
print(r.first())
print(asset.payload())
classes.py
3 KB
