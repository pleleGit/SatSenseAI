import os
import shutil


def form_bags(root):
    base_root = os.path.join(root, "images", "content", "VIIRS")
    if not os.path.isdir(base_root):
        print(f"Initial dataset {base_root} not exist")
        exit(1)
    new_root = os.path.join(root, "bags")
    os.makedirs(new_root, exist_ok=True)
    # collect all existing countries in 'images' directory
    countries = [f for f in os.listdir(base_root) if os.path.isdir(os.path.join(base_root, f))]
    years = range(2014, 2024)  # from 2014 to 2024 inclusive
    for cntr in countries:
        c_path = os.path.join(base_root, cntr)
        if not os.path.isdir(c_path):
            continue
        for y in years:
            year_str = f"-{y}"
            bag_code = f"b{str(y)[-2:]}"
            bag_folder = os.path.join(new_root, cntr, bag_code)
            os.makedirs(bag_folder, exist_ok=True)
            for f_name in os.listdir(c_path):
                if f_name.endswith(".png") and year_str in f_name:
                    header = bag_code + f_name.split("-")[0] + ".png"
                    src_path = os.path.join(c_path, f_name)
                    dst_path = os.path.join(bag_folder, header)
                    try:
                        shutil.copy2(src_path, dst_path)
                        # print(f"Copied: {src_path} -> {dst_path}")
                    except Exception as e:
                        print(f"Failed to copy {src_path}: {e}")
            # check if bag empty, remove it
            if not os.listdir(bag_folder):
                os.rmdir(bag_folder)
                print(f"Removed empty bag folder: {bag_folder}")

    print("Bag formation completed.")


if __name__ == "__main__":
    # get current script's path as root path
    rt = os.path.dirname(os.path.abspath(__file__))
    # function that organizes satellite images in bags per year recorded
    form_bags(rt)
