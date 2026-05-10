from . import base_types

class Exact4AlphaNumericText(base_types._BaseDataType_String):

	_pattern = r"[a-zA-Z0-9]{4}"

