
import os
import zipfile
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(100000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['szrap.zip.000.NOTES', 'szrap.zip.001.NOTES', 'szrap.zip.002.NOTES', 'szrap.zip.003.NOTES', 'szrap.zip.004.NOTES', 'szrap.zip.005.NOTES', 'szrap.zip.006.NOTES', 'szrap.zip.007.NOTES', 'szrap.zip.008.NOTES', 'szrap.zip.009.NOTES', 'szrap.zip.010.NOTES', 'szrap.zip.011.NOTES', 'szrap.zip.012.NOTES', 'szrap.zip.013.NOTES', 'szrap.zip.014.NOTES', 'szrap.zip.015.NOTES', 'szrap.zip.016.NOTES', 'szrap.zip.017.NOTES', 'szrap.zip.018.NOTES', 'szrap.zip.019.NOTES', 'szrap.zip.020.NOTES', 'szrap.zip.021.NOTES', 'szrap.zip.022.NOTES', 'szrap.zip.023.NOTES', 'szrap.zip.024.NOTES', 'szrap.zip.025.NOTES', 'szrap.zip.026.NOTES', 'szrap.zip.027.NOTES', 'szrap.zip.028.NOTES', 'szrap.zip.029.NOTES', 'szrap.zip.030.NOTES', 'szrap.zip.031.NOTES', 'szrap.zip.032.NOTES', 'szrap.zip.033.NOTES', 'szrap.zip.034.NOTES', 'szrap.zip.035.NOTES', 'szrap.zip.036.NOTES', 'szrap.zip.037.NOTES', 'szrap.zip.038.NOTES', 'szrap.zip.039.NOTES', 'szrap.zip.040.NOTES', 'szrap.zip.041.NOTES', 'szrap.zip.042.NOTES', 'szrap.zip.043.NOTES', 'szrap.zip.044.NOTES', 'szrap.zip.045.NOTES', 'szrap.zip.046.NOTES', 'szrap.zip.047.NOTES', 'szrap.zip.048.NOTES', 'szrap.zip.049.NOTES', 'szrap.zip.050.NOTES', 'szrap.zip.051.NOTES', 'szrap.zip.052.NOTES'],'szrap.zip')
print('unziping')
with zipfile.ZipFile('szrap.zip', 'r') as zip_ref:
    zip_ref.extractall('szrap')
os.remove('szrap.zip')
os.remove('join.py')
