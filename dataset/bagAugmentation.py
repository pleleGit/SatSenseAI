import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img, array_to_img
import shutil
import math


def augment_bag_images(root, images_per_bag=50.):
    # copy content in a new folder
    shutil.copytree(os.path.join(root, "bags"), os.path.join(root, "bagsAugmented"), dirs_exist_ok=True)
    bags_root = os.path.join(root, "bagsAugmented")
    datagen = ImageDataGenerator(
        rotation_range=20,  # [0-180]
        # width_shift_range=0.1,  # too much distortion
        # height_shift_range=0.1,  # too much distortion
        # zoom_range=0.1,
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode='constant',
        cval=0.0  # black fill
    )
    for cntr in os.listdir(bags_root):
        print(f"Processing country: {cntr}")
        country_path = os.path.join(bags_root, cntr)
        if not os.path.isdir(country_path):
            continue
        for bid in os.listdir(country_path):
            bid_path = os.path.join(country_path, bid)
            if not os.path.isdir(bid_path):
                continue
            img_names = [i for i in os.listdir(bid_path) if i.endswith(".png")]
            augmentations_per_image = math.ceil(images_per_bag / len(img_names))
            for fname in img_names:
                img_path = os.path.join(bid_path, fname)
                try:
                    img = load_img(img_path)
                    x = img_to_array(img)
                    x = x.reshape((1,) + x.shape)
                    # Generate and save a few augmentations
                    gen = datagen.flow(x, batch_size=1)
                    for i in range(augmentations_per_image):
                        aug_img = next(gen)[0].astype("uint8")
                        aug_img_pil = array_to_img(aug_img)
                        aug_filename = fname.replace(".png", f"a{i}.png")
                        aug_img_pil.save(os.path.join(bid_path, aug_filename))
                        # print(f"Saved augmented image: {aug_filename}")
                except Exception as e:
                    print(f"Failed to augment {img_path}: {e}")


# Example usage:
if __name__ == "__main__":
    rt = os.path.dirname(os.path.abspath(__file__))
    augment_bag_images(rt)
