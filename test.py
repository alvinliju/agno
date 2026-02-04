from agno.docker.resource.network import DockerNetwork
from agno.docker.api_client import DockerApiClient
import logging

logging.basicConfig(level=logging.DEBUG)

client = DockerApiClient()
network = DockerNetwork(name="test-validation-network-4")

try:
  result = network.create(client)
  print(result)
  print(network.active_resource)
finally:
  network.delete(client)
