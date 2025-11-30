import ollama
from syntax import directory_operations
import load_prompt
import os
import tempfile
import time
import markdown_it
import code_response
import debug_response
import globals

def ask_for_original_requirement()->str:
    file_of_default_prompt = load_prompt.file_of_prompt("default_prompt")
    prompt=input(f"请输入你想让AI生成代码的描述 ( 默认: { file_of_default_prompt } ): ")
    if prompt.strip() == "":
        prompt = load_prompt.load_prompt("default_prompt")

    return prompt
def main():
    prompt=ask_for_original_requirement()
    code_responser = code_response.CodeResponser()
    code_file_name = code_responser.make_original_code(prompt)
    print(f"\n\n\n{ code_responser.message_list }\n\n\n");
    while True:
        suggestion=debug_response.human_debug(code_file_name)
        if suggestion.strip() == "":
            break
        code_file_name = code_responser.make_suggested_code(suggestion)

if __name__ == '__main__':
    print("Available models before running the chat (And for starting the service of Ollama if it is not running):")
    os.system('ollama list')
    print("")
    main()