import argparse
from bs4 import BeautifulSoup
from selenium import webdriver      
import time

def getHTMLElement(page_url):
    driver = webdriver.Firefox()
    driver.get(page_url)

    while True:
        try:
            loadMoreResults = driver.find_element_by_xpath("//div[@class='mb-load-more-container']//button[@class='mb-load-more mb-btn-secondary-light-bg']")
            time.sleep(2)
            loadMoreResults.click()
            time.sleep(3)
        except Exception as e:
            print(e)
            break

    time.sleep(1)
    html_source = driver.page_source
    # time.sleep(3)
    driver.quit()

    return html_source

def writeToFile(list, filename):
    f = open(filename, "w")

    for i in range(0, len(list)-1):
        f.write(list[i] + " \n")

    f.close()


def fileParser(sourceCode, pdps):
    soup = BeautifulSoup(sourceCode, 'html.parser')

    pdplist = soup('div')

    for tag in pdplist[0]:
        for line in tag:
            string_line = str(line)
            s1 = string_line.split("data-prod-id")

            if len(s1)>1:
                for i in range(0, len(s1)):
                    s2= s1[i].split("\n")

                    if s2[0].startswith("="):
                        pdps.append(s2[0].strip('">').strip('="'))

    return pdps


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--pageurl", help="enter the url", required=True, type=str)
    parser.add_argument("-t", "--textfile", help="Output text file with Filter IDs, in .txt format", required=True, type=str)

    args = parser.parse_args()

    pageurl = args.pageurl
    textfile = args.textfile

    sourceCode = getHTMLElement(pageurl)

    pdps = []

    fileParser(sourceCode, pdps)
    # print(pdps)

    writeToFile(pdps, textfile)