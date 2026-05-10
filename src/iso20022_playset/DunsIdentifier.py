from . import base_types

class DunsIdentifier(base_types._BaseDataType_String):

	_pattern = r"[0-9]{9,9}"

