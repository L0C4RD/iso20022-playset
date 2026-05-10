from . import base_types

class EICIdentifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z0-9\-]{16}"

