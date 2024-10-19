import pytesseract
import pyPDF2
from pdf2image import convert_from_path
import os
import re
import glob
import io 
import pandas as pd


#define paths 


#path to where tesseract is downloaded 
pytesseract.pytesseract.tesseract_cmd = '/Users/nusratalam/anaconda3/lib/python3.11/site-packages' 

#path to poppler 


pytesseract.pytesseract.tesseract_cmd = 'directory'

def pdf_converter():
    #store all information of a pdf into an image then make that image searchable 
    pages =  