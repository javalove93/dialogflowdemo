import dialogflow_v2beta1

agentClient = dialogflow_v2beta1.AgentsClient()
client = dialogflow_v2beta1.EntityTypesClient()

parent = client.project_agent_path('shoppingmalldemo')
print parent

agentParent = agentClient.project_path('shoppingmalldemo')
print agentParent
response = agentClient.get_agent(agentParent)
print response

# Iterate over all results
for element in client.list_entity_types(parent):
    print element


