import base_types

class EntryTypeIdentifier(base_types._BaseDataType_String):

	_pattern = r"[BEOVW]{1,1}[0-9]{2,2}|DUM"

