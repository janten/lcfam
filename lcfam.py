#!/usr/bin/env python

import sys, warnings
from skimage import io, color, img_as_ubyte

if len(sys.argv) != 4:
    print 'Usage: %s <cfam.png> <fam.png> <outfile.png>' % sys.argv[0]
    sys.exit(1)

fam = io.imread(sys.argv[2])
fam_norm = fam.astype(float) / 255
cfam = io.imread(sys.argv[1])[:, :, 0:3]
cfam_lab = color.rgb2lab(cfam)
cfam_lightness = cfam_lab[:, :, 0].astype(float) / 100
lcfam_lab = cfam_lab
lcfam_lightness = fam_norm * 100
lcfam_lab[:, :, 0] = lcfam_lightness
lcfam = color.lab2rgb(lcfam_lab)
warnings.simplefilter("ignore")
io.imsave(sys.argv[3], lcfam);