# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation
from common import *


@operation
def create(**kwargs):
  ctx.logger.info("link_create")
  linkType = str(ctx.node.properties["linkType"])
  vlanId = str(ctx.node.properties["vlanId"])
  nsiBandwidth = str(ctx.node.properties["nsiBandwidth"])

  solo_config = None
  vNetworkName = None
  virtualPortNumber = {}
  datapathId = {}
  physicalPort = {}
  point = None
  for rel in ctx.instance.relationships:
    if rel.target.node.type == "cloudify.solo.nodes.VirtualSwitch":
      if rel.type == "cloudify.solo.connected_from":
        point = "src"
      if rel.type == "cloudify.solo.connected_to":
        point = "dst"
      solo_config = rel.target.instance.runtime_properties["solo_config"]
      vNetworkName = str(rel.target.instance.runtime_properties["vNetworkName"])
      datapathId[point] = str(rel.target.instance.runtime_properties["datapathId"])
      physicalPort[point] = str(rel.target.instance.runtime_properties["physicalPortName"])
      virtualPortNumber[point] = str(rel.target.instance.runtime_properties["virtualPortNumber"])
      aux += 1
  #TODO if it is defined in bluepint and not in relationship

  data = {"vLinks": [{
                "vNetworkName": vNetworkName,
                "srcVirtualPortNumber": virtualPortNumber["src"],
                "dstVirtualPortNumber": virtualPortNumber["dst"],
                "srcDatapathId": datapathId["src"],
                "dstDatapathId": datapathId["dst"],
                "srcPhysicalPort": physicalPort["src"],
                "dstPhysicalPort": physicalPort["dst"],
                "linkType": linkType,
                "vlanId": vlanId,
                "nsiBandwidth": nsiBandwidth
              }]
          }
  urlPath = "/vlink"
  ctx.logger.info(data)
  response = REST.post(urlPath, data, solo_config)

@operation
def delete(**kwargs):
  ctx.logger.info("link_delete")  
  linkType = str(ctx.node.properties["linkType"])
  vlanId = str(ctx.node.properties["vlanId"])
  nsiBandwidth = str(ctx.node.properties["nsiBandwidth"])

  solo_config = None
  vNetworkName = None
  virtualPortNumber = {}
  datapathId = {}
  physicalPort = {}
  dictName = ["src", "dst"]
  aux = 0
  for rel in ctx.instance.relationships:
    if rel.target.node.type == "cloudify.solo.nodes.VirtualPort":
      solo_config = rel.target.instance.runtime_properties["solo_config"]
      vNetworkName = str(rel.target.instance.runtime_properties["vNetworkName"])
      datapathId[dictName[aux]] = str(rel.target.instance.runtime_properties["datapathId"])
      physicalPort[dictName[aux]] = str(rel.target.instance.runtime_properties["physicalPortName"])
      virtualPortNumber[dictName[aux]] = str(rel.target.instance.runtime_properties["virtualPortNumber"])
      aux += 1
  #TODO if it is defined in bluepint and not in relationship

  data = {"vLinks": [{
                "vNetworkName": vNetworkName,
                "srcVirtualPortNumber": virtualPortNumber["src"],
                "dstVirtualPortNumber": virtualPortNumber["dst"],
                "srcDatapathId": datapathId["src"],
                "dstDatapathId": datapathId["dst"],
                "srcPhysicalPort": physicalPort["src"],
                "dstPhysicalPort": physicalPort["dst"],
                "linkType": linkType,
                "vlanId": vlanId,
                "nsiBandwidth": nsiBandwidth
              }]
          }
  urlPath = "/vlink"
  ctx.logger.info(data)
  response = REST.delete(urlPath, solo_config, data=data)