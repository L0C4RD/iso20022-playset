import base_types

class Exact4AlphaNumericUnderscoreText(base_types._BaseDataType_String):

	_pattern = r"[a-zA-Z0-9]{1}[a-zA-Z0-9_]{3}"

