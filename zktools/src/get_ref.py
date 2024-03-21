import requests
import os
import gzip
from .get_chr import download_chr
from ..constants.ensemble import *

#from ensemble import GRCh, GRCm, human, mouse


def download_ref_ensemble(build:int=38,
                        release:int=109,
                        species:str="human",
                        chr_folder:os.PathLike="./",
                        file_name:str='genome.fa.gz',
                        unzip:bool=True,
                        remove_gz:bool=False)->None:
    
    if species in human:
        url_chr = GRCh.replace('{release}',f'{release}').replace('{build}',f'{build}')
        
    elif species in mouse:
        url_chr = GRCm.replace('{release}',f'{release}').replace('{build}',f'{build}')


    url_chr = url_chr.replace('chromosome.{chr}','primary_assembly')
    download_chr(chr_folder=chr_folder,
                 url_chr=url_chr,
                 unzip=unzip,
                 file_name=file_name,
                 remove_gz=remove_gz)
    return

def main():
    funcs = {"ensembl":download_ref_ensemble,
            "t2t:":"download_ref_t2t",}
    return