import argparse
from bs4 import BeautifulSoup
import urllib


def writeToFile(list, filename):
    f = open(filename, "w")

    for i in range(0, len(list)):
        f.write(list[i] + " \n")

    f.close()


def fileParser(filename, pdps):
    file = open(filename, "r").read()

    soup = BeautifulSoup(file, 'html.parser')

    pdplist = soup('div')

    for tag in pdplist[0]:
        for line in tag:
            string_line = str(line)
            s1 = string_line.split("data-prod-id")

            if len(s1)>1:
                for i in range(0, len(s1)-1):
                    s2= s1[i].split("\n")

                    if s2[0].startswith("="):
                        pdps.append(s2[0].strip('">').strip('="'))

    return pdps


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--htmlfile", help="enter the html file", required=True, type=str)
    parser.add_argument("-t", "--textfile", help="Output text file with Filter IDs, in .txt format", required=True, type=str)

    args = parser.parse_args()

    htmlFile = args.htmlfile
    textfile = args.textfile

    # htmlFile = "/home/pratik/projects/MTB/wri.html"
    pdps = []

    fileParser(htmlFile, pdps)
    print(pdps)

    # print(type(textfile))
    writeToFile(pdps, textfile)
