from . import base_types

class RestrictedFINZMax8000Text(base_types._BaseDataType_String):

	_max = 8000
	_min = 1
	_pattern = r"[0-9a-zA-Z!\"%&\*;<> \.,\(\)\n\r/='\+:\?@#\{\-_]{1,8000}"

