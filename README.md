# cryo-em-project
A simple script for cryo-EM micrographs and single particle analysis.

:wave: Welcome to the cryo-EM project! This Python-based library integrates machine learning and computer vision functionalities to streamline cryo-electron microscopy (cryo-EM) data processing. The project is comprised of three main functions [TBC]:

* **cluster_images(image_folder, num_clusters)**: This function clusters the micrographs stored in the specified image_folder using a clustering algorithm, facilitating efficient organization and analysis of the data.

* **particle_picking(micrograph, template)**: Designed to enhance particle identification accuracy, this function employs template matching techniques to locate individual protein particles within a given micrograph. It compares the micrograph with a user-defined template, enabling precise particle picking while minimizing false positives.

* **classify_particles(particles)**: This function categorizes the detected particles based on their features, allowing for further analysis and processing of the cryo-EM data.

### Functionality
Images and visualisation are handled by the [PLACEHOLDER] module in cryo-em-project/images.py [TBC]. The project functionalities are outlined in the tutorial notebook and docstrings.

### Pre-requisites [TBC]
* Tested with python 3.12.1
* matplotlib
* numpy
* pytorch
* scipy
* scikit-learn
* scikit-image
* torchvision
