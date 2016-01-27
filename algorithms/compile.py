import yaml
import os
import subprocess

with open('header.tex') as header_file:
    header = yaml.load(header.read().replace('\n', '\n\n'))
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(".tex")::
            with open(name) as source:
                with open('temp.tex', 'w') as temp:
                    temp.write()
