import json
import sys
import os
import nbformat
import pprint


dir_lookup = {"ai-intro":"Intro_to_DL",
              "ai-climate":"Tropical_Cyclone_Intensity_Estimation",
              "ai-cfd":"CFD"}


def create_kernel_spec(img_name, display_name):
    argv = ["shifter",
            "--image="+img_name,
            "/usr/bin/python",
            "-m",
            "ipykernel_launcher",
            "-f",
            "{connection_file}"]
    k = {"argv":argv,
         "display_name": display_name,
          "language": "python"}
    return k


def set_default_kernel(display_name, filename=None):
    notebook_dir = './'+dir_lookup[display_name]
    ipynbs = list(map(lambda x:  os.path.abspath(os.path.join('./'+dir_lookup[display_name], x)), 
                      [n for n in os.listdir(notebook_dir) if n.endswith('ipynb')]))
    if display_name == 'ai-intro':
        ipynbs.append(os.path.abspath('./Start_Here.ipynb'))
    for notebook in ipynbs:
        nb = nbformat.read(notebook, as_version=4)
        nb.metadata.kernelspec.display_name = display_name
        nb.metadata.kernelspec.name = display_name
        nb.metadata.language_info.version = '3.8.5'
        nbformat.write(nb, notebook)


# Parse shifter image and tag
img, tag = sys.argv[1], sys.argv[2]

# Write kernel spec json
spec = create_kernel_spec(img, tag)
kernel_spec_path = os.path.join(os.path.expandvars("$HOME/.local/share/jupyter/kernels"), tag)
os.makedirs(kernel_spec_path, exist_ok=True)
with open(os.path.join(kernel_spec_path, "kernel.json"), "w", encoding='utf-8') as outfile:
    json.dump(spec, outfile, ensure_ascii=False, indent=4, sort_keys=True)
    outfile.write('\n')

# Make notebooks use given kernel as default
set_default_kernel(tag)

