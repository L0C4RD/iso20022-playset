from . import base_types

class SouthAfricanNCCIdentifier(base_types._BaseDataType_String):

	_pattern = r"ZA[0-9]{6,6}"

