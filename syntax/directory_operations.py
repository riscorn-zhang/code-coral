
import os
def locate_directory(item_name:str) -> str:
    """
    Locate the directory of a given item name.
    
    Args:
        item_name (str): The name of the item to locate.
        
    Returns:
        str: The directory path where the item is located.
    """
    return os.path.dirname(os.path.abspath(item_name))