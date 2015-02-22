import os
import sys
import re
from urllib import urlencode

"""
This script gets the stock symbol from the .csv files downloaded from industy
section of http://www.nasdaq.com/screening/company-list.aspx

It extracts the first element(stock symbol) of each line in the .csv files in a
directory and creats a text file called Symbols.txt

This script could be reworked to take advantage of Python's csv module.

@baldwin Browne
Feb 21, 2014
"""

def main(argv):

    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".csv")]
    ##print(files)
    wfile = open('Symbols.txt', 'w')
    for f in files:
##        print(f)
        try:
            rfile = open(f, 'r')
        except:
            print('No such file')
            sys.exit()
        #industry = argv[1].split('.')
        #wfile = open('Symbols.txt', 'w')
        line = rfile.readline();
        while line != '':
            procLine = line.split(',')
            if (procLine[0] == 'Symbol'):
                line = rfile.readline
            else:
                symbol = removeQuote(procLine[0])
                symbol = urlEncode(symbol)
                symbol = symbol.strip()
                wfile.write(symbol + '\n')
                line = rfile.readline()
    
        rfile.close()
    wfile.close()

def removeQuote(s):
    if (s[0] == s[-1])and s.startswith(("'", '"')):
        return s[1:-1]
    return s

def urlEncode(s):
    s = s.replace("^", "%5E")
    s = s.replace("@", "%40")
    s = s.replace("&", "%26")
    s = s.replace("$", "%24")
    s = s.replace("+", "%2B")
    s = s.replace(",", "%2C")
    s = s.replace("/", "%2F")
    s = s.replace(":", "%3A")
    s = s.replace(";", "%3B")
    s = s.replace("=", "%3D")
    s = s.replace("?", "%3F")
    return s


if __name__ == "__main__":
    main(sys.argv)
