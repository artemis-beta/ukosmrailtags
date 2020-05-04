import json
import glob
import logging
import os

logging.basicConfig(level=logging.DEBUG)

class SignalEntryParser(object):
    def __init__(self, root_dir=None):
        self._logger = logging.getLogger('SignalEntryParser')
        self._root = root_dir if root_dir else os.getcwd()

    def makeMD(self):
        _folders = glob.glob(os.path.join(self._root, 'signal', '*'))

        _out = '''# UK Signals Database for OSM
Below is a listing of various types of UK signal and the proposed methods for tagging them in OpenRailwayMap
'''

        for f in _folders:
            _out += '''
## {}

| **Description** | **Image** | **Tags** |
|---|---|---|
'''.format(f.split('/')[-1].title())
            _files = glob.glob(os.path.join(f, '*.json'))
            _dict = None
            for i, in_file in enumerate(_files):
                with open(in_file) as file_obj:
                    _dict = json.load(file_obj)
                    _tags = ['{}={}'.format(i, _dict['tags'][i]) for i in _dict['tags']]
                    _out +='''| {} | ![{}]({}) | {} |
'''.format(_dict['description'], 'image_'+str(i),
                                  _dict['img'], '</br>'.join(_tags))

        with open(os.path.join(self._root, 'Catalog.md'), 'w') as f:
            f.write(_out)


if __name__ in "__main__":
    SignalEntryParser().makeMD()
