from . import base_types

class MICIdentifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z0-9]{4,4}"

