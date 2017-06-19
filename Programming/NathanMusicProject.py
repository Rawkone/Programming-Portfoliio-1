# python code
#
# script_name: Intro Script
#
# author: The EarSketch Team
#
# description: This code adds one audio clip to the DAW
#
#
#

#Setup Section
from earsketch import *
init()
setTempo(105)

#Music Section
fitMedia(Y07_DRUM_SAMPLE, 1, 3, 11)
fitMedia(Y08_BASS, 2,3,11)
fitMedia(YG_NEW_HIP_HOP_SYNTH_LEAD_1, 3,1,3)
fitMedia(RD_RNB_ACOUSTIC_NYLONSTRING_4, 4,3,11)

#Finish Section
finish()