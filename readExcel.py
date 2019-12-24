import os
import omegafaceTest.getpathInfo
from xlrd import open_workbook
path = omegafaceTest.getpathInfo.get_Path()

class readExcel():
    def get_xls(self,xls_name,sheet_name):
        cls = []
        #获取用例文件路径
        xlspath = os.path.join(path,"testFile",'case',xls_name)
        file = open_workbook(xlspath)# 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)#获得打开Excel的sheet
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls
if __name__ == '__main__':
    print(readExcel().get_xls('userCase1.xlsx','userCase'))
    print(readExcel().get_xls('userCase1.xlsx','userCase')[0][1])
    print(readExcel().get_xls('userCase1.xlsx','userCase')[1][2])