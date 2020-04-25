#!/usr/bin/python3

# StegaNoMore
'''

This is a very basic script that performs some basic reconnaissance
on a file to determine whether any steganography techniques have
been used to hide files or information.

This work is licensed under the GPLv3.0

# Dependencies:
Packages:
    python3
    strings
    steghide
    fcrackzip
    imagemagick
    stegcracker (Install with "pip3.6 install stegcracker")
Other:
    rockyou.txt must be located in /usr/share/wordlists

'''

# Imports
import sys
import os
import subprocess

# Figure out basic requirements.

# Get Arguments
## Working with Arguments:
##print("Number of arguments", len(sys.argv)) #Prints the number of arguments.
##print("Argument List", str(sys.argv)) #Prints the arguments. sys.argv[0] is the script name.

# Get the Target File, stored as $target
target = sys.argv[1]
# Get the path to the Target File, stored as $targetpath
targetpath = os.path.abspath(target)
# Get the Extension of the file, stored as $extension
filename = os.path.splitext(target)
extension = filename[1]

# List of interesting strings.
interesting_strings = ["pass", "password", "passwd", "admin", "administrator", "root", "user", "username", "secret", "name", "hash", "HTB"] # These are strings that may be interesting to look for, particularly with CTF challenges.

# Check what type of file the target is:
print("")
print("Getting the file type for the target file:")
subprocess.check_call(["file", target])

# Getting contents of the file with `cat`
print("")
print("Getting the contents from the file and writing to output_cat.txt.")
f=open("output_cat.txt","w")
subprocess.check_call(["cat", target], stdout=f)
cat_output = str(subprocess.check_output(["cat", target]))
## Look for interesting strings in the output from `cat`.
print("")
for x in interesting_strings:
    if x in str(cat_output):
        print("     Possible interesting string in file contents: " + x)

# Testing the file with `strings`
print("")
print("Getting the human-readable strings from the file and writing to output_strings.txt.")
f=open("output_strings.txt","w")
subprocess.check_call(["strings", target], stdout=f)
strings_output = str(subprocess.check_output(["strings", target]))
## Look for interesting strings in the output from `strings`.
print("")
for x in interesting_strings:
    if x in str(strings_output):
        print("     Possible interesting string in human readable strings: " + x)

# Image EXIF Data Extraction
exif_extensions = [".jpg", ".JPG", ".jpg", ".JPEG", ".raw", ".RAW", ".png", ".PNG"]
if extension in exif_extensions:
    print("")
    print("Extracting image metadata.")
    f = open("output_exif_data.txt", "w")
    subprocess.check_call(["identify", "-verbose", target], stdout=f)

# Checking for hidden files with steghide
# ## Check for hidden files
# ## If the file is password-protected, commence bruteforcing using rockyou.txt
steghide_extensions = [".jpg", ".JPG", ".jpeg", ".JPEG", ".bmp", ".BMP", ".wav", ".WAV", ".au", ".AU"] # These are the extensions supported by steghide, so if we have a file with one of these extensions, we will see if steghide has been used to hide information.
if extension in steghide_extensions:
    print("")
    print("File extension is a supported steghide extension. Loading Stegcracker.")
    subprocess.check_call(["stegcracker", target])

# Compressed File Testing
compressed_extensions = [".zip", ".ZIP", ".gzip", ".GZIP"]
### Test whether the file is encrypted
encrypted_zip_test = str(subprocess.check_output(["7z","l","-slt",target]))
if "ZipCrypto" in encrypted_zip_test:
    print("")
    print("The compressed file is encrypted.")
    print("Brute forcing the file using Fcrackzip and Rockyou.txt")
    subprocess.check_call(["fcrackzip", "-u", "-D", "-p", "/usr/share/wordlists/rockyou.txt", target])
else:
    print("The compressed file is not encryped.")
    print("Extracting the file.")
    subprocess.check_call(["unzip", target])
