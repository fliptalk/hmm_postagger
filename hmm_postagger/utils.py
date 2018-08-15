import os

class Corpus:
    def __init__(self, filepath):
        self.filepath = filepath
    def __iter__(self):
        with open(self.filepath, encoding='utf-8') as f:
            for doc in f:
                pos_list = [word.rsplit('/', 1) for word in doc.split() if word]
                if pos_list:
                    yield pos_list

def check_dirs(path):
    dirname = os.path.dirname(path)
    if dirname and dirname != '.' and not os.path.exists(dirname):
        os.makedirs(dirname)