# QR Code Encoder / Decoder
# Authors: Oliver Johns(tenthdoctor@linuxmail.org), Jacob Foster(jacobfoster135@gmail.com)
# This software is property of Oliver Johns and Jacob Foster, all rights reserved.
# License: no license atm
# Support: No support atm

# Library Imports
import datetime
import os
import qrcode as qr
from pyzbar.pyzbar import decode
from PIL import Image
from colorama import Fore, Back, Style

# misc vars
n = datetime.datetime.now()
date = n.strftime("%d-%m-%Y")
exportParent = "export/"
importParent = "import/"
time = n.strftime("%H-%M-%S" + ".png")
txtTime = n.strftime("%H-%M-%S" + ".txt")
exPath = os.path.join(exportParent, date)
imPath = os.path.join(importParent, date)

# functions
def directory():
  # export folder
  if os.path.exists("export") == False:
    os.mkdir("export")
  if os.path.exists("import") == False:
    os.mkdir("import")
  menu()

  

def encoder():
  global path, time
  encodee = input("Enter the data you would like to encode: ")
  exported = qr.make(encodee)
  exmd()
  path2 = os.path.join(exPath, time)
  exported.save(path2)
  print("QR Code Exported to " + path2)
  return True
  # THIS FUNCTION IS WORKING AS INTENDED, DO NOT MESS WITH IT.

def decoder():
  global txtTime, imPath
  if os.path.exists(imPath):
    print("Dated folder detected, skipping step...")
  else:
    print("Dated folder not detected, creating...")
    immd()
  decodee = input("Enter the file name of the QR code you would like to decode: ")
  decodeePath = os.path.join(imPath, decodee)
  if os.path.exists(decodeePath):
    print("Detected file. Decoding...")
    decodee = decode(Image.open(decodeePath))
    decoded = decodee[0].data.decode("utf-8")
    print(" ")
    print(Fore.GREEN + "Data decoded successfully!")
    print("Data: " + decoded)
    print(" ")
    opt2 = input(Fore.GREEN + "Export to TXT? (Y/N): " + Fore.WHITE)
    opt2 = opt2.lower()
    if opt2 == "y":
      print("Exporting to TXT...")
      txt = open(os.path.join(imPath, txtTime), "w")
      txt.write(decoded)
      txt.close()
      print(Fore.GREEN + "Exported to TXT!" + Fore.WHITE)
      return True
    if opt2 == "n":
      print("Operation Cancelled.")
      return True
  else:
    print("File not found, returning to menu...")
    menu()
    
    

def exmd():
  global n, date, path2, path, parent
  if os.path.exists(exPath):
    print("Directory already exists. Skipping...")
    return True
  else:
    print("Dated directory does not exist, creating...")
    os.mkdir(exPath)
    print("Directory created at: " + exPath)
    return True
    # THIS FUNCTION IS WORKING AS INTENDED, DO NOT MESS WITH IT.

def immd():
  global imPath
  os.mkdir(imPath)
  print("Directory created at: " + imPath)
  return True
  # THIS FUNCTION IS WORKING AS INTENTED, DO NOT MESS WITH IT.
  
def menu():
  print("Welcome to the TenthSystemsUK QR Code Encooder/Decoder!")
  print("This script is currently in development, please be patient.")
  print("This script is also property of TenthSystemsUK, all rights reserved.")
  print("Please select an option from the list below:")
  print("1) Encode a QR Code")
  print("2) Decode a QR Code")
  print("3) Exit Software")
  opt = input("Option: ")
  if opt == "1":
    print(" ")
    encoder()
  elif opt == "2":
    print(" ")
    decoder()
  elif opt == "3":
    print("This feature is currently in development.")
    menu()
    print(" ")
  else:
    print(" ")
    print("Invalid option, please try again.")
    menu()
menu()