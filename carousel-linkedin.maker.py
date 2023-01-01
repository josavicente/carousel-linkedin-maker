import glob
import json
import os
from PyPDF2 import PdfMerger

CONFIG_FILE_NAME = "config-carousel-linkedin-maker.json"
ORIGIN_FOLDER_FIELD = "origin_folder"
FINAL_FOLDER_FIELD = "final_folder"
    
class CarouselLinkedinMaker():
    
    configFileData = ""
    input_folder = ""
    output_folder = ""
    
    def __init__(self):
        # super(CarouselLinkedinMaker, self).__init__("josavicentedev")
        self.openConfigDataFile()
        self.checkFolderInput()
        self.checkFolderOutput()
        self.mergePDFs()
        
    def openConfigDataFile(self):
        configFile = open(CONFIG_FILE_NAME)
        self.configFileData = json.load(configFile)
    
    def checkFolderInput(self):
        self.input_folder = self.checkFolder(self.configFileData[ORIGIN_FOLDER_FIELD])
        
    def checkFolderOutput(self):
        self.output_folder =  self.checkFolder(self.configFileData[FINAL_FOLDER_FIELD])
        
    
    def checkFolder(self, folder_name):
        CHECK_FOLDER = os.path.isdir(folder_name)
        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(folder_name)
            print("created folder : ", folder_name)

        else:
            print(folder_name, "folder already exists.")
            return folder_name
        
    def mergePDFs(self):
        print(self.input_folder)
        listOfPdfs = [f for f in glob.glob(self.input_folder + "/*.pdf")]
        listOfPdfs.sort
        print(listOfPdfs)
        merger = PdfMerger()

        for pdf in listOfPdfs:
            merger.append(pdf)

        merger.write(self.output_folder + "/result.pdf")
        merger.close()

if __name__ == "__main__":
    CarouselLinkedinMaker()