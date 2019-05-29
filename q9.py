#from tabulate import *

def AnalaysisArticle(positive, negative, neutral, fullword, dic):
    freq = getFreq(positive, negative, neutral, fullword, dic)
    percent = getPercent(freq["Positive"], freq["Negative"], freq["Neutral"], freq["Full"])
    results = {"freq": freq, "percent": percent}
    return results



def AnalysisFreq(percent):
    print ("Article is", max(percent, key=lambda i: percent[i]))

def getPercent(pos, neg, neut, full):
    ratio = 100/full
    percent = {
    "Positive": pos*ratio,
    "Negative": neg*ratio,
    "Neutral": neut*ratio

    }
    return percent

def getFreq(pos, neg, neut, full, dic):
    pos = 0
    neg = 0
    neut = 0
    full = 0

    for i in pos:
        pos += dic[i]
    for i in neg:
        neg += dic[i]
    for i in neut:
        neut += dic[i]
    for i in dic.keys():
        full += dic[i]
    freq = {
    "Positive": pos, "Negative": neg, "Neutral": neut, "Full": full
    }
    return freq

def get_dic(keys, ori_dic):
    new_dic = {}
    for i in keys:
        new_dic[i] = ori_dic[i]
    return new_dic

def printAnalysis(results):
    table_header = ["Type","Total Words", "Percentage (%)"]
    table_body = [
    ["Positive", results["freq"]["Positive"], "%.f" % results["percent"]["Positive"]],
    ["Negative", results["freq"]["Negative"], "%.f" % results["percent"]["Negative"]],
    ["Neutral", results["freq"]["Neutral"], "%.f" % results["percent"]["Neutral"]]
    ]

    print (tabulate(table_body, table_header), "\n\nTotal Words: ", results["freq"]["Full"])
    AnalysisFreq(results["percent"])


    if pos > neg:
        print("The country has positive sentiment. ")

    elif neg > pos:
        print("The country has negative sentiment. ")

    elif neg == pos:
        print("The country has natural sentiment.")
