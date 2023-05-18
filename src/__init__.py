# Initialization file for all contents of 'src' directory.
# The content of the file is extremely important globally for the entire application. So do not remove
# anything from it that could in any way affect the functioning of the application.
#
# <Flask's main data package>
from flask import Flask

app: Flask = Flask(__name__)


# TODO: You should change the location and include the code below.
# Path configuration for 'config' files.
from dotenv import load_dotenv
from pathlib import Path

dotenv_path: Path = Path('config/serverConfig.env')
load_dotenv(dotenv_path=dotenv_path)