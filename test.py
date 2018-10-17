# coding=utf-8

import parse
import os
import sys
import glob

##### constants
NUM = 6
WIDTH, HEIGHT = 400, 300

NAMES = [
    "camp",
    "ccorr",
    "flag",
    "flag_phase",
    "flag_phaseG_amp",
    "flag_phase_laplacian",
    "binAmp",
]

# {}: items
CODE0_HTML = """<html>
<head>
<title></title>
</head>
<body>
{}
</body>
</html>
"""
# {}, {}, {}, {}, {}: id, imgname, W, H, id
CODE1_ITEM = """<p>
<a href="views/{}.html">
<img src="imgs/{}" width={} height={}/> {}
</a>
</p>
"""

# {}, {}, {}, {}: imgname, W, H, name
CODE2_ITEM = """<p>
<img src="../imgs/{}" width={} height={}/> {}
</p>
"""


##### function
def getPath():
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            return sys.argv[1]
    return '.'


##### main
if __name__ == '__main__':
    PATH = getPath()

    if len(sys.argv) > 2 and sys.argv[2].isdecimal():
        WIDTH = int(sys.argv[2])
        if len(sys.argv) > 3 and sys.argv[3].isdecimal():
            HEIGHT = int(sys.argv[3])
        else:
            HEIGHT = int(WIDTH * 3 / 4)


    files = glob.glob("{}/imgs/*.png".format(PATH))

    files.sort()

    if os.path.exists("{}/views".format(PATH)) is False:
        os.mkdir("{}/views".format(PATH))

    ITEMS = ""
    for filepath in files:
        filename = os.path.basename(filepath)

        _id = filename[:9]
        num = int(filename[10])
        name = filename[12:-4]

        if num==0:
            print(filename)
            ITEMS += CODE1_ITEM.format(_id, filename, WIDTH, HEIGHT, _id)
            ITEMS2 = ""
            for k, name in enumerate(NAMES):
                imgname = "{}_{}_{}.png".format(_id, k, name)
                ITEMS2 += CODE2_ITEM.format(imgname, WIDTH, HEIGHT, name)
            HTML = CODE0_HTML.format(ITEMS2)
            f = open("{}/views/{}.html".format(PATH,_id), 'w')
            f.write(HTML)
            f.close()


    HTML = CODE0_HTML.format(ITEMS)
    f = open("{}/index.html".format(PATH), 'w')
    f.write(HTML)
    f.close()



