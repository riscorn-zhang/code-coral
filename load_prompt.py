
from syntax import directory_operations
import os

def file_of_prompt(item:str) -> str:
    return os.path.join(directory_operations.locate_directory(__file__), "prompts", item + ".md")
def load_prompt(item:str) -> str:
    response_prompt = ""
    with open(file_of_prompt(item), 'r', encoding='utf-8') as file: 
        response_prompt = file.read()
    return response_prompt