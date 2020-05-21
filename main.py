import json, sys
from fatx import fatx
from fatx.interface import DirectoryObject

def listfiles(root, path=''):
	for item in root.ls():
		print(path+'/'+item._name)
		if isinstance(item, DirectoryObject):
			listfiles(item, path+'/'+item._name)

if __name__ == "__main__":
	fs = fatx.Filesystem(sys.argv[1])
	fs.status()
	root = fs.root
	listfiles(root)
