from selenium import webdriver
from selenium.webdriver.common.by import By
import json
browser = webdriver.Chrome()
d = {"version": "1.0"}

def getCPI():
    global d
    global browser
    browser.get("https://tradingeconomics.com/united-kingdom/consumer-price-index-cpi")
    ukCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    ukPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/united-states/consumer-price-index-cpi")
    usCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    usPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/japan/consumer-price-index-cpi")
    jpCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    jpPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/australia/consumer-price-index-cpi")
    audCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    audPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/canada/consumer-price-index-cpi")
    cadCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    cadPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/switzerland/consumer-price-index-cpi")
    chfCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    chfPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/new-zealand/consumer-price-index-cpi")
    nzdCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    nzdPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    d["cpiInfo"] = [{"gbpCurr" : ukCurr, "gbpPrev": ukPrev}, {"jpyCurr" : jpCurr, "jpyPrev": jpPrev}, {"usdCurr" : usCurr, "usdPrev": usPrev}, {"audCurr":audCurr, "audPrev": audPrev}, {"cadCurr":cadCurr, "cadPrev":cadPrev}, {"chfCurr":chfCurr, "chfPrev":chfPrev}, {"nzdCurr":nzdCurr, "nzdPrev":nzdPrev}]


def getIR():
    global d
    global browser
    browser.get("https://tradingeconomics.com/united-kingdom/interest-rate")
    ukCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    ukPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/united-states/interest-rate")
    usCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    usPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/japan/interest-rate")
    jpCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    jpPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/australia/interest-rate")
    audCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    audPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/canada/interest-rate")
    cadCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    cadPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/switzerland/interest-rate")
    chfCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    chfPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/new-zealand/interest-rate")
    nzdCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    nzdPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    d["irInfo"] = [{"gbpCurr" : ukCurr, "gbpPrev": ukPrev}, {"jpyCurr" : jpCurr, "jpyPrev": jpPrev}, {"usdCurr" : usCurr, "usdPrev": usPrev}, {"audCurr":audCurr, "audPrev": audPrev}, {"cadCurr":cadCurr, "cadPrev":cadPrev}, {"chfCurr":chfCurr, "chfPrev":chfPrev}, {"nzdCurr":nzdCurr, "nzdPrev":nzdPrev}]


def getPP():
    global d
    global browser
    browser.get("https://tradingeconomics.com/united-kingdom/producer-prices")
    ukCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    ukPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/united-states/producer-prices")
    usCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    usPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/japan/producer-prices")
    jpCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    jpPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/australia/producer-prices")
    audCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    audPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/canada/producer-prices")
    cadCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    cadPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/switzerland/producer-prices")
    chfCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    chfPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/new-zealand/producer-prices")
    nzdCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    nzdPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    d["ppInfo"] = [{"gbpCurr" : ukCurr, "gbpPrev": ukPrev}, {"jpyCurr" : jpCurr, "jpyPrev": jpPrev}, {"usdCurr" : usCurr, "usdPrev": usPrev}, {"audCurr":audCurr, "audPrev": audPrev}, {"cadCurr":cadCurr, "cadPrev":cadPrev}, {"chfCurr":chfCurr, "chfPrev":chfPrev}, {"nzdCurr":nzdCurr, "nzdPrev":nzdPrev}]


def getRS():
    global d
    global browser
    browser.get("https://tradingeconomics.com/united-kingdom/retail-sales")
    ukCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    ukPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/united-states/retail-sales")
    usCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    usPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/japan/retail-sales")
    jpCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    jpPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/australia/retail-sales")
    audCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    audPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/canada/retail-sales")
    cadCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    cadPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/switzerland/retail-sales")
    chfCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    chfPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/new-zealand/retail-sales")
    nzdCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    nzdPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    d["rsInfo"] = [{"gbpCurr" : ukCurr, "gbpPrev": ukPrev}, {"jpyCurr" : jpCurr, "jpyPrev": jpPrev}, {"usdCurr" : usCurr, "usdPrev": usPrev}, {"audCurr":audCurr, "audPrev": audPrev}, {"cadCurr":cadCurr, "cadPrev":cadPrev}, {"chfCurr":chfCurr, "chfPrev":chfPrev}, {"nzdCurr":nzdCurr, "nzdPrev":nzdPrev}]


