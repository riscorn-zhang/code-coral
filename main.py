import ollama
from syntax import directory_operations
import load_prompt
import os
import tempfile
import time
import markdown_it

md=markdown_it.MarkdownIt('commonmark')

tmp_dir = os.path.join(tempfile.gettempdir(),"CodeCoral")
os.makedirs(tmp_dir, exist_ok=True)

def extract_code_blocks(markdown_text: str) -> list:
    tokens = md.parse(markdown_text)
    code_blocks = []
    for token in tokens:
        if token.type == 'fence':
            code_blocks.append(token.content)
    return code_blocks
def get_response(prompt:str)->str:
    stream = ollama.chat(
        model='gemma',
        messages=[
            {
                'role': 'system',
                'content': load_prompt.load_prompt("python_simple")
            },
            {
                'role': 'user',
                'content': prompt
            }
            ],
        stream=True
    )

    tmp_file_path = os.path.join(tmp_dir, str(time.time())+".py")

    original_response = ""
    code_response = ""

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        original_response += chunk['message']['content']

    code_response = extract_code_blocks(original_response)[0]
    
    with open(tmp_file_path, 'w', encoding='utf-8') as tmp_file:
        tmp_file.write(code_response)

    print("\n\nResponse saved to:", tmp_file_path)

    return tmp_file_path

def main():
    default_prompt = '''### 2. 📝 项目建议：Markdown 驱动的知识库管理工具

这是一个侧重于文本解析和数据持久化的项目，适用于个人笔记或文档管理。

| **复杂性** | **核心功能** | **复杂点** |
| --- | --- | --- |
| **中** | 允许用户通过 Markdown 文件创建、查询和管理结构化的知识条目。 | **高级 Markdown 解析**（精确提取代码块/YAML Front Matter）、**数据索引**、**简单的全文搜索**。 |''';
    prompt=input(f"请输入你想让AI生成代码的描述 (默认: {default_prompt}): ")
    if prompt.strip() == "":
        prompt = default_prompt
    file_name = get_response(prompt);
    print("\nExecuting the generated code:\n")
    os.system(f'python "{file_name}"')

if __name__ == '__main__':
    print("Available models before running the chat (And for starting the service of Ollama if it is not running):")
    os.system('ollama list')
    print("")
    main();