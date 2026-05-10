import base_types

class EANGLNIdentifier(base_types._BaseDataType_String):

	_pattern = r"[0-9]{13,13}"

