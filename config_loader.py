from syntax import directory_operations
import os

config_dir = os.path.join(directory_operations.locate_directory(__file__),"config")
def get_config(item:str,name:str)->str:
    config_file = os.path.join(config_dir,item)