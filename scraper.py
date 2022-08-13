from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import os


risk_factor = {
    "high" : ["Acrylates Copolymer", "Acrylates Crosspolymer", "Butylene", "Carbomer", "Dimethicone", "Ethylene",
    "Methacrylate Copolymer", "Methacrylate Crosspolymer", "Methyl Methacrylate Copolymer", "Methyl Methacrylate Crosspolymer",
    "Nylon", "Polyacrylamide", "Polyacrylate", "Polypropylene", "Polyurethane", "Polyvinyl", "Propylene Copolymer",
    "PVP", "Styrene Copolymer", "Tetrafluoroethylene", "Vinyl Acetate Copolymer", "VP/VA Copolymer"],

    "medium" : ["Acrylamidopropyltrimonium Chloride/​Acrylamide Copolymer", "Acrylates/​Palmeth-25 Acrylate Copolymer", 
    "Acrylates/​T-Butylacrylamide Copolymer", "Acrylic Acid/​VP Crosspolymer", "Methyl Methacrylate Crosspolymer", 
    "Adipic Acid/​Neopentyl Glycol Crosspolymer", "Adipic Acid/​Neopentyl Glycol/​Trimellitic Anhydride Copolymer", 
    "Almond Oil PEG-6 Esters", "Aminopropyl Dimethicone", "Ammonium Acryloyldimethyltaurate/​VP Copolymer", 
    "Ammonium Polyacryloyldimethyl Taurate", "Amodimethicone", "Amodimethicone/​Morpholinomethyl Silsesquioxane Copolymer", 
    "Amodimethicone/​Silsesquioxane Copolymer", "Apricot Kernel Oil PEG-6 Esters", "Bis-Aminopropyl Dimethicone", "Bis-Butyldimethicone Polyglyceryl-3", 
    "Bis-C16-20 Isoalkoxy Tmhdi/​PEG-90 Copolymer", "Bis-Cetearyl Amodimethicone", "Bis-Diglyceryl Polyacyladipate-1", "Bis-Diglyceryl Polyacyladipate-2",
    "Bis-Diisopropanolamino-Pg-Propyl Dimethicone/​Bis-Isobutyl PEG-14 Copolymer"]
}

'''
os.environ['PATH'] += r':/opt/homebrew/bin/chromedriver'
driver = webdriver.Chrome(executable_path=os.environ['PATH'], service_args=["--verbose", "--log-path=:/qc1.log"])
driver = webdriver.Chrome()
'''
url = "https://incidecoder.com/products/"

prName = input("Enter your product: ")
prName = prName.split()

for x in range(len(prName) -1):
    url+=prName[x]
    url+="-"

url += str(prName[-1])
#print(url)

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
ingredients = soup.find_all('a', class_ = "ingred-link black")


temp = ""
high = []
med = []

for ingredient in ingredients:
    if ingredient.text in risk_factor["high"] and ingredient.text not in high:
        high.append(ingredient.text)
    elif ingredient.text in risk_factor["medium"] and ingredient.text not in med:
        med.append(ingredient.text)

if len(high) > 0:
    print("Your product contains ingredients classified as highly susceptible to microplastic contamination")
    print("Here are the ingredients that have been flagged as high risk:")
    for x in high:
        print(x)
if len(med) > 0:
    print("Your product contains ingredients classified as susceptible to microplastic contamination")
    print("Here are the ingredients that have been flagged as medium risk:")
    for x in med:
        print(x)
#print(ingredients.text)
