import ipywidgets as widgets
from ipywidgets import FileUpload
from IPython.display import display
from PIL import Image
import os

def change_file_type(upload):
    """
    Changes image files to PNG format. Renames to `image.png` and deletes original file.
    """
    for name, file_info in upload.value.items():
        with open (name, 'wb') as file:
            file.write(file_info['content'])
        file = name
    img = Image.open(file)
    img.save("image.png")
    if os.path.exists(file):
        os.remove(file)