from cloudify.mocks import MockCloudifyContext
from cloudify.state import current_ctx
import docker_

props1 = {
      "physicalPort": "host-smoon2",
      "dockerClientAddr": "192.168.0.192:2375",
      "dockerImage": "hermsi/alpine-sshd:latest",
      "hostname": "alpsmoon2",
      "vlanId": "12",
      "dataplaneCIDR": "10.11.0.10/24",
      "dataplaneGateway": "10.11.0.1",
      "managementNetwork": "ext",
      "managementIP": "192.168.0.31"
}

props2 = {
      "physicalPort": "host-smoon",
      "dockerClientAddr": "192.168.0.192:2375",
      "dockerImage": "hermsi/alpine-sshd:latest",
      "hostname": "alpsmoon",
      "vlanId": "11",
      "dataplaneCIDR": "10.11.0.30/24",
      "dataplaneGateway": "10.11.0.2",
      "managementNetwork": "ext",
      "managementIP": "192.168.0.32"
}

mock_ctx1 = MockCloudifyContext(node_id='test_node_id',
                               node_name='test_node_name',
                               properties=props1)
mock_ctx2 = MockCloudifyContext(node_id='test_node_id',
                               node_name='test_node_name',
                               properties=props2)                               

input = raw_input("[c]reate, [d]elete or nothing: ")
try:
    if input == "create" or input == "c":
      current_ctx.set(mock_ctx1)
      docker_.create()
      current_ctx.clear()
      
      print "create1"
      raw_input("press any key to continue...")
      current_ctx.set(mock_ctx2)
      docker_.create()
      print "create2"
    if input == "delete" or input == "d":
      current_ctx.set(mock_ctx1)
      docker_.delete()
      current_ctx.clear()
      print "delete1"
      current_ctx.set(mock_ctx2)
      docker_.delete()
      print "delete2"
finally:
    current_ctx.clear()                               
