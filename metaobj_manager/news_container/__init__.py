class news_container:
	"""
	python-representation of news_container
	"""

	# Access
	access = {"delete_custom":""
		,"delete_deny":[""
			,""
			,""]
		,"insert_custom":"{$}"
		,"insert_deny":[""
			,""
			,""]}

	# Enabled
	enabled = 1

	# Id
	id = "news_container"

	# Name
	name = "news_container"

	# Package
	package = ""

	# Revision
	revision = "0.0.1"

	# Type
	type = "ZMSDocument"

	# Attrs
	class Attrs:
		titlealt = {"default":""
			,"id":"titlealt"
			,"keys":[]
			,"mandatory":1
			,"multilang":1
			,"name":"DC.Title.Alt"
			,"repetitive":0
			,"type":"titlealt"}

		title = {"default":""
			,"id":"title"
			,"keys":[]
			,"mandatory":1
			,"multilang":1
			,"name":"DC.Title"
			,"repetitive":0
			,"type":"title"}

		items = {"default":""
			,"id":"items"
			,"keys":["amount"]
			,"mandatory":0
			,"multilang":0
			,"name":"Items"
			,"repetitive":0
			,"type":"*"}

		standard_html = {"default":""
			,"id":"standard_html"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"Template: news_container"
			,"repetitive":0
			,"type":"zpt"}
