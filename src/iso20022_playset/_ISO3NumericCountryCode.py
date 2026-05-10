from . import base_types

class ISO3NumericCountryCode(base_types._BaseDataType_String):

	_pattern = r"[0-9]{3,3}"

