import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def display_sample_images():
    # Define the categories and their paths
    categories = ['high', 'medium', 'low']
    fig, axes = plt.subplots(3, 2, figsize=(12, 15))
    fig.suptitle('Sample Images from Training and Test Sets', fontsize=16)

    for idx, category in enumerate(categories):
        # Training image
        train_path = f'data/train/{category}/{os.listdir(f"data/train/{category}")[0]}'
        train_img = mpimg.imread(train_path)
        axes[idx, 0].imshow(train_img)
        axes[idx, 0].set_title(f'Training: {category} risk')
        axes[idx, 0].axis('off')

        # Test image
        test_path = f'data/test/{category}/{os.listdir(f"data/test/{category}")[0]}'
        test_img = mpimg.imread(test_path)
        axes[idx, 1].imshow(test_img)
        axes[idx, 1].set_title(f'Test: {category} risk')
        axes[idx, 1].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    display_sample_images()
