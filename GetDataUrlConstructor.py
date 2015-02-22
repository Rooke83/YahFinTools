import urllib3

"""
This script contructs URLs to pull information from the Yahoo Finance API.
It relies on the file Symbols.txt which contains a stock symbol on each new line.
Symbols.txt can be constructed using GetSymbolFromCSVv2.py with information
downloaded from the nasdaq.com website.

@Baldwin Browne
Feb 21, 2015
"""

def main():
    file = open('Symbols.txt', 'r')
    startUrl = 'http://download.finance.yahoo.com/d/quotes.csv?s='
    endUrl = '&f=sa2ee7e8e9jkj1m3m4p5p6rr5r6r7s7yk5j6p'
    symString = ''
    urlList = []
    symList = []
    
    line = file.readline()
    while line != '':
        symList.append(line.strip())
        line = file.readline()
    x = 1 
    for sym in symList:
        symString += sym + ','
        x += 1
        if(x%50==0):
            finalUrl = startUrl + symString + endUrl
            urlList.append(finalUrl)
            symString = ''
    finalUrl = startUrl+symString + endUrl
    urlList.append(finalUrl)
    file.close()

    http = urllib3.PoolManager()
    with open('fetchedData.csv', 'wb') as f:
        for url in urlList:
            print(url)
            r = http.request('GET', url)
            f.write(r.data)

    r.release_conn()
        
    
main()
