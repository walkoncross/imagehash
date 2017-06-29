# -*- coding: utf-8 -*-

import imagehash
import numpy as np
from PIL import Image

def get_image_hash(img_path):
    img = Image.open(img_path)
    hash_val = imagehash.average_hash(img)

    return hash_val

fn1 = './data/koala1.jpg'
#fn2 = './data/koala4.jpg'
fn2 = './data/another_koala.jpg'

#fn1 = 'c:/zyf/test_imgs/oscar1.jpg'
#fn2 = 'c:/zyf/test_imgs/Oscars.jpg'
#fn2 = 'c:/zyf/test_imgs/lena.jpg'

#img1 = Image.open(fn1)
#hash1 = imagehash.phash(img1)
hash1 = get_image_hash(fn1)
print('\n--->' + fn1)
print('image hash is: {}'.format(hash1))

#img2 = Image.open(fn2)
#hash2 = imagehash.phash(img2)
hash2 = get_image_hash(fn2)
print('\n--->' + fn2)
print('image hash is: {}'.format(hash2))

diff = hash1 - hash2
similaritty = 1 - diff/64.0

print('\ndiff between two hash valuses is: {}'.format(diff))
print('similarity between two images is: {}'.format(similaritty))