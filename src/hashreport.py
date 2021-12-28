#!/usr/bin/env python3

import os
from helpers.loadconfig import load_config
from data.hash import hash_file
import json
import pathlib

# Load configuration
config = load_config()

# Get root path to scan
path = config['targetPath']

# Get hash type
hash_type =  config['hash_type'].lower()

# Check if the directory is empty
if len( os.listdir(path) ) == 0:
    raise ValueError("The directory is empty.")

# Initiate hashes variable
hashes = []

# Scan path directory recursively
for subdir, dirs, files in os.walk(path):
    for file in files:

        file_fullpath = os.path.join(subdir, file)
        try:
            getHash = hash_file(file_fullpath, hash_type)
            hashes.append({ "path": os.path.abspath(file_fullpath), "hash": getHash })
            print(file_fullpath + ";" + getHash)
        except ValueError as e:
            print("Something went wrong hashing the files. " + e)

# Store hashes
hash_file_path = pathlib.Path(__file__).parent.resolve()
hash_file_path = str(hash_file_path) + "/data/hashes"
f = open(hash_file_path, "w")
f.write(json.dumps(hashes))
f.close()