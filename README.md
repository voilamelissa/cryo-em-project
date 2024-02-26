# cryo-em-project
### A pipeline for cryo-EM reconstruction
:wave: Welcome to my cryo-EM project! This Python-based toolkit is designed to facilitate the reconstruction process in cryo-electron microscopy (cryo-EM). 

A custom class is built as part of the toolkit, comprised of three main functions:

* **cluster_images(image_folder, num_clusters)**: This function clusters the micrographs stored in the specified image_folder using a clustering algorithm, facilitating efficient organisation and analysis of the data. [*TBC based on decision routine provided, may just be an image loader*]
* **particle_picking(micrograph, template)**: Designed to enhance particle identification accuracy, this function employs template matching techniques to locate individual protein particles within a given micrograph. It compares the micrograph with a user-defined template, enabling precise particle picking while minimising false positives.
* **classify_particles(particles)**: This function categorises the detected particles based on their features, allowing for further analysis and processing of the cryo-EM data.

### Functionality
The toolkit identifies whether a selection of picked particles are visually similar enough to manually selected ones.
* **Input**: Images adapted from EMPIAR.
* **Output**: A decision per image.

Images and visualisation are handled by the [*PLACEHOLDER*] module in cryo-em-project/images.py [*TBC*]. The project functionalities are outlined in the tutorial notebook and docstrings.

### Pre-requisites [*TBC*]
* Tested with python 3.12.1
* matplotlib
* numpy
* pytorch
* scipy
* scikit-learn
* scikit-image
* torchvision
