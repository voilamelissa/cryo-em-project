import unittest
import numpy as np
from cryo_em_toolkit import cryo_em

class TestCryoEM(unittest.TestCase):

    def set_up(self):
        """Set up any variables and instances needed for the tests."""
        self.cryo_em_instance = cryo_em()
        self.sample_npz_file = './project_em_particle/all_images.npz'

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

class TestCryoEMClustering(unittest.TestCase):
    ########################################## WIP

    def test_cluster_images(self):
        """Test that images are clustered into specified groups."""
        images = self.cryo_em_instance.load_images(self.sample_npz_file)
        # Default cluster count, adjust to fit requirement
        n_clusters = 2
        labels = self.cryo_em_instance.cluster_images(images, n_clusters)
        
        # Verify number of unique labels matches number of clusters
        unique_labels = set(labels)
        self.assertEqual(len(unique_labels), n_clusters, "The number of clusters should match the expected value.")

if __name__ == '__main__':
    unittest.main()