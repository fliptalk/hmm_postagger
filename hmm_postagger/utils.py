import os

class Corpus:
    def __init__(self, path, num_sent=-1):
        self.path = path
        self.num_sent = num_sent
    def __iter__(self):
        with open(self.path, encoding='utf-8') as f:
            for i, sent in enumerate(f):
                if self.num_sent > 0 and i > self.num_sent:
                    break
                wordpos = [token.rsplit('/', 1) for token in sent.split()]
                yield wordpos

def check_dirs(path):
    dirname = os.path.dirname(path)
    if dirname and dirname != '.' and not os.path.exists(dirname):
        os.makedirs(dirname)

bos = 'BOS'
eos = 'EOS'
unk = 'Unk'