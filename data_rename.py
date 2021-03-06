import os
import os.path

def rename():
    pic_root = os.path.join(".", "Dataset", "raw_screenshots")
    sample_root = [os.path.join(pic_root, x) 
        for x in os.listdir(pic_root)]  # sample 目录列表

    for e in sample_root:
        sample_old = os.listdir(e)
        sample_new = sorted(sample_old, key=lambda x: os.path.getmtime(os.path.join(e, x)))
        nums = len(sample_new)
        for i in range(nums):
            old = os.path.join(e, sample_new[i])
            os.rename(old, os.path.join(e, f"{i:04d}.jpg"))

rename()