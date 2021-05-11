#!/usr/bin/python
#Author: Tang Sing Yuen (sintang@cisco.com)

from ansible.module_utils.basic import AnsibleModule
import requests
import json


def run_module():

	module = AnsibleModule(
		argument_spec=dict(
			dnacToken=dict(type='str',  required=True)
		)
	)

	result = dict(
        networkDevice=''
    )
	result = dict(changed=False)

	dnacToken = module.params["dnacToken"]

	url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/de6477ad-22a2-4daa-9941-eb61cecefb34"

	payload = {}
	headers = {
		'Content-Type': 'application/json',
		'X-Auth-Token': dnacToken
	}

	response = requests.request("GET", url, headers=headers, data = payload)
	
	result['networkDevice'] = json.loads(response.text)

	module.exit_json(**result)

if __name__ == '__main__':
    run_module()
