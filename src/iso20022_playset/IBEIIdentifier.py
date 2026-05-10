from . import base_types

class IBEIIdentifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z]{2,2}[B-DF-HJ-NP-TV-XZ0-9]{7,7}[0-9]{1,1}"

