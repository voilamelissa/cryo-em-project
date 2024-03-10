import numpy as np
import matplotlib.pyplot as plt

class cryo_em:
    """A simple class for handling image data to facilitate the reconstruction process in cryo-EM."""

# Step 1: Compare
    def load_images(self, filepath):
        """
        A function to load data in the form of images from a specified local .npz file.
        
        Parameters:
        - filepath: a string representing the path to the .npz file containing images.
        
        Returns:
        - images: a numpy array of images loaded from the .npz file.
        """
        data = np.load(filepath)
        images = data['arr_0']
        return images

    def compare_with_reference(self, image, reference_images, threshold):
        """
        A function to compare a single image with a set of reference images to determine similarity.
        
        Parameters:
        - image: a numpy array representing the image to compare.
        - reference_images: a list of numpy arrays representing the reference images.
        - threshold: a float representing the threshold for determining similarity.
        
        Returns:
        - A boolean value indicating whether the image is similar to the reference images
          (True if similar, False otherwise).
        """
        similarities = [np.corrcoef(image.ravel(), ref.ravel())[0, 1] for ref in reference_images]
        mean_similarity = np.mean(similarities)
        return mean_similarity > threshold

    def calculate_similarity(self, image1, image2):
        """
        A function to calculate a similarity value between two images for categorisation.

        Parameters:
        - image1: a numpy.ndarray numpy array representing the first image.
        - image2: a numpy.ndarray numpy array representing the second image.
        
        Returns:
        - float: a correlation coefficient between the two images, indicating their similarity.
        """
        return np.corrcoef(image1.ravel(), image2.ravel())[0, 1]

# Step 2: Cluster
    def hierarchical_clustering(self, images, n_clusters):
        """
        A function that performs basic hierarchical clustering on a set of images.

        Parameters:
        - images: a numpy.ndarray numpy array of images to cluster.
        - n_clusters: an integer with the desired number of clusters.

        Returns:
        - numpy.ndarray: an array of cluster labels for each image.
        """
        # Initialise clusters with each image as a separate cluster
        clusters = [[i] for i in range(len(images))]

        while len(clusters) > n_clusters:
            # Calculate similarity matrix
            sim_matrix = np.zeros((len(clusters), len(clusters)))

            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    # Check against the first image in each cluster
                    sim_matrix[i, j] = self.calculate_similarity(images[clusters[i][0]], images[clusters[j][0]])

            # Find the two most similar clusters
            i, j = np.unravel_index(sim_matrix.argmax(), sim_matrix.shape)

            # Merge these clusters
            clusters[i].extend(clusters[j])
            del clusters[j]

        # Return cluster assignments
        labels = np.zeros(len(images), dtype=int)
        for cluster_id, cluster in enumerate(clusters):
            for image_id in cluster:
                labels[image_id] = cluster_id
        return labels

    # def load_and_display_images(image_file, num_images=4):
    #     """
    #     Load image data from a .npz file and display a random selection of images.
        
    #     Parameters:
    #     - image_file: Path to the .npz file containing images.
    #     - num_images: Number of images to display.
    #     """
    #     data = np.load(image_file)
    #     images = [data['arr_0'][i, :, :] for i in range(data['arr_0'].shape[0])]
    #     print(f"Total images loaded: {len(images)}")

    #     fig, axes = plt.subplots(1, num_images, sharex=True, sharey=True)
    #     for ax, i in zip(axes, np.random.permutation(len(images))[:num_images]):
    #         ax.imshow(images[i])
    #         ax.set_title(f"Image {i}")
    #     fig.tight_layout()
    #     plt.show()
    #     return images


    # def cluster_images(image_folder, num_clusters): 
    #     """
    #     This function clusters the micrographs stored in the specified image_folder 
    #     using a clustering algorithm, facilitating efficient organisation and analysis of the data. 
    #     [TBC based on decision routine provided, may just be an image loader].
    #     Parametres:
    #     Input/Output/Return:
    #     """
        
    # def particle_picking(micrograph, template): 
    #     """
    #     Designed to enhance particle identification accuracy, 
    #     this function employs template matching techniques to locate individual protein 
    #     particles within a given micrograph. It compares the micrograph with a user-defined template, 
    #     enabling precise particle picking while minimising false positives.
    #     Parametres:
    #     Input/Output/Return:
    #     """
        
    # def classify_particles(particles): 
    #     """
    #     This function categorises the detected particles based on their features, 
    #     allowing for further analysis and processing of the cryo-EM data.
    #     Parametres:
    #     Input/Output/Return:
    #     """