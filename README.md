# Oleoresin Synthesis in Young Copaifera multijuga Hayne (Fabaceae) Plants

## A Chemical network for sesquitepene biosynthesis of Young Copaifera multijuga Hayne (Fabaceae) Plants

## How to use it?

First you need to have installed the MedØlDatschgerl (MØD) version 0.8.0.
Assuming you have [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) installed, then just pull the image:

`docker pull waldeyr/mod_v0.8.0:v1.0`

Clone this repository

`git clone https://github.com/waldeyr/ycp.git && cd ycp`

Run the code:

`docker run --rm --volume $(pwd):/home/shared/ --workdir /home/shared/ waldeyr/mod_v0.8.0:v1.0 /home/mod-v0.8.0/bin/mod -f /home/shared/molecules.py -f /home/shared/simulation.py -f /home/shared/printer.py `
