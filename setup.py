# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:16:56 2023

@author: marlo
"""

from cx_Freeze import setup, Executable

# Specify the main script (1.py)
main_script = "main.py"

# Create an Executable object for the main script
executables = [Executable(main_script)]

setup(
    name="AFKFarm",
    version="1.0",
    description="AFKFarm for DBD (1920x1080 screen resolution, 2023)",
    executables=executables,
    options={
        "build_exe": {
            "includes": ["findMainWindow"],  # Add the name of the module (2.py) to include it
        }
    }
)
