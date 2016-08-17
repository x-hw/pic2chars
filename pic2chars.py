# -*- coding: utf-8 -*-

import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('file', help='the picture to convert')
parser.add_argument('-o', '--output', help="the filename to output, default 'output.txt' ")
parser.add_argument('-w', '--width', type=int, help='the width of output file')
parser.add_argument('-ht', '--height', type=int, help='the height of output file')

args = parser.parse_args()

#you can change chars(black to white):
#chars = list("@@WW##$$XXoo**""==::''..--  ")
chars = list("01. ")

def get_char(r, b, g, alpha = 256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return chars[int(gray / 256.0 * len(chars))]
    
if __name__ == '__main__':
    im = Image.open(args.file)
    w = args.width if args.width else im.size[0]
    h = args.height if args.height else im.size[1]
    im = im.resize((w,h), Image.ANTIALIAS)
    
    im = im.convert('RGBA')
       
    txt = ""	
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            txt += get_char(*im.getpixel((i,j)))
        txt += '\n'

    if args.output:
        with open(args.output,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)