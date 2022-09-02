import matplotlib.pyplot as plt
import xarray as xr
import dask
from tqdm.autonotebook import tqdm
import pandas as pd
import numpy as np
import intake
import geopandas as gpd
#import cmocean



__version__ = "0.1.0"



def shapefilename(domain='lan'):
    # url = "https://daten.gdz.bkg.bund.de/produkte/vg/vg2500/aktuell/vg2500_01-01.gk3.shape.zip"
    #fname = "/mnt/lustre02/work/ch0636/eddy/pool/obs/REGNIE/yearly/d4dc28db585019e49bb8fc14dea93f55-vg2500_01-01.gk3.shape.zip"
    fname = "./data/shapefiles/vg2500_01-01.gk3.shape.zip"
    shp_file = "!vg2500_01-01.gk3.shape/vg2500/vg2500_{}.shp".format(domain)
    return "zip://" + fname + shp_file



def get_hamburg_geodata():
    germany = gpd.read_file(shapefilename()).to_crs("EPSG:4326")
    # take only first element of hamburg multipolgon which is the main city, might be a little nasty
    hamburg = germany[germany.GEN=='Hamburg'].geometry.iloc[0]
    germany.loc[germany['GEN'] == "Hamburg", 'geometry'] = hamburg.geoms[0]
    return germany[germany.GEN=='Hamburg']
