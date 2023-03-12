from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

from time import sleep

import time

inValid_user='invalid_UserName'  #Invalid user name

Valid_user=''  #Enter Valid User

passValid=''  #Enter Valid password

driver=webdriver.Chrome()

driver.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

time.sleep(2)

sign=driver.find_element(By.XPATH,'//*[@id="ap_email"]')

sign.send_keys(inValid_user)

search=driver.find_element(By.XPATH,'//*[@id="continue"]')

search.click()

time.sleep(2)


driver.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

sign=driver.find_element(By.XPATH,'//*[@id="ap_email"]')

sign.send_keys(Valid_user)

time.sleep(2)

search=driver.find_element(By.XPATH,'//*[@id="continue"]')

search.click()

password=driver.find_element(By.XPATH,'//*[@id="ap_password"]')

time.sleep(2)

password.send_keys(passValid)

passin=driver.find_element(By.XPATH,'//*[@id="signInSubmit"]')

passin.click()

searchBox=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')

time.sleep(2)

searchBox.send_keys('microphone')

time.sleep(2)

searchButton=driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')


searchButton.click()

time.sleep(2)

driver.get('https://www.amazon.in/dp/B0B8DF9H2R/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=4ab4daa93f229181f15c908c974bd2a4&content-id=amzn1.sym.f2e74a72-0286-402b-ae7d-4395a990fd1f%3Aamzn1.sym.f2e74a72-0286-402b-ae7d-4395a990fd1f&hsa_cr_id=0&pd_rd_plhdr=t&pd_rd_r=462c4c04-0d90-4805-b77b-0ae185674171&pd_rd_w=le7S4&pd_rd_wg=629kc&qid=1678588952&ref_=sbx_be_s_sparkle_mcd_asin_0_img&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987')


addto=driver.find_element(By.XPATH,'//*[@id="add-to-cart-button"]')

addto.click()

time.sleep(2)

buy=driver.find_element(By.XPATH,'//*[@id="sc-buy-box-ptc-button"]/span/input')

buy.click()


time.sleep(2)

home=driver.find_element(By.XPATH,'//*[@id="banner-image"]/span/span/div')

home.click()

time.sleep(2)

gotocart=driver.find_element(By.XPATH,'//*[@id="a-autoid-1-announce"]')

gotocart.click()

time.sleep(2)

a = ActionChains(driver)

m = driver.find_element(By.XPATH,'//*[@id="nav-link-accountList"]')

a.move_to_element(m).perform()

time.sleep(2)

out=driver.find_element(By.XPATH,'//*[@id="nav-item-signout"]/span')

a.move_to_element(out).click().perform()

time.sleep(500)

driver.close()