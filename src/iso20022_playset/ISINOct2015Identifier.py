import base_types

class ISINOct2015Identifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}"

