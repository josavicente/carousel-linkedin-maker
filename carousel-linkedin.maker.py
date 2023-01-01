import glob
import json
import os
from PyPDF2 import PdfMerger

CONFIG_FILE_NAME = "config-carousel-linkedin-maker.json"
ORIGIN_FOLDER_FIELD = "origin_folder"
FINAL_FOLDER_FIELD = "final_folder"

class CarouselLinkedinMaker():
    """# Automatization of merging PDF's from a input folder"""
    config_file_data = ""
    input_folder = ""
    output_folder = ""

    def __init__(self):
        # super(CarouselLinkedinMaker, self).__init__("josavicentedev")
        self.open_config_data_file()
        self.check_folder_input()
        self.check_folder_output()
        self.merge_pdfs()

    def open_config_data_file(self):
        """# Open config data"""
        config_file = open(CONFIG_FILE_NAME)
        self.config_file_data = json.load(config_file)

    def check_folder_input(self):
        """# Checking existence of input folder and/or create"""
        self.input_folder = self.check_folfer(self.config_file_data[ORIGIN_FOLDER_FIELD])

    def check_folder_output(self):
        """# Checking existence of output folder and/or create"""
        self.output_folder =  self.check_folfer(self.config_file_data[FINAL_FOLDER_FIELD])

    def check_folfer(self, folder_name):
        """# Checking existence fo given folder and/or create"""
        check_folder = os.path.isdir(folder_name)
        if not check_folder:
            os.makedirs(folder_name)
            print("created folder : ", folder_name)
        else:
            print(folder_name, "folder already exists.")
            return folder_name

    def merge_pdfs(self):
        """# Merge PDF's"""
        print(self.input_folder)
        list_of_pfds = [f for f in glob.glob(self.input_folder + "/*.pdf")]
        list_of_pfds.sort()
        print(list_of_pfds)
        self.group_by_name(list_of_pfds)
        merger = PdfMerger()

        for pdf in list_of_pfds:
            merger.append(pdf)

        merger.write(self.output_folder + "/result.pdf")
        merger.close()
    def group_by_name(self, list_of_pdfs):
        # A list comprehension. It is a way to create a list from another list.
        list_splitted = [element.lower().replace('/', ' ').replace('.', ' ').split() for element in list_of_pdfs]
        print(list_splitted)
        file_name_set = set()
        for pdf in list_splitted:
            file_name = ''.join((x for x in pdf[1] if not x.isdigit()))
            file_name_set.add(file_name)
if __name__ == "__main__":
    CarouselLinkedinMaker()
