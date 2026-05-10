import base_types

class ISICIdentifier(base_types._BaseDataType_String):

	_pattern = r"[A-U]{1,1}[0-9]{0,4}"

