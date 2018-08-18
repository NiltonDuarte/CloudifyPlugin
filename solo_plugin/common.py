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
    self.server = "{}:{}".format(self.serverIP,self.serverPort)
    self.jsonPath = "/overlay/orchestrator/v1"

  def url(self, urlPath):
    return "http://{}{}{}".format(self.server,self.jsonPath,urlPath)

class REST:
  @staticmethod
  def post(urlPath, data, solo_config):
    config = SOLO_Config(solo_config) 
    url = config.url(urlPath)
    ctx.logger.info(url)
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    #url = 'http://httpbin.org/post'
    response = requests.post(url, data=data_json, headers=headers, auth=config.auth)
    return response

  @staticmethod
  def delete(urlPath, solo_config):
    config = SOLO_Config(solo_config)
    url = config.url(urlPath)
    ctx.logger.info(url)
    headers = {'Accept': 'application/json'}
    response = requests.delete(url, headers=headers, auth=config.auth)
    return response  

  @staticmethod
  def get():
    pass
  """
  getURL = restURL + "/vnet/network/" + vNetName
  reqCode = -1
  max_count = 20
  count = 0
  while not reqCode == 200:
    if count > max_count:
      #throw
      return
    count += 1
    time.sleep(0.2)
    response = requests.get(getURL, headers=headers, auth=('karaf','karaf'))
    reqCode = response.status_code
    ctx.logger.info("req_status_code:"+str(reqCode))
  """