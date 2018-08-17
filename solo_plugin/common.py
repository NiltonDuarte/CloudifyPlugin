from cloudify import ctx
import requests
import json

jsonPath = "/overlay/orchestrator/v1"

def post(urlPath, data, serverIP, serverPort, username, password):
  restURL = "http://"+serverIP+":"+str(serverPort)+jsonPath
  url = restURL + urlPath
  ctx.logger.info(url)
  data_json = json.dumps(data)
  headers = {'Content-type': 'application/json'}
  #url = 'http://httpbin.org/post'
  response = requests.post(url, data=data_json, headers=headers, auth=(username,password))
  return response

def delete(urlPath, serverIP, serverPort, username, password):
  restURL = "http://"+serverIP+":"+str(serverPort)+jsonPath
  url = restURL + urlPath
  ctx.logger.info(url)
  headers = {'Accept': 'application/json'}
  response = requests.post(url, headers=headers, auth=(username,password))
  return response  