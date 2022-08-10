#!/bin/bash

img1="pzharrington/ai-science-cfd:test"
img2="pzharrington/ai-science-climate:test"
base=$(pwd)


if [ ! -e Intro_to_DL ]; then
    echo -n "Building material -- Intro to DL..."
    shifter --image=$img1 bash -c "
            cp -r /workspace/python/jupyter_notebook/Intro_to_DL $base
            python kernel_setup.py $img1 ai-intro
    "
    echo "done"
fi

if [ ! -e Tropical_Cyclone_Intensity_Estimation ]; then
    echo -n "Building material -- AI for Climate..."
    shifter --image=$img2 bash -c "
            cp -r /workspace/python/jupyter_notebook/Tropical_Cyclone_Intensity_Estimation/  $base
            python kernel_setup.py $img2 ai-climate
    "
    echo "done"
fi

if [ ! -e CFD ]; then
    echo -n "Building material -- AI for CFD..."
    shifter --image=$img1 bash -c "
            cp -r /workspace/python/jupyter_notebook/CFD $base
            python kernel_setup.py $img1 ai-cfd
    "
    echo "done"
fi

