from pathlib import Path

def find_usd_file(keyword, folder):
    """
    Searches for the first USD file in the given folder containing the specified keyword in its filename.

    Args:
        keyword (str): The keyword to search for in USD filenames.
        folder (Path): A pathlib.Path object pointing to the directory to search in.

    Returns:
        str: The full POSIX-style path to the first matching USD file.

    Raises:
        FileNotFoundError: If no matching USD file is found in the folder.
    """
    path =  list(folder.glob(f"*{keyword}.usd"))[0]
    if not path:
        raise FileNotFoundError(f"No USD file with keyword '{keyword}' found in {folder}")
    return str(path.as_posix())

class UsdEntity:
    """
    Base class for a USD entity, representing a single or non-sequence USD asset.

    This class provides a common interface for handling USD entities located in
    a given folder path. It can be extended for both static (single file) and
    time-varying (range) assets.

    Attributes:
        folder_path (str): The path to the folder containing the USD asset.
    """
    def __init__(self, folder_path):
        self.folder_path = folder_path
        
    def has_range(self):
        return False

    def path(self):
        return self.folder_path
    
class UsdRange(UsdEntity):
    """
    Represents a time-varying USD entity, such as an animation or simulation.

    Inherits from `UsdEntity`. This class automatically detects a sequence
    of USD files in the folder based on a naming pattern that includes a
    4-digit frame number (e.g., `asset.0100.usd`).

    Attributes:
        file_sequence (List[str]): A list of frame identifiers extracted from USD filenames.
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
    """
    Represents a single, static USD asset.

    Inherits from `UsdEntity`.
    
    Attributes:
        type (str): Identifies the entity type, set to "Single".
    """
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.type = "Single"
    
class FrameRange(UsdRange):
    """
    Represents a USD entity that spans a range of frames.

    Inherits from `UsdRange`.

    Attributes:
        type (str): Identifies the entity type, set to "FrameRange".
    """
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.type = "FrameRange"
    
class Asset(UsdEntity):
    """
    Represents a general-purpose USD asset.

    Inherits from `UsdEntity`.

    Attributes:
        type (str): Identifies the entity type, set to "Asset".
    
    Methods:
        payload(): Returns the path to the asset's payload USD file.
    """
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.type = "Asset"
    
    def payload(self):
        payload_path = find_usd_file("payload", self.folder_path)
        return payload_path
        
class USDVolume(UsdRange):
    """
    Represents a volumetric USD asset that spans a range of frames.

    Inherits from `UsdRange`, and is specifically used for `.vdb` files
    (typically OpenVDB volume data) that exist as a sequence over time. It overrides the `UsdRange` file_sequnce attribute

    Attributes:
        file_sequence (List[str]): A list of frame identifiers extracted from
                                   the VDB filenames.
        type (str): Identifies the entity type, set to "USDVolume".
    """
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.file_sequence = list(Path(f).parts[-1].split(".")[-2] for f in Path(folder_path).glob("*.vdb"))
        self.type = "USDVolume"

class StichClip(UsdRange):
    """
    Represents a stitched USD clip across a frame range.

    Inherits from `UsdRange`. This class is used to handle compound USD assets
    made by stitching together multiple clips into a single timeline. It provides
    methods to retrieve the manifest and topology files associated with the clip.

    Attributes:
        type (str): Identifies the entity type, set to "StichClip".
    
    Methods:
        manifest(): Returns the path to the manifest USD file.
        topology(): Returns the path to the topology USD file.
    """
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.type = "StichClip"
        
    def manifest(self):
        manifest_path = find_usd_file("manifest", self.folder_path)
        return manifest_path
    
    def topology(self):
        topology_path = find_usd_file("topology", self.folder_path)
        return topology_path            
