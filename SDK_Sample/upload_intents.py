import dialogflow_v2beta1
from dialogflow_v2beta1.types import Intent

client = dialogflow_v2beta1.IntentsClient()

parent = "projects/shoppingmalldemo/agent/intents/29f5436d-33e2-4b9e-b471-815f2c2f046c"

intent = client.get_intent(parent)
print intent
intent.messages.add(text=Intent.Message.Text(text='a'))
print intent.messages
part1 = Intent.TrainingPhrase.Part(text='abcd')
part2 = Intent.TrainingPhrase.Part(text='defg')
part3 = Intent.TrainingPhrase.Part(text='hijk @model')
intent.training_phrases.add(parts=[part1])
intent.training_phrases.add(parts=[part2])
intent.training_phrases.add(type=Intent.TrainingPhrase.Type.Value('TEMPLATE'), parts=[part3])
print intent.training_phrases

language_code = ''

response = client.update_intent(intent, language_code)
print response

