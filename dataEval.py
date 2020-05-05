import json
baseCurrency = input("Enter base currency: ")
quoteCurrency = input("Enter quote currency: ")
json_file = open("Y:/Benjamin/MoneyMaking/DayTrading/Forex/forexInfo.txt", "r")
currency_info = json.load(json_file)
json_file.close()
print(currency_info["cpiInfo"])
baseCurrencyN = -1
baseCurrencyStrCurr = ""
baseCurrencyStrPrev = ""
quoteCurrencyN = -1
quoteCurrencyStrCurr = ""
quoteCurrencyStrPrev = ""
if(baseCurrency=="GBP"):
    baseCurrencyN = 0
    baseCurrencyStrCurr = "gbpCurr"
    baseCurrencyStrPrev = "gbpPrev"
if(baseCurrency=="JPY"):
    baseCurrencyN = 1
    baseCurrencyStrCurr = "jpyCurr"
    baseCurrencyStrPrev = "jpyPrev"
if(baseCurrency=="USD"):
    baseCurrencyN = 2
    baseCurrencyStrCurr = "usdCurr"
    baseCurrencyStrPrev = "usdPrev"
if(baseCurrency=="AUD"):
    baseCurrencyN = 3
    baseCurrencyStrCurr = "audCurr"
    baseCurrencyStrPrev = "audPrev"
if(baseCurrency=="CAD"):
    baseCurrencyN = 4
    baseCurrencyStrCurr = "cadCurr"
    baseCurrencyStrPrev = "cadPrev"
if(baseCurrency=="CHF"):
    baseCurrencyN = 5
    baseCurrencyStrCurr = "chfCurr"
    baseCurrencyStrPrev = "chfPrev"
if(baseCurrency=="NZD"):
    baseCurrencyN = 6
    baseCurrencyStrCurr = "nzdCurr"
    baseCurrencyStrPrev = "nzdPrev"
if(quoteCurrency=="GBP"):
    quoteCurrencyN = 0
    quoteCurrencyStrCurr = "gbpCurr"
    quoteCurrencyStrPrev = "gbpPrev"
if(quoteCurrency=="JPY"):
    quoteCurrencyN = 1
    quoteCurrencyStrCurr = "jpyCurr"
    quoteCurrencyStrPrev = "jpyPrev"
if(quoteCurrency=="USD"):
    quoteCurrencyN = 2
    quoteCurrencyStrCurr = "usdCurr"
    quoteCurrencyStrPrev = "usdPrev"
if(quoteCurrency=="AUD"):
    quoteCurrencyN = 3
    quoteCurrencyStrCurr = "audCurr"
    quoteCurrencyStrPrev = "audPrev"
if(quoteCurrency=="CAD"):
    quoteCurrencyN = 4
    quoteCurrencyStrCurr = "cadCurr"
    quoteCurrencyStrPrev = "cadPrev"
if(quoteCurrency=="CHF"):
    quoteCurrencyN = 5
    quoteCurrencyStrCurr = "chfCurr"
    quoteCurrencyStrPrev = "chfPrev"
if(quoteCurrency=="NZD"):
    quoteCurrencyN = 6
    quoteCurrencyStrCurr = "nzdCurr"
    quoteCurrencyStrPrev = "nzdPrev"

baseCurrCPI = currency_info["cpiInfo"][baseCurrencyN][baseCurrencyStrCurr]
basePrevCPI = currency_info["cpiInfo"][baseCurrencyN][baseCurrencyStrPrev]
baseCurrIR =  currency_info["irInfo"][baseCurrencyN][baseCurrencyStrCurr]
basePrevIR =  currency_info["irInfo"][baseCurrencyN][baseCurrencyStrPrev]
baseCurrPP = currency_info["ppInfo"][baseCurrencyN][baseCurrencyStrCurr]
basePrevPP = currency_info["ppInfo"][baseCurrencyN][baseCurrencyStrPrev]
baseCurrRS =  currency_info["rsInfo"][baseCurrencyN][baseCurrencyStrCurr]
basePrevRS =  currency_info["rsInfo"][baseCurrencyN][baseCurrencyStrPrev]
baseCurrPMI = currency_info["pmiInfo"][baseCurrencyN][baseCurrencyStrCurr]
basePrevPMI = currency_info["pmiInfo"][baseCurrencyN][baseCurrencyStrPrev]
baseCurrEN =  currency_info["enInfo"][baseCurrencyN][baseCurrencyStrCurr]
basePrevEN = currency_info["enInfo"][baseCurrencyN][baseCurrencyStrPrev]
baseCurrGDP = currency_info["gdpInfo"][baseCurrencyN][baseCurrencyStrCurr]
basePrevGDP =  currency_info["gdpInfo"][baseCurrencyN][baseCurrencyStrPrev]

