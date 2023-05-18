# File: main.py
# Date start: 17.05.2023
#
# TODO: Add a project name.
# Project name: <======>
# Author: Krystian Ozga, Stanisław Synowiec
#
# Project description:
#   A project created for the purpose of passing laboratories in object-oriented programming(OOP) in Python. The main
#   goal of the project is to test knowledge at the intermediate level.
#
import os
from src import app


# <Main application boot file>
if __name__ == '__main__':

    # The user MUST select one of the options provided.
    # At the same time, the given options are fully independent of each other, but they should not be
    # exercised at the same time.
    while True:
        optionVal: str = input('Activate unit test for software? (Yes/No)\n').lower()

        match optionVal:
            case 'yes':
                # TODO: Create a method or function responsible for the test mode.
                break

            case 'no':
                print(app.config)

                app.run()
                break
