from . import base_types

class ISO20022MessageIdentificationText(base_types._BaseDataType_String):

	_pattern = r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}"

