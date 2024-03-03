import os

class oop:

    def __init__(self):
        self.mainDir = 'C:\\Users\\12345\\Desktop\\temchik\\temp'
        self.currentDir = 'C:\\Users\\12345\\Desktop\\temchik\\temp'
        os.chdir(self.mainDir)

    def createDir(self, dirName):
        os.mkdir(f'"{self.currentDir}\\{dirName}"')

    def changeDir(self, dirName):
        os.chdir(f'{self.currentDir}\\{dirName}')
        self.currentDir = os.getcwd()

    def removeDir(self, dirName):
        os.rmdir(self.currentDir + "\\" + dirName) 
    
    def openFile(self, fileName):
        os.system(f'"{self.currentDir}\\{fileName}"')

    def checkDir(self, dirName='', main = False):
        if main:
            list_of_dirs = os.listdir(self.mainDir + '\\' + dirName)
        else:
            list_of_dirs = os.listdir(self.currentDir + '\\' + dirName)
        return list_of_dirs

    def resetDir(self):
        os.chdir(self.mainDir)
        self.currentDir = os.getcwd()

#bt = oop()
#bt.changedDir('1 курс')
#bt.openFile('т1 метод.docx')
#bt.openFile('Т1 Л2 СМССН.pptx')
#print(bt.checkDir('Взводы'))
#bt.changedDir('Взводы')


