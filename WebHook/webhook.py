# -*- coding:utf8 -*-

import json
import csv

from flask import Flask, request, make_response, jsonify

APP = Flask(__name__)
LOG = APP.logger


@APP.route('/', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('result').get('action')
    except AttributeError:
        return 'json error'

    parameters = req['result']['parameters']
    contexts = req['result']['contexts']

    print 'Dialogflow Parameters:'
    print json.dumps(parameters, indent=4)

    if action == 'fulfill':
        res = fulfill(parameters, contexts)
    elif action == 'myintent.test':
        res = myintent_test(parameters, contexts)
    elif action == 'looking-forsmartphone.looking-forsmartphone-yes.looking-forsmartphone-yes-brand-please-custom':
        res = goto_list_models(parameters, contexts)
    elif action == 'list-smartphone-model':
        res = list_smartphone_model(parameters, contexts)
    elif action == 'listsmartphonemodel.listsmartphonemodel-select':
        res = select_smartphone_model(parameters, contexts)
    elif action == 'looking-forothers.looking-forothers-yes':
        res = list_others(parameters, contexts)
    else:
        LOG.error('Unexpected action.')

    print 'Action: ' + action
    print 'Response: ' + json.dumps(res)

    return make_response(jsonify(res))

def fulfill(parameters, contexts):
    res = {
		'contextOut': [{"name": "looking-for-smartphone", "lifespan": 2, "parameters": {
				"product-smartphone": "smartphone",
				"brand": "samsung"
		}}],
		'followupEvent': {
			"name": "LIST_SMARTPHONE_MODEL"
		},
		'speech': '', 
		'displayText': ''
	}

    return res

def goto_list_models(parameters, contexts):
    res = {
		'contextOut': [{"name": "looking-for-smartphone", "lifespan": 2, "parameters": {
				"product-smartphone": "smartphone",
				"brand": parameters["brand"]
		}}],
		'followupEvent': {
			"name": "LIST_SMARTPHONE_MODEL"
		},
		'speech': '', 
		'displayText': ''
	}

    return res

def select_smartphone_model(parameters, contexts):
    res = {
		'followupEvent': {
			"name": "SMARTPHONE_MODEL",
			"data": {
				"model": parameters['model']
			}
		},
		'speech': '', 
		'displayText': ''
	}

    return res

def myintent_test(parameters, contexts):
    res = {
		'contextOut': [{"name": "myintent", "lifespan": 2, "parameters": {
				"intent": "rome"
		}}],
		'speech': 'My Intent ' + str(parameters['brand']), 
		'displayText': 'My Intent ' + str(parameters['brand'])
	}

    return res

def list_smartphone_model(parameters, contexts):
    with open('model.csv', 'rb') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='"')

	models = []
	brand = parameters['brand']
        for line in rows:
		print line[0], brand, line[0].startswith(brand)
		if line[0].startswith(brand):
			models.append(line[0])
			print line[0]

	txt = 'This is ' + parameters['product-smartphone'] +' list for ' + parameters['brand'] + '.\nWhich model do you want?'

    res = {
		'speech': txt, 
		'displayText': txt + '\n' + '\n'.join(models)
	}

    return res

def list_others(parameters, contexts):
    with open('category.csv', 'rb') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='"')

	models = []
        for line in rows:
		models.append(line[0])

	txt = 'This is ' + parameters['product-others'] +' list.\nWhich one do you want?'

    res = {
		'speech': txt, 
		'displayText': txt + '\n' + '\n'.join(models)
	}

    return res

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
