from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

LOAD_RESULT_PER_PAGE = 50
currys_url = "https://www.currys.co.uk/computing/printers-scanners-and-ink/printers"

apend_query = "?"
if "?" in currys_url:
    apend_query = "&"

all_product_name = []

#open tab and look for number of results
driver.get(currys_url)
page_count_result = int(driver.find_element(By.CSS_SELECTOR, ".page-count-results-shown").get_attribute("data-count"))
page_count = page_count_result
print(f"total_results = {page_count}")
driver.quit()

for items in range(0, page_count, LOAD_RESULT_PER_PAGE):
    driver = webdriver.Chrome()
    #driver.switch_to.new_window('tab')
    driver.get(f"{currys_url}{apend_query}start={items}&sz={LOAD_RESULT_PER_PAGE}")
    product_names_result = driver.find_elements(By.CSS_SELECTOR, ".desktop-only h2.pdp-grid-product-name")
    product_names = [names.text.strip() for names in product_names_result]
    all_product_name.extend(product_names)
    print(product_names)
    driver.close()
    
print(f"total fetched: {len(all_product_name)}")
      

with open("product_names.txt", mode="w") as file:
    for names in all_product_name:
        file.writelines(f"{names}\n")
    




