import unittest
import numpy as np
from cryo_em_toolkit import cryo_em

class TestCryoEM(unittest.TestCase):

    def setUp(self):
        """Initialise variables and instances required for testing."""
        self.cryo_em_instance = cryo_em()
        self.sample_npz_file = './project_em_particle/all_images.npz'
        self.images = self.cryo_em_instance.load_images(self.sample_npz_file)

    def test_load_images(self):
        """Test that images are loaded correctly from a .npz file."""
        images = self.cryo_em_instance.load_images(self.sample_npz_file)
        # Adjust based on number of sample files
        expected_num_images = 10
        self.assertEqual(len(images), expected_num_images, "The number of loaded images should match the expected value.")

    def test_compare_with_reference(self):
        """Test the similarity comparison between images."""
        # Load images for testing
        images = self.cryo_em_instance.load_images(self.sample_npz_file)
        # First image is used as a reference and tested against itself
        reference_images = [images[0]]
        image_to_test = images[0]
        # High threshold when comparing image to itself
        threshold = 0.9
        # Expected boolean value: True
        self.assertTrue(self.cryo_em_instance.compare_with_reference(image_to_test, reference_images, threshold),
                        "Identical images should be considered similar.")

    def test_calculate_similarity(self):
        """Test the calculation of similarity between two images."""
        similarity = self.cryo_em_instance.calculate_similarity(self.images[0], self.images[0])
        # Assuming perfect similarity when comparing an image to itself
        self.assertEqual(similarity, 1.0, "The similarity of an image to itself should be 1.")

    def test_hierarchical_clustering(self):
        """Test hierarchical clustering method."""
        n_clusters = 2  # Example: aiming to cluster into 2 groups for simplicity
        labels = self.cryo_em_instance.hierarchical_clustering(self.images, n_clusters)
        # Test if the correct number of clusters is returned
        self.assertEqual(len(set(labels)), n_clusters, "The number of clusters should match the desired number.")

if __name__ == '__main__':
    unittest.main()