import requests

#Returns the total cases in germany for every day.

reqUrl = "https://api.corona-zahlen.org/germany/history/cases"

headersList = {
 "Accept": "*/*" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)


#Returns the total deaths in germany for every day.

reqUrl = "https://api.corona-zahlen.org/germany/history/deaths"

headersList = {
 "Accept": "*/*" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)


#Returns statistics per state

reqUrl = "https://api.corona-zahlen.org/states"

headersList = {
 "Accept": "*/*" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)


#Returs statistics about hospitalization per state

reqUrl = "https://api.corona-zahlen.org/states/history/hospitalization"

headersList = {
 "Accept": "*/*" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)


#Returs statistics about recovered per state


reqUrl = "https://api.corona-zahlen.org/states/history/recovered"

headersList = {
 "Accept": "*/*" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

