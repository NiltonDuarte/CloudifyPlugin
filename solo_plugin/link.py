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
  srcVirtualPortNumber = str(ctx.node.properties["srcVirtualPortNumber"])
  dstVirtualPortNumber = str(ctx.node.properties["dstVirtualPortNumber"])
  srcPhysicalPort = str(ctx.node.properties["srcPhysicalPort"])
  dstPhysicalPort = str(ctx.node.properties["dstPhysicalPort"])

  solo_config = None
  vNetworkName = None
  datapathId = {}
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

  #TODO if it is defined in bluepint and not in relationship

  data = {"vLinks": [{
                "vNetworkName": vNetworkName,
                "srcVirtualPortNumber": srcVirtualPortNumber,
                "dstVirtualPortNumber": dstVirtualPortNumber,
                "srcDatapathId": datapathId["src"],
                "dstDatapathId": datapathId["dst"],
                "srcPhysicalPort": srcPhysicalPort,
                "dstPhysicalPort": dstPhysicalPort,
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
  srcVirtualPortNumber = str(ctx.node.properties["srcVirtualPortNumber"])
  dstVirtualPortNumber = str(ctx.node.properties["dstVirtualPortNumber"])
  srcPhysicalPort = str(ctx.node.properties["srcPhysicalPort"])
  dstPhysicalPort = str(ctx.node.properties["dstPhysicalPort"])

  solo_config = None
  vNetworkName = None
  datapathId = {}
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

  #TODO if it is defined in bluepint and not in relationship

  data = {"vLinks": [{
                "vNetworkName": vNetworkName,
                "srcVirtualPortNumber": srcVirtualPortNumber,
                "dstVirtualPortNumber": dstVirtualPortNumber,
                "srcDatapathId": datapathId["src"],
                "dstDatapathId": datapathId["dst"],
                "srcPhysicalPort": srcPhysicalPort,
                "dstPhysicalPort": dstPhysicalPort,
                "linkType": linkType,
              }]
          }
  urlPath = "/vlink"
  ctx.logger.info(data)
  response = REST.delete(urlPath, solo_config, data=data)