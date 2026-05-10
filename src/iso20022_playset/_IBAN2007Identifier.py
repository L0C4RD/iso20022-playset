from . import base_types

class IBAN2007Identifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}"

