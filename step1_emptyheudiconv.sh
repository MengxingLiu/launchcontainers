basedir="/scratch/lmx/ABCDA"
subj="NDARINV0JR6Y529"
ses='baselineYear1Arm1'

# First run it empty
singularity run \
	        --bind ${basedir}:/base \
		/scratch/lmx/containers/heudiconv_0.11.6.sif \
		-d /base/raw_zip/sub-{subject}/ses-${ses}/anat/*NORM*/*.dcm \
                -o /base/Nifti/ \
                -f bids_with_ses \
                -s ${subj} \
                -ss ${ses} \
		--grouping all \
                -c none


