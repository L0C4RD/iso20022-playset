from . import base_types

class Max2NumericText(base_types._BaseDataType_String):

	_pattern = r"[0-9]{1,2}"

