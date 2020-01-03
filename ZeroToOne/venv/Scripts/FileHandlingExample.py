
import urllib.request
import urllib.error
import sys
import zipfile
import os

urlOfFileName = "https://www.nseindia.com/content/historical/EQUITIES/2015/JUL/cm17JUL2015bhav.csv.zip"
localStorageZipPath = "C:\Git_Repositories\Stack-Skills-Courses\ZeroToOne\Resources\cm17JUL2015bhav.csv.zip"

# Generate a header so that the NSE thinks that this is a human browser, not a bot crawling the site to scrape the data. They don't like that.
hdr = {'Accept': 'test/html, application/xhtml+xml,application/xml;q=0.9, */*q=0.8',
       'Accept-Charset': 'ISO-8859-1;utf-8,q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'Keep-alive',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
webRequest = urllib.request.Request(urlOfFileName, headers = hdr)

try:
    page = urllib.request.urlopen(webRequest)
    content = page.read()
    output = open(localStorageZipPath,"wb") #wb indicated a (written, binary)
    output.write(bytearray(content))
    output.close()

except HTTPError as e:
    print (e.fp.read())
    print ("looks like the file was not downloaded")

################################## Unzipping file ################################################

localExtractFilePath = "C:\Git_Repositories\Stack-Skills-Courses\ZeroToOne\Resources"

if os.path.exists(localStorageZipPath):
    print (localStorageZipPath + " exists, proceeding...")
    listOfFiles = []
    fh = open(localStorageZipPath, 'rb') # rb indicated (read, binary)
    zipFileHandler = zipfile.ZipFile(fh) # This is the file handler for the zipfile library to process the unzipping operation
    for fileName in zipFileHandler.namelist():
        zipFileHandler.extract(fileName, localExtractFilePath)
        listOfFiles.append(localExtractFilePath + "\\" + fileName)
        print ("Extracetd " + fileName + " from the zip file to " + localExtractFilePath)
    print ("in total, we extracted ", str(len(listOfFiles)) + "file(s)")
    fh.close()

################################ CSV Processing ####################################################
################################ Parsing CSV #######################################################
import csv

oneFileName = listOfFiles[0]
lineNum = 0 # setting up the iterator for the parse

listOfLists = [] #setting up the list for the lists of stock indexes and data
with open(oneFileName) as csvfile: # using the with operator, there is no need to opena nd close a file as the "with" operator handels that for us. When the block is closed, the file is closed
    lineReader = csv.reader(csvfile,delimiter=",",quotechar="\"")
    for row in lineReader:
        lineNum = lineNum + 1
        if lineNum == 1:
            print ("Skipping the header line")
            continue
        symbol = row[0]
        close = row[5]
        prevClose = row[7]
        tradedQty = row[9]
        pctChange = float(close)/float(prevClose)-1
        oneResultRow = [symbol,pctChange,float(tradedQty)]
        listOfLists.append(oneResultRow)
        print (symbol, "{:,.1f}".format(float(tradedQty)/1e6) + "M INR", "{:,.1f}".format(pctChange*100) + "%")
        # note the {:,.lf}.format helps with printing comma separated numbers
print ("Done iterating over the file contents - The file is closed now")

################################ Sorting the lists #######################################################
#using lambda functions

listOfListsSortedByPctChange = sorted(listOfLists, key=lambda x:x[1], reverse=True)
#sorting by row 3, Qut
#reversed means descending

################################ Wrinting to excel file #######################################################

import xlsxwriter

excelFileName = "C:\Git_Repositories\Stack-Skills-Courses\ZeroToOne\Resources\OutputStockCsv.xlsx"

workbook = xlsxwriter.Workbook(excelFileName)
worksheet = workbook.add_worksheet("Summary")
worksheet.write_row("A1", ["Top Traded Stocks"])
worksheet.write_row("A2", ["Stock", "% Change", "value traded (INR)"])
for rowNum in range(listOfListsSortedByPctChange.__len__()):
    onerowToWrite = listOfListsSortedByPctChange[rowNum]
    worksheet.write_row("A" + str(rowNum + 3), onerowToWrite)
workbook.close()