baseCPIChange = float(baseCurrCPI)/float(basePrevCPI)
baseIRChange = float(baseCurrIR)/float(basePrevIR)
basePPChange = float(baseCurrPP)/float(basePrevPP)
baseRSChange = float(baseCurrRS)-float(basePrevRS)
basePMIChange = float(baseCurrPMI)/float(basePrevPMI)
baseENChange = float(baseCurrEN)/float(basePrevEN)
baseGDPChange = float(baseCurrGDP)/float(basePrevGDP)



quoteCurrCPI = currency_info["cpiInfo"][quoteCurrencyN][quoteCurrencyStrCurr]
quotePrevCPI = currency_info["cpiInfo"][quoteCurrencyN][quoteCurrencyStrPrev]
quoteCurrIR =  currency_info["irInfo"][quoteCurrencyN][quoteCurrencyStrCurr]
quotePrevIR =  currency_info["irInfo"][quoteCurrencyN][quoteCurrencyStrPrev]
quoteCurrPP = currency_info["ppInfo"][quoteCurrencyN][quoteCurrencyStrCurr]
quotePrevPP = currency_info["ppInfo"][quoteCurrencyN][quoteCurrencyStrPrev]
quoteCurrRS =  currency_info["rsInfo"][quoteCurrencyN][quoteCurrencyStrCurr]
quotePrevRS =  currency_info["rsInfo"][quoteCurrencyN][quoteCurrencyStrPrev]
quoteCurrPMI = currency_info["pmiInfo"][quoteCurrencyN][quoteCurrencyStrCurr]
quotePrevPMI = currency_info["pmiInfo"][quoteCurrencyN][quoteCurrencyStrPrev]
quoteCurrEN =  currency_info["enInfo"][quoteCurrencyN][quoteCurrencyStrCurr]
quotePrevEN = currency_info["enInfo"][quoteCurrencyN][quoteCurrencyStrPrev]
quoteCurrGDP = currency_info["gdpInfo"][quoteCurrencyN][quoteCurrencyStrCurr]
quotePrevGDP =  currency_info["gdpInfo"][quoteCurrencyN][quoteCurrencyStrPrev]


quoteCPIChange = float(quoteCurrCPI)/float(quotePrevCPI)
quoteIRChange = float(quoteCurrIR)/float(quotePrevIR)
quotePPChange = float(quoteCurrPP)/float(quotePrevPP)
quoteRSChange = float(quoteCurrRS)-float(quotePrevRS)
quotePMIChange = float(quoteCurrPMI)/float(quotePrevPMI)
quoteENChange = float(quoteCurrEN)/float(quotePrevEN)
quoteGDPChange = float(quoteCurrGDP)/float(quotePrevGDP)


print(baseCurrCPI, basePrevCPI, baseCurrIR, basePrevIR, baseCurrPP, basePrevPP, baseCurrRS, basePrevRS, baseCurrPMI, baseCurrEN, basePrevEN, baseCurrGDP, basePrevGDP)
print(quoteCurrCPI, quotePrevCPI, quoteCurrIR, quotePrevIR, quoteCurrPP, quotePrevPP, quoteCurrRS, quotePrevRS, quoteCurrPMI, quoteCurrEN, quotePrevEN, quoteCurrGDP, quotePrevGDP)


print("Base CPI change:", baseCPIChange, "Base IR change:", baseIRChange, "Base PP change:", basePPChange, "Base RS Change:", baseRSChange, "Base PMI Change:", basePMIChange, "Base EN Change:", baseENChange, "Base GDP Change:", baseGDPChange)
print("Quote CPI change:", quoteCPIChange, "Quote IR change:", quoteIRChange, "Quote PP change:", quotePPChange, "Quote RS Change:", quoteRSChange, "Quote PMI Change:", quotePMIChange, "Quote EN Change:", quoteENChange, "Quote GDP Change:", quoteGDPChange)

counterBase = 0
counterQuote = 0
if(baseCPIChange>quoteCPIChange):
    counterBase += 1
else:
    counterQuote += 1
#if(baseIRChange>quoteIRChange):
#    counterBase += 1
#else:
#    counterQuote+=1
if(basePPChange>quotePPChange):
    counterBase+=1
elif(quotePPChange>basePPChange):
    counterQuote+=1
if(baseRSChange>quoteRSChange):
    counterBase+=1
elif(quoteRSChange>baseRSChange):
    counterQuote+=1
if(basePMIChange>quotePMIChange):
    counterBase+=1
elif(quotePMIChange>basePMIChange):
    counterQuote+=1
if(baseENChange>quoteENChange):
    counterBase+=1
elif(quoteENChange>baseENChange):
    counterQuote+=1
if(baseGDPChange>quoteGDPChange):
    counterBase+=1
elif(quoteGDPChange>baseGDPChange):
    counterQuote+=1

if(counterBase>counterQuote):
    print(baseCurrency, "is stronger")
else:
    print(quoteCurrency, "is stronger")
