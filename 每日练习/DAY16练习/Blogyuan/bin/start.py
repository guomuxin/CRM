import sys
import os
PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PATH)
from core import src

src.run()