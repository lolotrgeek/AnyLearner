import pkgutil
search_path = ['./agents'] # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)

# import sys

import modules
from modules.publish import Publish
from modules.reply import Reply