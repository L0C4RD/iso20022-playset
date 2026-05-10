import base_types

class SHA256SignatureText(base_types._BaseDataType_String):

	_pattern = r"([0-9A-F][0-9A-F]){32}"

