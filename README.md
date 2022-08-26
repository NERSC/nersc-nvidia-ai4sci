# NERSC AI for Science Bootcamp

This repository contains setup instructions and material for the NERSC AI for Science Bootcamp, August 25-26, 2022.
All tutorial content comes from the [Open Hackathons GPU bootcamp repository](https://github.com/openhackathons-org/gpubootcamp/tree/master/hpc_ai).

## Accessing Perlmutter

These notebooks can be run in NERSC JupyterHub via [jupyter.nersc.gov](https://jupyter.nersc.gov).
Once logged into the hub, start a session by clicking the button for **Perlmutter Exclusive GPU Node**. 
Once your GPU node has been allocated, you can run the setup steps below and start using the bootcamp materials.

## Running bootcamp materials

To begin, start a terminal from JupyterHub and clone this repository with:
```bash
cd $SCRATCH
git clone https://github.com/NERSC/nersc-nvidia-ai4sci.git
cd nersc-nvidia-ai4sci
```

Then, run the setup script to install the bootcamp materials, data, and software environment by executing the following command in the termial:
```bash
bash setup.sh
```

This might take awhile to copy the data and notebooks, but when finished you should see some subdirectories created for the different tutorial contents:
```
Intro_to_DL
Tropical_Cyclone_Intensity_Estimation
CFD
```

You can use the Jupyter file browser to view the source files and notebooks. If you get lost, you can always click on the `$SCRATCH` folder shortcut to return to your scratch directory. To begin, simply open the `Start_Here.ipynb` notebook included in this repository. All notebooks contain relative links to each other for easy navigation between different parts of the bootcamp.
