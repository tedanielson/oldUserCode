#!/bin/bash


global=express/BeamCommissioning09  # Runs: < 122011 -
path=OfflineMonitor/FEVTHLTALL/v2     # Runs: < 122011 -
#path=MinimumBias/RAW/v1     # Runs: < 122011 -
# path=TestEnables/RAW/v1   # ONLY FOR TESTS
a=124
b=230
nFiles=100

cat << EOF >> "listoffiles_${run}.txt"

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
EOF

nsls /castor/cern.ch/cms/store/$global/$path/000/$a/$b |
head -n $nFiles |
awk -v globalTemp=$global -v pathTemp=$path -v aTemp=$a -v bTemp=$b '{print "        '\''rfio:/castor/cern.ch/cms/store/data/" globalTemp "/" pathTemp "/000/" aTemp "/" bTemp "/" $1 "'\'',"}' |
sed '$s/.$//' >> "listoffiles_${run}.txt"

cat << EOF >> "listoffiles_${run}.txt"
    )
)

