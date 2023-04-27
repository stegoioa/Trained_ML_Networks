
#Use the Split_Image Section for Segmenting Images

!pip install split-image

!split-image /content/drive/MyDrive/projects/diploma/buildingheights/22.jpg 10 10

#Use the Stich_Image Section for Stich Images Back Together

git clone https://github.com/adamancer/stitch2d
python -m pip install -U scikit-image
pip install stich2D
from stitch2d import S
from stitch2d import Mosaic

mosaic = Mosaic("/path/to/tiles")

mosaic = StructuredMosaic(
    "/path/to/tiles",
    dim=15,                  # number of tiles in primary axis
    origin="upper left",     # position of first tile
    direction="horizontal",  # primary axis (i.e., the direction to traverse first)
    pattern="snake"          # snake or raster
  )
