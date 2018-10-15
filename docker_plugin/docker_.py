# import the ctx object
from cloudify import ctx
# import the operation decorator
from cloudify.decorators import operation
import docker


@operation
def create(**kwargs):
    dockerClientAddr = ctx.node.properties["dockerClientAddr"]
    managementNet = ctx.node.properties["managementNetwork"]
    physicalPort = ctx.node.properties["physicalPort"]
    dockerImage = ctx.node.properties["dockerImage"]
    hostname = ctx.node.properties["hostname"]
    vlanId = ctx.node.properties["vlanId"]
    dataplaneCIDR = ctx.node.properties["dataplaneCIDR"]
    dataplaneGateway = ctx.node.properties["dataplaneGateway"]
    managementIP = ctx.node.properties["managementIP"]
    networkName = "macvlan{}".format(vlanId)
    dp_ipAddr = dataplaneCIDR.split("/")[0]
    client = docker.DockerClient(base_url=dockerClientAddr)

    ipam_pool = docker.types.IPAMPool(subnet=dataplaneCIDR, gateway=dataplaneGateway, iprange="{}/32".format(dp_ipAddr))
    ipam_cfg = docker.types.IPAMConfig(pool_configs=[ipam_pool])
    parent = "{}.{}".format(physicalPort, vlanId)
    client.networks.create(networkName, driver="macvlan", options = {"parent": parent},ipam=ipam_cfg, )

    cnt = client.containers.create(
        dockerImage, name=hostname, hostname=hostname, detach=True, 
        tty=True, cap_add=["NET_ADMIN"], network=managementNet)
    #client.networks.get(managementNet).connect(cnt)
    client.networks.get(networkName).connect(cnt, ipv4_address=dp_ipAddr)
    cnt.start()


@operation
def delete(**kwargs):
    dockerClientAddr = ctx.node.properties["dockerClientAddr"]
    hostname = ctx.node.properties["hostname"]
    vlanId = ctx.node.properties["vlanId"]
    networkName = "macvlan{}".format(vlanId)
    client = docker.DockerClient(base_url=dockerClientAddr)
    client.containers.get(hostname).remove(force=True)
    client.networks.get(networkName).remove()

