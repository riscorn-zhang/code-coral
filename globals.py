import os
import tempfile

globals = {
    "tmp_dir":os.path.join(tempfile.gettempdir(),"CodeCoral"),
    "initialed": False,
}

def init():
    os.makedirs(globals["tmp_dir"], exist_ok=True)

if globals["initialed"] == False:
    globals["initialed"] = True
    init()