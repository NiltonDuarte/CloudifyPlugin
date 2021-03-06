# import the ctx object
from cloudify import ctx # pylint: disable=import-error
# import the operation decorator
from cloudify.decorators import operation # pylint: disable=import-error
from common import REST

@operation
def create(**kwargs):
  ctx.logger.info("switch_create")
  
  datapathId = str(ctx.node.properties["datapathId"])
  controllerIp = str(ctx.node.properties["controllerIp"])
  controllerPort = str(ctx.node.properties["controllerPort"])
  openflowVersion = str(ctx.node.properties["openflowVersion"])
  physicalDevice = str(ctx.node.properties["physicalDevice"])
  
  ctx.logger.info("properties: "+str(ctx.node.properties))
  ctx.logger.info("ctx: "+str(dir(ctx)))
  ctx.logger.info("ctx.node: "+str(dir(ctx.node)))
  ctx.logger.info("ctx.instance: "+str(dir(ctx.instance)))
  ctx.logger.info("ctx.instance.runtime_properties: "+str(ctx.instance.runtime_properties))
  for rel in ctx.instance.relationships:
    solo_config = rel.target.node.properties["solo_config"]
    ctx.logger.info("rel: "+str(dir(rel)))
    ctx.logger.info("rel.target: "+str(dir(rel.target)))
    ctx.logger.info("rel.type: "+str(rel.type))
    ctx.logger.info("rel.target.node.properties: "+str(rel.target.node.properties))
    ctx.logger.info("rel.target.node.type: " + str(rel.target.node.type))

  solo_config = None
  vNetworkName = None
  for rel in ctx.instance.relationships:
    if rel.target.node.type == "cloudify.solo.nodes.VirtualNetwork":
      solo_config = rel.target.node.properties["solo_config"]
      vNetworkName = str(rel.target.node.properties["vNetworkName"])
      
  if solo_config == None:
    solo_config = ctx.node.properties["solo_config"]
  if vNetworkName == None:
    vNetworkName = str(ctx.node.properties["vNetworkName"])

  ctx.instance.runtime_properties['vNetworkName'] = vNetworkName
  ctx.instance.runtime_properties['solo_config'] = solo_config
  ctx.instance.runtime_properties['datapathId'] = datapathId
  data = { "vSwitches": [{
              "vNetworkName": vNetworkName,
              "datapathId": datapathId,
              "controllerIp": controllerIp,
              "controllerPort": controllerPort,
              "openflowVersion": openflowVersion,
              "physicalDevice": physicalDevice
            }]
          }
  urlPath = "/vswitch"
  ctx.logger.info(data)
  dummy = REST.post(urlPath, data, solo_config)
  #ctx.logger.info(response.json())   

@operation
def delete(**kwargs):
  ctx.logger.info("switch_delete")
  datapathId = str(ctx.node.properties["datapathId"])
  #maybe I could get this information in runtime_properties
  solo_config = None
  vNetworkName = None
  for rel in ctx.instance.relationships:
    if rel.target.node.type == "cloudify.solo.nodes.VirtualNetwork":
      solo_config = rel.target.node.properties["solo_config"]
      vNetworkName = str(rel.target.node.properties["vNetworkName"])
  if solo_config == None:
    solo_config = ctx.node.properties["solo_config"]
  if vNetworkName == None:
    vNetworkName = str(ctx.node.properties["vNetworkName"])
  urlPath="/vswitch/network/{}/device/{}".format(vNetworkName, datapathId)
  dummy = REST.delete(urlPath, solo_config)