
basedir=/scratch/xgao/ABCDA_19
subj=$1
ses=$2

if [ -d $basedir/raw_zip/sub-${subj}/ses-${ses}/anat/*NORM*/ ];
then
T1=NORM
else
T1=T1_run
fi
echo $subj $ses $T1
singularity run --bind ${basedir}:/base \
        /scratch/xgao/containers/heudiconv_0.11.6.sif \
        -d /base/raw_zip/sub-{subject}/ses-${ses}/anat/*${T1}*/*.dcm \
        --outdir /base/Nifti/ \
        --heuristic /base/heuristic.py \
        --subjects ${subj} \
        --ses ${ses} \
        --converter dcm2niix \
        --bids \
        --minmeta \
        --grouping all \
        --overwrite


