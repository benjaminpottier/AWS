### get_ssm_keys.py

Use AWS Systems Manager Parameter Store to manager SSH access.

Create a new paramter:

Name: `/ssh/<user>`, e.g. `/ssh/ubuntu`. The user must already exist.

TypeL `StringList`.

Paste your public key into the value.
