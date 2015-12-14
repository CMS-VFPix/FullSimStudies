#!/usr/bin/env python



# makes one canvas for each pt to test for each variable for each element of 'plots'

pts_to_test = ['0p7','1p0','10p0','50p0','100p0']
#pts_to_test = ['0p7']
variables_to_test = ['pt','d0','dz']
#variables_to_test = ['pt']
baseline = '80x52'

# will replace 'pitch' with actual pitch
inputFileFormat = "ttbar_pitch.root"

plots = []

changeLocalX = {
    'name' : 'changeLocalX',
    'title' : 'Changing Pitch in Local X (Global R)',
    'pitches' : ['73x52', '53x52', '40x52']
}
plots.append(changeLocalX)

changeLocalY = {
    'name' : 'changeLocalY',
    'title' : 'Changing Pitch in Local Y (Global #phi)',
    'pitches' : ['80x47', '80x35', '80x26']
}
plots.append(changeLocalY)

