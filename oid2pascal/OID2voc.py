from pascal_voc_io import XML_EXT
from pascal_voc_io import PascalVocWriter
from OID_io import OIDReader
import os.path
import sys

try:
    from PyQt5.QtGui import QImage
except ImportError:
    from PyQt4.QtGui import QImage


imgFolderPath = sys.argv[1]
#print(imgFolderPath)

# Search all yolo annotation (txt files) in this folder
for file in os.listdir(imgFolderPath):
    if file.endswith(".jpg"):
        print("Convert", file)

        annotation_no_txt = os.path.splitext(file)[0]

        imagePath = imgFolderPath + "/" + annotation_no_txt + ".jpg"

        image = QImage()
        image.load(imagePath)
        imageShape = [image.height(), image.width(), 1 if image.isGrayscale() else 3]
        imgFolderName = os.path.basename(imgFolderPath)
        imgFileName = os.path.basename(imagePath)

        writer = PascalVocWriter(imgFolderName, imgFileName, imageShape, localImgPath=imagePath)


        # Read YOLO file
        txtPath = imgFolderPath + "/Label/" + annotation_no_txt+'.txt'
        #print(txtPath)
        tOIDParseReader = OIDReader(txtPath)
        shapes = tOIDParseReader.getShapes()
        #print(shapes)


        for shape in shapes:

            label=shape[0]
            xmin=shape[1]
            ymin=shape[2]
            x_max=shape[3]
            y_max=shape[4]

            writer.addBndBox(xmin, ymin, x_max, y_max, label, 0)

        writer.save(targetFile= imgFolderPath + "/" + annotation_no_txt + ".xml")
