# Service Chains Demo
The purpose of this demo is to highlight how deployment update process work. In order to make it verbose, we are using artificial (phantom) node & relationship types in TOSCA - which the only purpose is to print on the console fact that given lifecycle action is being triggered on a node.
```
demo$ cat ./types/demo-types.yaml 
node_types:

  cloudify.nodes.vRouter:
    derived_from: cloudify.nodes.Router
    interfaces:
      cloudify.interfaces.lifecycle:
        start:
          implementation: scripts/router-start.py
          executor: central_deployment_agent
        stop:
          implementation: scripts/router-stop.py
          executor: central_deployment_agent

----CUT---
relationships:

  cloudify.relationships.rtr_connected_to_network:
    derived_from: cloudify.relationships.connected_to
    source_interfaces:
      cloudify.interfaces.relationship_lifecycle:
        preconfigure:
          implementation: scripts/relationships/src-preconfigure.py
          executor: central_deployment_agent
---CUT---
```

Besides of update workflow execution, this example is demonstrating what lifecycle interfaces are triggered in install & uninstall workflow executions.

```
2018-02-02 11:48:43.768  LOG <service-chains> [network2_4lfoqj.start] INFO: ---> NETWORK network2 is starting...
2018-02-02 11:48:43.768  LOG <service-chains> [network1_9spema.start] INFO: ---> NETWORK network1 is starting...
2018-02-02 11:48:47.862  LOG <service-chains> [vRTR-1_hkfv3i.start] INFO: ---> VNF vRTR-1 is starting...
2018-02-02 11:48:47.862  LOG <service-chains> [vLoadBalancer_cvt181.start] INFO: ---> VNF vLoadBalancer is starting...
```
# Execution examples

### STEP1: Create basic service chain

cfy blueprint upload -b 3vnf-bp ./3vnf-blueprint.yaml
cfy deployment create service-chains -b 3vnf-bp
cfy executions start -d service-chains install

### STEP2: Update deployment

cfy deployments update  service-chains -p ./1vnf-blueprint.yaml
cfy deployments update  service-chains -p ./2vnf-blueprint.yaml
cfy deployments update  service-chains -p ./3vnf-blueprint.yaml