def getPMI():
    global d
    global browser
    browser.get("https://tradingeconomics.com/united-kingdom/manufacturing-pmi")
    ukCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    ukPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/united-states/manufacturing-pmi")
    usCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    usPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/japan/manufacturing-pmi")
    jpCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    jpPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/australia/manufacturing-pmi")
    audCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    audPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/canada/manufacturing-pmi")
    cadCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    cadPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/switzerland/manufacturing-pmi")
    chfCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    chfPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/new-zealand/manufacturing-pmi")
    nzdCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    nzdPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    d["pmiInfo"] = [{"gbpCurr" : ukCurr, "gbpPrev": ukPrev}, {"jpyCurr" : jpCurr, "jpyPrev": jpPrev}, {"usdCurr" : usCurr, "usdPrev": usPrev}, {"audCurr":audCurr, "audPrev": audPrev}, {"cadCurr":cadCurr, "cadPrev":cadPrev}, {"chfCurr":chfCurr, "chfPrev":chfPrev}, {"nzdCurr":nzdCurr, "nzdPrev":nzdPrev}]


def getEN():
    global d
    global browser
    browser.get("https://tradingeconomics.com/united-kingdom/employment-rate")
    ukCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    ukPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/united-states/employment-rate")
    usCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    usPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/japan/employment-rate")
    jpCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    jpPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/australia/employment-rate")
    audCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    audPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/canada/employment-rate")
    cadCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    cadPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/switzerland/employment-rate")
    chfCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    chfPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/new-zealand/employment-rate")
    nzdCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    nzdPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    d["enInfo"] = [{"gbpCurr" : ukCurr, "gbpPrev": ukPrev}, {"jpyCurr" : jpCurr, "jpyPrev": jpPrev}, {"usdCurr" : usCurr, "usdPrev": usPrev}, {"audCurr":audCurr, "audPrev": audPrev}, {"cadCurr":cadCurr, "cadPrev":cadPrev}, {"chfCurr":chfCurr, "chfPrev":chfPrev}, {"nzdCurr":nzdCurr, "nzdPrev":nzdPrev}]



def getGDP():
    global d
    global browser
    browser.get("https://tradingeconomics.com/united-kingdom/gdp")
    ukCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    ukPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/united-states/gdp")
    usCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    usPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/japan/gdp")
    jpCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    jpPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/australia/gdp")
    audCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    audPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/canada/gdp")
    cadCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    cadPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/switzerland/gdp")
    chfCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    chfPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    browser.get("https://tradingeconomics.com/new-zealand/gdp")
    nzdCurr = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[2]").text
    nzdPrev = browser.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div[5]/div/table/tbody/tr/td[3]").text
    d["gdpInfo"] = [{"gbpCurr" : ukCurr, "gbpPrev": ukPrev}, {"jpyCurr" : jpCurr, "jpyPrev": jpPrev}, {"usdCurr" : usCurr, "usdPrev": usPrev}, {"audCurr":audCurr, "audPrev": audPrev}, {"cadCurr":cadCurr, "cadPrev":cadPrev}, {"chfCurr":chfCurr, "chfPrev":chfPrev}, {"nzdCurr":nzdCurr, "nzdPrev":nzdPrev}]

getCPI()
getIR()
getPP()
getRS()
getPMI()
getEN()
getGDP()

file1 = open("Y:/Benjamin/MoneyMaking/DayTrading/Forex/forexInfo.txt", "w")
jsond = json.dump(d, file1)
file1.close()
