import os
import pandas as pd

# Get the unique list of subjects and sessions
# basedir  = "/bcbl/home/public/Gari/MAGNO2"
basedir="/scratch/lmx/ABCDA/"
curatedlist=os.path.join(basedir,"Nifti", "participants.tsv")

# READ THE FILE
dt = pd.read_csv(curatedlist, sep="\t")
sess = ["baselineYear1Arm1", "2YearFollowUpYArm1"]
# OBTAIN UNIQUE VALUES
# Save unique S and SS file and edit as required
subses = pd.DataFrame(columns = ["sub","ses","RUN","anat","dwi","func","age","sex"])

# Make only those dwi and func's true as required
for index, row in dt.iterrows():
    sub = row["participant_id"][4:]
    for ses in sess:
        if os.path.isdir(os.path.join(basedir, 'Nifti', 'sub-'+sub,'ses-'+ses)):
            anat = False; dwi = False; func = False
            if os.path.isdir(os.path.join(basedir,'Nifti','sub-'+sub,'ses-'+ses,'anat')):
                anat = True
            if os.path.isdir(os.path.join(basedir,'Nifti','sub-'+sub,'ses-'+ses,'dwi')):
                dwi = True
            if os.path.isdir(os.path.join(basedir,'Nifti','sub-'+sub,'ses-'+ses,'func')):
                func = True
            subses = subses.append({"sub":sub, "ses":ses, "RUN":True, "anat":anat, 
                            "dwi":dwi, "func":func, "age": row["age"], "sex": row["sex"]}, ignore_index=True)
 


opFile = os.path.join(basedir, "Nifti", 'subSesList.txt')
subses.to_csv(opFile, header=True, sep=",", index = False)


