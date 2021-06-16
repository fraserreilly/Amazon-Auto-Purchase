# -*- coding: UTF-8 -*-
import time
import os
import coloredlogs
import logging
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random import randint


load_dotenv()

login = os.environ.get("user")
passw = os.environ.get("passw")
priceLimit = 710.00
acceptedShop = "Dispatched from and sold by Amazon"
itemUrl = "https://www.amazon.co.uk/_itm/dp/ENTERASINHERE"
options = Options()
logger = logging.getLogger("sniper")
coloredlogs.install(level='DEBUG', logger=logger)
options.headless = True
options.add_argument("--log-level=3")

if __name__ == "__main__":
    try:
        driver = webdriver.Chrome("./chromedriver", options=options)
        driver.get(itemUrl)
        driver.find_element_by_id("sp-cc-accept").click()
    except:
        logger.critical("Failed to open browser")
        exit()

    while True:
        while True:
            try:
                shop = driver.find_element_by_id("merchant-info").text

                if acceptedShop not in shop:
                    raise Exception("not Amazon.")
                driver.find_element_by_id("add-to-cart-button").click()
                logger.info("adding card to cart")
                time.sleep(2)
                break
            except:
                logger.info("refreshing")
                time.sleep(randint(1, 2))
                driver.refresh()

        driver.get(
            "https://www.amazon.co.uk/gp/cart/view.html/ref=dp_atch_dss_cart?")
        driver.find_element_by_id("sc-buy-box-ptc-button").click()
        logger.info("card is successfully in cart, logging in")

        try:
            driver.find_element_by_id("ap_email").send_keys(login)
            driver.find_element_by_id("continue").click()
            driver.find_element_by_id("ap_password").send_keys(passw)
            driver.find_element_by_id("signInSubmit").click()
        except:
            logger.info("passing log in if already logged in.")
            pass

        total = driver.find_element_by_css_selector(
            "td.grand-total-price").text
        if float(total.replace("£", "")) > priceLimit:
            logger.warning("Item price is too high.")
            break

        driver.find_element_by_name("placeYourOrder1").click()
        break
    logger.debug("Successfully purchased a card, Congrats!")
