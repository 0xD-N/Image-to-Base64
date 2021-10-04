import os
import sys
import base64
import time

#base64 encoding
def encode(file, output_path=None):
    
    byte_str = None
    
    #pretty understandable 
    isPath = False
    
    if("\\" in file):
        isPath = True
    
    #image to be read in bytes, then encoded in base64
    try:
        if(isPath):
            with open(file, "rb") as f:
                byte_str = base64.encodebytes(f.read())
        else:
            with open(f"{file}", "rb") as f:
                byte_str = base64.encodebytes(f.read())
                
    except IOError as E:
        print("Invalid File Path")
        return

    try:
        #if a path is specified
        if(output_path != None):
            with open(f"{output_path}\\base64-output.txt", "wb") as f:
                f.write(byte_str)
                p = f"{output_path}\\base64-output.txt"
                
                print(f"\nBase64 has been outputted in {p}")
        
        
        #if not then by default save the base64 text to the location of where this file is running
        else:
            
            with open(f"{os.path.dirname(__file__)}\\base64-output.txt", "wb") as f:
                f.write(byte_str)
                
                p = f"{os.path.dirname(__file__)}\\base64-output.txt"
                print(f"\nBase64 has been outputted in {p}")
                
    except IOError as E:
        print(E)
    

if __name__ == "__main__":

    try:
        if(len(sys.argv) == 3):
            encode(sys.argv[1], sys.argv[2])
        elif(len(sys.argv) == 2):
            encode(sys.argv[1])
    except IndexError as E:
        print("Missing file path argument")
    
    time.sleep(3)
