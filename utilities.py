from PIL import Image
# import tkinter

def import_image(filename, abs_path=False):
    file_path = filename
    if not abs_path:
        file_path = 'test_images' + file_path

    im = Image.open(file_path).convert

    return im

