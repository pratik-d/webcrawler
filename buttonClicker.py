from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test(website):    
	driver = webdriver.Firefox()
	driver.get(website)
	# python_button = driver.find_elements_by_class_name("mb-load-more mb-btn-secondary-light-bg")

	a = "mb-load-more-container"
	python_button = driver.find_elements_by_xpath("//div[@class='mb-load-more-container']//button[@class='mb-load-more mb-btn-secondary-light-bg']")

	if python_button.is_displayed():
		print("Button displayed")
	else:
		print("nope")

	# while python_button.is_displayed():
	# 	python_button.click()
	# 	print("\n ############## Button clicked ############ \n")


	driver.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--website", help="enter the html file", required=True, type=str)

    args = parser.parse_args()

    website = args.website

    test(website)