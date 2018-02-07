import dialogflow_v2beta1
from dialogflow_v2beta1.types import EntityType

client = dialogflow_v2beta1.EntityTypesClient()

parent = client.project_agent_path('shoppingmalldemo')
entity_type = EntityType(display_name='entity-creation-demo', kind=EntityType.Kind.Value('KIND_MAP'))
# entity_type = EntityType(name='entity_demo', display_name='Entity creation demo', kind=1)
print entity_type

# response = client.create_entity_type(parent, entity_type)
# print response


# parent = response.name
parent = 'projects/shoppingmalldemo/agent/entityTypes/5b2c3eae-9f8e-46d8-8b6c-16073f685cb4'
entities = [
	EntityType.Entity(value='aa3', synonyms=['bb', 'cc']),
	EntityType.Entity(value='aa4', synonyms=['bb', 'cc'])
]

response = client.batch_create_entities(parent, entities)
print response

def callback(operation_future):
    # Handle result.
    result = operation_future.result()

response.add_done_callback(callback)

ex = response.exception()
print ex

# Handle metadata.
# metadata = response.metadata()



