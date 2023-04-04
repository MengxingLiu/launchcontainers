#!/bin/python

import pandas as pd
import os
import subprocess as sp

df = pd.read_csv("failed_sub.txt",sep=' ')

base_dir = "/scratch/xgao/ABCDA_19"
for index in df.index:
    sub = df.loc[index,'sub']
    ses = df.loc[index,'ses']

    # print file number under
    dicom_dir = f"{base_dir}/raw_zip/sub-{sub}/ses-{ses}"
    if not os.path.exists(dicom_dir):
        print(sub,ses, "not exist")
        continue

    heudi_dir = f"{base_dir}/Nifti/.heudiconv/{sub}/ses-{ses}/info/"
    if ses == "2YearFollowUpYArm1":
        source_file = f"{base_dir}/Nifti/.heudiconv/{sub}/ses-baselineYear1Arm1/info/{sub}_ses-baselineYear1Arm1.edit.txt"
        target_file = f"{base_dir}/Nifti/.heudiconv/{sub}/ses-{ses}/info/{sub}_ses-{ses}.edit.txt"
    elif ses == "baselineYear1Arm1":
        source_file = f"{base_dir}/Nifti/.heudiconv/{sub}/ses-2YearFollowUpYArm1/info/{sub}_ses-2YearFollowUpYArm1.edit.txt"
        target_file = f"{base_dir}/Nifti/.heudiconv/{sub}/ses-{ses}/info/{sub}_ses-{ses}.edit.txt"

    cmd_str = f"cp {source_file} {target_file}"
    print(cmd_str)
    sp.call(cmd_str, shell=True)
    cmd_str = f"bash step2_heudiconv.sh {sub} {ses}"
    print(cmd_str)
    sp.call(cmd_str, shell=True)

