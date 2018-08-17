from cloudify import ctx
import requests
import json



class SOLO_Config:
  def __init__(self, config):
    self.serverIP = config["server_ip"]
    self.serverPort = str(config["server_port"])
    self.username = config["username"]
    self.password = config["password"]
    self.auth = (self.username,self.password)
    self.server = self.serverIP+":"+self.serverPort
    self.jsonPath = "/overlay/orchestrator/v1"

  def url(self, urlPath):
    return "http://"+self.server+self.jsonPath

class REST:
  @staticmethod
  def post(urlPath, data, solo_config):
    config = SOLO_Config(solo_config) 
    url = config.url(urlPath)
    ctx.logger.info(url)
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    #url = 'http://httpbin.org/post'
    response = requests.post(url, data=data_json, headers=headers, auth=config.auth)
    return response

  @staticmethod
  def delete(urlPath, solo_config):
    config = SOLO_Config(solo_config)
    url = config.url(urlPath)
    ctx.logger.info(url)
    headers = {'Accept': 'application/json'}
    response = requests.post(url, headers=headers, auth=config.auth)
    return response  

  @staticmethod
  def get():
    pass