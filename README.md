# cryo-em-project
### A pipeline for cryo-EM reconstruction
:wave: Welcome to my cryo-EM project! This Python-based toolkit is designed to facilitate the reconstruction process in cryo-electron microscopy (cryo-EM), and is comprised of three main functionalities:

* **Step 1: Compare** – Compares images with reference particles to filter out noise, serving as the initial particle picking phase.
* **Step 2: Cluster** – Groups identified particles into clusters based on visual similarity, crucial for organising data for analysis.
* **Step 3: Visualise** – Creates graphical representation of clusters to evaluate clustering quality and understand particle distribution.

### Functionality
The toolkit identifies whether a selection of picked particles are visually similar enough to manually selected ones.
* **Input**: Images adapted from EMPIAR.
* **Output**: A decision per image, from comparing to a reference image of a particle, to classification within a dedicated cluster based on categorisation, and visualisation of the output.

Images are found within the **all_images.npz** file in [cryo-em-project/project_em_particple/all_images.npz](https://github.com/voilamelissa/cryo-em-project/blob/main/project_em_particle/all_images.npz), and functionality is handled by the **cryo_em** class in [cryo-em-project/cryo_em_toolkit.py](https://github.com/voilamelissa/cryo-em-project/blob/main/cryo_em_toolkit.py). The project functionalities are outlined in the tutorial notebook ([cryoEM-notebook.ipynb](https://github.com/voilamelissa/cryo-em-project/blob/main/cryoEM%E2%80%93notebook.ipynb)) and docstrings.

If you're new to Cryo-EM as a concept and want to get familiar with the dataset images before checking out the main functionalities in the toolkit, we have a simple notebook provided within the [project_em_particle](https://github.com/voilamelissa/cryo-em-project/tree/main/project_em_particle) folder called [EM_images.ipynb](https://github.com/voilamelissa/cryo-em-project/blob/main/project_em_particle/EM_images.ipynb) you can check out!

If you change any aspects of the code during your tinkering, such as the number of clusters you split the data into – be sure to check for any dependencies in the unit tests (visualisations in particular will be impacted in the Jupyter notebook).

### Pre-requisites
* Tested with python 3.12.1
* matplotlib
* numpy

### WIP
* pytorch
* scipy
* scikit-learn
* scikit-image
* torchvision