#!/usr/bin/python
#Author: Tang Sing Yuen (sintang@cisco.com)

from ansible.module_utils.basic import AnsibleModule
import requests
import base64
import json


def run_module():

	module = AnsibleModule(
		argument_spec=dict(
			username=dict(type='str',  required=True),
			password=dict(type='str',  required=True, no_log=True)
		)
	)
	result = dict(
        token=''
    )
	#result = dict(changed=False)

	sandbox_username = module.params["username"]
	sandbox_password = module.params["password"]

	base64_encoded = base64.b64encode(sandbox_username + ":" + sandbox_password)

	url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

	payload = {}
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Basic ' + base64_encoded
	}

	response = requests.request("POST", url, headers=headers, data = payload)
	
	result['Token'] = json.loads(response.text)["Token"]

	module.exit_json(**result)

if __name__ == '__main__':
    run_module()
