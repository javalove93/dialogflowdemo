import dialogflow_v2beta1

client = dialogflow_v2beta1.IntentsClient()

parent = client.project_agent_path('shoppingmalldemo')


# Iterate over all results
for element in client.list_intents(parent):
	print element

