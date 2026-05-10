from . import base_types

class Min2Max3AlphaText(base_types._BaseDataType_String):

	_pattern = r"[a-zA-Z]{2,3}"

