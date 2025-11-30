import os
import sys
import subprocess

if sys.platform == "win32":
    # CREATE_NEW_CONSOLE 的值是 0x00000010
    CREATE_NEW_CONSOLE = 0x00000010 
else:
    # 在非 Windows 系统上，将该标志设为 0，防止错误
    CREATE_NEW_CONSOLE = 0

def run_code(code_locaition:str):
    try:
        print("\nExecuting the generated code:\n")
        subprocess.run(["python", code_locaition], check=True, creationflags=CREATE_NEW_CONSOLE)
        print("\nExecution completed.\n")
    except Exception as e:
        print(f"\nError: {e}")
        print("Execution completed with an exception.\n")

def ai_debug(requirement:str, responsed_code:str)->str:
    pass

def human_debug(code_location:str)->str:
    while True:
        run_code(code_location)
        if input("Execute again? (y/[n]): ") != "y":
            break;
    suggestions=input("Type some suggestions:>\n")
    return suggestions