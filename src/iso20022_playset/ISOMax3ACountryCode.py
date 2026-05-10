from . import base_types

class ISOMax3ACountryCode(base_types._BaseDataType_String):

	_pattern = r"[A-Z]{2,3}"

