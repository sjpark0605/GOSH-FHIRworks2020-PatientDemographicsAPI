import matplotlib
import matplotlib.pyplot as plot
import base64
import json
import os
from fhir_parser import FHIR
from collections import OrderedDict

matplotlib.use('agg')

fhir = FHIR()
patients = fhir.get_all_patients()
possibleSelection = ["language", "gender", "year_group", "marital", "country", "distribution", "cumulative"]

def getLanguageGroupMap():
    languages = {}
    for patient in patients:
        for language in patient.communications.languages:
            languages.update({language: languages.get(language, 0) + 1})

    return languages

def getGenderGroupMap():
    genders = {}
    for patient in patients:
        currentKey = patient.gender.capitalize()
        genders.update({currentKey: genders.get(currentKey, 0) + 1})

    return genders

def getYearGroupMap():
    years = {}
    for patient in patients:
        currentKey = (str (int (patient.birth_date.year / 10) * 10) + "s")
        years.update({currentKey: years.get(currentKey, 0) + 1})

    sortedYears = OrderedDict(sorted(years.items()))

    return sortedYears

def getMaritalGroupMap():
    maritals = {}
    for patient in patients:
        currentKey = (str (patient.marital_status)).strip()
        maritals.update({currentKey: maritals.get(currentKey, 0) + 1})

    return maritals

def getCountryGroupMap():
    countries = {}
    for patient in patients:
        for address in patient.addresses:
            currentKey = address.country
            countries.update({currentKey: countries.get(currentKey, 0) + 1})
    
    return countries

def getAgeDistributionMap():
    ages = {}
    for patient in patients:
        currentKey = (int (patient.age()))
        ages.update({currentKey: ages.get(currentKey, 0) + 1})

    sortedAges = OrderedDict(sorted(ages.items()))

    return sortedAges

def getCumulativeAgeMap():
    sortedAgeMap =  getAgeDistributionMap()
    cumulativePop = {}
    currPop = 0

    for key in sortedAgeMap:
        currPop = currPop + sortedAgeMap.get(key)
        cumulativePop.update({key: currPop})

    return cumulativePop

def mapSelector(selection):
    targetMap = {}
    if (selection == "language"):
        targetMap = getLanguageGroupMap()
    elif (selection == "gender"):
        targetMap = getGenderGroupMap()
    elif (selection == "year_group"):
        targetMap = getYearGroupMap()
    elif (selection == "marital"):
        targetMap = getMaritalGroupMap()
    elif (selection == "country"):
        targetMap = getCountryGroupMap()  
    elif (selection == "distribution"):
        targetMap = getAgeDistributionMap()
    elif (selection == "cumulative"):
        targetMap = getCumulativeAgeMap()
    return targetMap

def fileHandler():
    if os.path.isfile('result.png'): 
        os.remove('result.png')

def plotGraph(map):
    plot.clf()
    plot.bar(range(len(map)), list(map.values()), align='center')
    plot.xticks(range(len(map)), list(map.keys()), rotation='vertical')
    plot.subplots_adjust(bottom=0.30, top=0.99)
    return plot

def plotDescriptiveGraph(map): 
    plot.clf()
    x = [k for k in map]
    y = [v for v in map.values()]
    plot.xlabel("Age")
    plot.ylabel("Population")
    plot.plot(x, y)
    return plot

def constructTargetGraph(selection):
    targetMap = mapSelector(selection)
    
    graphResult = None

    if (selection == "distribution" or selection == "cumulative"):
        graphResult = plotDescriptiveGraph(targetMap)
    else:
        graphResult = plotGraph(targetMap)

    fileHandler()
    graphResult.savefig("result.png")
    encoded = base64.b64encode(open("result.png", "rb").read())
    return encoded

def constructTargetJson(selection):
    targetMap = mapSelector(selection)
    
    jsonResult = json.dumps(targetMap)
    return jsonResult 