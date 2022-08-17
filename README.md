# NERSC AI for Science Bootcamp

This repository contains setup instructions and material for the NERSC AI for Science Bootcamp, August 25-26, 2022.
All tutorial content comes from the [Open Hackathons GPU bootcamp repository](https://github.com/openhackathons-org/gpubootcamp/tree/master/hpc_ai).

## Accessing Perlmutter

To activate your training account, visit [iris.nersc.gov/train](https://iris.nersc.gov/train) and fill in the training account request form. The access code for this event will be given out in the presentations and posted on the event's Slack channel.
Once you have your provided account credentials, you can log in to the NERSC JupyterHub via [jupyter.nersc.gov](https://jupyter.nersc.gov) (leave the OTP field blank when logging into JupyterHub).

Once logged into the hub, start a session by clicking the button for **Perlmutter Configurable GPU Node** (other options will not be able to use the compute reservation for this event). Use the following options when configuring the GPU node:
```
Account: ntrain1
Constraint: gpu
QOS: jupyter
cpus-per-task: 128
gpus-per-task: 4
nodes: 1
ntasks-per-node: 1
Reservation: ai4sci
time: 180
```

Note that the `ai4sci` reservation for this event expires at 12:30 PT each day; if you request a time limit that would make your job run beyond the end of the reservation, your GPU node will not start. Once your GPU node has been allocated, you can run the setup steps below and start using the bootcamp materials.

## Running bootcamp materials

To begin, start a terminal from JupyterHub and clone this repository with:
```bash
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

You can use the Jupyter file browser to view the source files and notebooks. If you get lost, you can always click on the `$HOME` folder shortcut to return to your home directory. To begin, simply open the `Start_Here.ipynb` notebook included in this repository. All notebooks contain relative links to each other for easy navigation between different parts of the bootcamp.