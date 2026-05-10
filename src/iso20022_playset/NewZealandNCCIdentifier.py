from . import base_types

class NewZealandNCCIdentifier(base_types._BaseDataType_String):

	_pattern = r"NZ[0-9]{6,6}"

