### get_ssm_keys.py

Use AWS Systems Manager Parameter Store to manager SSH access.

Create a new paramter:

Name: `/ssh/ubuntu` 

Type: `StringList`

Paste your public key into the value.
