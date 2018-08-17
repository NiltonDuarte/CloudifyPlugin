# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation
from common import *

@operation
def create(**kwargs):
  ctx.logger.info("port_create")

  virtualPortNumber = str(ctx.node.properties["virtualPortNumber"])
  physicalPortName = str(ctx.node.properties["physicalPortName"])
  bindingType = str(ctx.node.properties["bindingType"])
  vlanId = str(ctx.node.properties["vlanId"])

  solo_config = None
  vNetworkName = None
  datapathId = None
  for rel in ctx.instance.relationships:
    if rel.target.node.type == "cloudify.solo.nodes.VirtualSwitch":
      solo_config = rel.target.node.properties["solo_config"]
      vNetworkName = str(rel.target.node.properties["vNetworkName"])
      datapathId = str(rel.target.node.properties["datapathId"])

  if solo_config == None:
    solo_config = ctx.node.properties["solo_config"]
  if vNetworkName == None:
    vNetworkName = str(ctx.node.properties["vNetworkName"])
  if datapathId == None:
    datapathId = str(ctx.node.properties["datapathId"])
  data = { "vPorts": [{
                "vNetworkName": vNetworkName,
                "datapathId": datapathId,
                "virtualPortNumber": virtualPortNumber,
                "physicalPortName": physicalPortName,
                "bindingType": bindingType,
                "vlanId": vlanId
              }]
          }
  urlPath = "/vport"
  ctx.logger.info(data)
  response = REST.post(urlPath, data, solo_config)
  ctx.logger.info(response.json()) 

@operation
def delete(**kwargs):
  ctx.logger.info("port_delete") 
  virtualPortNumber = str(ctx.node.properties["virtualPortNumber"])
  solo_config = None
  vNetworkName = None
  datapathId = None
  for rel in ctx.instance.relationships:
    if rel.target.node.type == "cloudify.solo.nodes.VirtualSwitch":
      solo_config = rel.target.node.properties["solo_config"]
      vNetworkName = str(rel.target.node.properties["vNetworkName"])
      datapathId = str(rel.target.node.properties["datapathId"])

  if solo_config == None:
    solo_config = ctx.node.properties["solo_config"]
  if vNetworkName == None:
    vNetworkName = str(ctx.node.properties["vNetworkName"])
  if datapathId == None:
    datapathId = str(ctx.node.properties["datapathId"])
  urlPath = "/vport/network/{}/device/{}/port/{}".format(vNetworkName, datapathId, virtualPortNumber)
  response = REST.delete(urlPath, solo_config)