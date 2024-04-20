import torch
import matplotlib.pyplot as plt
import torchmetrics

class cryo_em:
    """A simple class for handling image data to facilitate the reconstruction process in cryo-EM."""

### Step 1: Compare
    
    def load_images(self, filepath):
        """
        A function to load data in the form of images from a specified local .npz file.
        
        Parameters:
        - filepath: a string representing the path to the .npz file containing images.
        
        Returns:
        - images: a numpy array of images loaded from the .npz file.
        """
        # PyTorch doesn't support directly loading .npz files, convert to a PyTorch tensor
        import numpy as np
        data = np.load(filepath)
        images = data['arr_0']
        return torch.tensor(images, dtype=torch.float32)

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
        # PyTorch has no direct correlation function = np.corrcoef, adjust to torch.corrcoef from the torchmetrics package
        metric = torchmetrics.PearsonCorrCoef()
        similarities = [metric(image.flatten(), ref.flatten()).item() for ref in reference_images]
        mean_similarity = torch.mean(torch.tensor(similarities))
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
        image1_flat = image1.flatten()
        image2_flat = image2.flatten()
        mean1 = torch.mean(image1_flat)
        mean2 = torch.mean(image2_flat)
        denom = torch.sqrt(torch.sum((image1_flat - mean1) ** 2)) * torch.sqrt(torch.sum((image2_flat - mean2) ** 2))
        # Avoid division by zero
        if denom == 0:
            return 0  
        else:
            return torch.sum((image1_flat - mean1) * (image2_flat - mean2)) / denom

### Step 2: Cluster
    
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
            sim_matrix = torch.zeros((len(clusters), len(clusters)))

            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
            # Check against the first image in each cluster
                    sim_matrix[i, j] = self.calculate_similarity(images[clusters[i][0]], images[clusters[j][0]])
        
            # Find the two most similar clusters
            i, j = torch.unravel_index(torch.argmax(sim_matrix), sim_matrix.shape)

            # Merge these clusters
            clusters[i].extend(clusters[j])
            del clusters[j]

        # Return cluster assignments
        labels = torch.zeros(len(images), dtype=torch.int)
        for cluster_id, cluster in enumerate(clusters):
            for image_id in cluster:
                labels[image_id] = cluster_id
        return labels
    
        # sim_matrix = torch.zeros((len(clusters), len(clusters)))
        #     # Calculate similarity matrix
        #     sim_matrix = np.zeros((len(clusters), len(clusters)))

        #     for i in range(len(clusters)):
        #         for j in range(i + 1, len(clusters)):
        #             # Check against the first image in each cluster
        #             sim_matrix[i, j] = self.calculate_similarity(images[clusters[i][0]], images[clusters[j][0]])

        #     # Find the two most similar clusters
        #     i, j = np.unravel_index(sim_matrix.argmax(), sim_matrix.shape)

        #     # Merge these clusters
        #     clusters[i].extend(clusters[j])
        #     del clusters[j]

        # # Return cluster assignments
        # labels = np.zeros(len(images), dtype=int)
        # for cluster_id, cluster in enumerate(clusters):
        #     for image_id in cluster:
        #         labels[image_id] = cluster_id
        # return labels
    
### Step 3: Visualise
    
    def visualise_clusters(self, images, labels, n_samples=5):
        """
        A function that visualises a random sample of images from each cluster.

        Parameters:
        - images: a numpy.ndarray numpy array of images.
        - labels: a numpy.ndarray array of cluster labels for each image.
        - n_samples: integer with the number of images to sample from each cluster for visualisation.
        """
        if isinstance(labels, torch.Tensor):
            labels = labels.cpu().numpy()

        unique_labels = set(labels)
        n_clusters = len(unique_labels)
        fig, axs = plt.subplots(n_clusters, n_samples, figsize=(n_samples * 2, n_clusters * 2), squeeze=False)
        
        for i, cluster in enumerate(unique_labels):
            # Filter cluster images
            cluster_images = images[labels == cluster]
            # Convert cluster_images to numpy if it's a tensor
            if isinstance(cluster_images, torch.Tensor):
                cluster_images = cluster_images.cpu().numpy()

            # Sample indices for visualization
            sample_indices = torch.randperm(len(cluster_images))[:min(len(cluster_images), n_samples)].tolist()
            for j, idx in enumerate(sample_indices):
                axs[i, j].imshow(cluster_images[idx], cmap='gray')
                axs[i, j].axis('off')
            axs[i, 0].set_ylabel(f'Cluster {cluster}')

        plt.tight_layout()
        plt.show()

        # Check if images are tensors, as they may need to be converted to NumPy arrays before plotting?