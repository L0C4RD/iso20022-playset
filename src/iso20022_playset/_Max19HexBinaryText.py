from . import base_types

class Max19HexBinaryText(base_types._BaseDataType_String):

	_pattern = r"([0-9A-F][0-9A-F]){1,19}"

