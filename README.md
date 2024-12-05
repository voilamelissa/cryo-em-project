<img width="1355" alt="Screenshot 2024-03-24 at 07 59 26" src="https://github.com/voilamelissa/cryo-em-project/assets/23558054/a076f5b2-df0f-4c55-8f01-2f36e75175dd">

# cryo-em-project

### A pipeline for cryo-EM reconstruction
:wave: Welcome to my cryo-EM project! This Python-based toolkit is designed to facilitate the reconstruction process in cryo-electron microscopy (cryo-EM), and is comprised of three main functionalities:

* **Step 1: Compare** – Compares images with reference particles to filter out noise, serving as the initial particle picking phase.
* **Step 2: Cluster** – Groups identified particles into clusters based on visual similarity, crucial for organising data for analysis.
* **Step 3: Visualise** – Creates graphical representation of clusters to evaluate clustering quality and understand particle distribution.

### Functionality
The toolkit identifies whether a selection of picked particles are visually similar enough to manually selected ones.
* **Input**: Images adapted from [EMPIAR](https://www.ebi.ac.uk/empiar/).
* **Output**: A decision per image, from comparing to a reference image of a particle, to classification within a dedicated cluster based on categorisation, and visualisation of the output.

Images are found within the **all_images.npz** file in [cryo-em-project/project_em_particple/all_images.npz](https://github.com/voilamelissa/cryo-em-project/blob/main/project_em_particle/all_images.npz), and functionality is handled by the **cryo_em** class in [cryo-em-project/cryo_em_toolkit.py](https://github.com/voilamelissa/cryo-em-project/blob/main/cryo_em_toolkit.py). The project functionalities are outlined in the tutorial notebook ([cryoEM-notebook.ipynb](https://github.com/voilamelissa/cryo-em-project/blob/main/cryoEM%E2%80%93notebook.ipynb)) and docstrings.

If you're new to Cryo-EM as a concept and want to get familiar with the dataset images before checking out the main functionalities in the toolkit, we have a simple notebook provided within the [project_em_particle](https://github.com/voilamelissa/cryo-em-project/tree/main/project_em_particle) folder called [EM_images.ipynb](https://github.com/voilamelissa/cryo-em-project/blob/main/project_em_particle/EM_images.ipynb) you can check out!

If you change any aspects of the code during your tinkering, such as the number of clusters you split the data into – be sure to check for any dependencies in the unit tests (visualisations in particular will be impacted in the Jupyter notebook).

### Pre-requisites
* Tested with python 3.12.1
* matplotlib
* numpy

### Setting up your development environment
To run this project, it's recommended to use a virtual environment to keep dependencies required from other projects separate by creating isolated environments for each project (for example, if the requirement here is Python 3, but you have a different project that also requires you to have Python 2 installed, you can prevent version conflicts and ensure that each project's dependencies are managed correctly).

#### Using a Virtual Environment
* **1. Create a virtual environment.** Navigate to the project's root directory in your terminal or command prompt, and run the following command to create a virtual environment named **env**: `python3 -m venv env` for MacOS and Linux, or `python -m venv env` for Windows.
* **2. Activate your virtual environment.** `source env/bin/activate` for MacOS and Linux, or its `.\env\Scripts\activate` for Windows users.
* **3. Install any dependencies.** After activating your virtual environment, you'll need to install the project's dependencies in **requirements.txt** by running `pip install -r requirements.txt`: this command will install all the required Python packages as specified.
* **4. Deactivate your virtual environment**. Once you're done working on the project, you can deactivate the virtual environment by running `deactivate`

### Roadmap
Planned improvements will include investigating the following in order to improve speed and efficiency, including the current compute load required for clustering. On the list:
* pytorch
* scipy
* scikit-learn
* scikit-image
* torchvision
* Docker for packaging the application for containerised deployments
