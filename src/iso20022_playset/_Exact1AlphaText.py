from . import base_types

class Exact1AlphaText(base_types._BaseDataType_String):

	_pattern = r"[a-zA-Z]{1}"

