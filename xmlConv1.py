import re

class xmlConv():

    @classmethod
    def xmlConversion(self,path):
        inputStr=""

        with open(path,'r') as todo:
           inputStr= todo.read()
        inputStr=re.sub("\r*\n","@r@n",inputStr)
        print inputStr
print 'working'

if __name__ == '__main__':
    givenPath= raw_input('Please enter your file:')
    xmlConv.xmlConversion(givenPath)
    #xmlConversion(r'D:\Application\samples\scivalAward_excel2xml\QA\001a\501100003921.xml')

