#Group svg from klatexfromula

from bs4 import BeautifulSoup

def readandsoupsvg():
    infile = open("autom_trasgr.svg","r")
    contents = infile.read()
    soup = BeautifulSoup(contents, "lxml-xml")
    return soup

def group(soup):
    soup.find(id="page1").wrap(soup.new_tag("g"))

def export(soup, exportfilename):
    svgmoved = open("%s.svg" %(exportfilename), "w+")
    svgmoved.write(soup.prettify())
    svgmoved.close()
    
    
def main():   
    soup = readandsoupsvg()
    group(soup)
    
    exportfilename = 'tgr'
    export(soup, exportfilename)

main()
