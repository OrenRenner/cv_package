import os

def get_im_list(path):
    return [
        os.path.join(path, f) for f in os.listdir(path)
        if f.endswith('.jpg')
    ]
