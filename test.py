#!/usr/bin/env python3

import sys
import os
import nibabel as nib

def main():
    if len(sys.argv) < 3:
        print("Usage: python test.py <subjects_dir> <subj>")
        sys.exit(1)

    subjects_dir = sys.argv[1]
    subj = sys.argv[2]

    t1_path = os.path.normpath(f'{subjects_dir}/{subj}/mri/T1.mgz')
    print(f"Trying to load T1 image from: {t1_path}")

    try:
        img = nib.load(t1_path)
        print(f"Image loaded successfully!")
        print(f"Image type: {type(img)}")
        print(f"Image shape: {img.shape}")
        print(f"Image affine:\n{img.affine}")
    except Exception as e:
        print(f"Failed to load image. Error:\n{e}")

if __name__ == "__main__":
    main()
