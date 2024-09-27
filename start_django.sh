#!/bin/bash
namedir="venv"
if [ ! -d "$namedir" ]; then
     python3 -m venv "$namedir"   
else
    echo "$namedir já existe"
fi