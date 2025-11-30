import os,ollama,load_prompt,time,markdown_it,globals


class CodeResponser:
    model="codegemma"
    message_list=[]
    
    md=markdown_it.MarkdownIt('commonmark')
    def __init__(self):
        self.message_list.append(
            {
                'role': 'system',
                'content': load_prompt.load_prompt("python_simple")
            },
        )

    def make_original_code(self, requirement:str)->str:
        return self.make_code(requirement)

    def make_suggested_code(self, requirement:str)->str:
        prompt=load_prompt.load_prompt("suggestion_addition").format(suggestion=requirement)
        return self.make_code(prompt)

    def make_code(self,prompt:str)->str:
        self.message_list.append(
            {
                'role': 'user',
                'content': prompt
            },
        )
        stream = ollama.chat(
            model='codegemma',
            messages=self.message_list,
            stream=True
        )
        tmp_file = os.path.join(globals.globals["tmp_dir"], str(time.time())+".py")

        original_response = ""
        code_response = ""

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
            original_response += chunk['message']['content']

        code_response = self.extract_code_blocks(original_response)[0]

        self.message_list.append(
            {
                "role": "assistant",
                "content": code_response
            }
        )
        
        with open(tmp_file, 'w', encoding='utf-8') as tmp_file_obj:
            tmp_file_obj.write(code_response)

        print("\n\nResponse saved to:", tmp_file)

        return tmp_file
    def extract_code_blocks(self,markdown_text: str) -> list:
        tokens = self.md.parse(markdown_text)
        code_blocks = []
        for token in tokens:
            if token.type == 'fence':
                code_blocks.append(token.content)
        return code_blocks
    