from . import base_types

class CHIPSUniversalIdentifier(base_types._BaseDataType_String):

	_pattern = r"CH[0-9]{6,6}"

