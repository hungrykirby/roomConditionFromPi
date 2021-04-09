import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')

FIREBASE_FIRENAME=os.environ.get("FIREBASE_FIRENAME")
FIREBASE_ADMINURL=os.environ.get("FIREBASE_ADMINURL")