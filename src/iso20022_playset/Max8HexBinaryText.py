import base_types

class Max8HexBinaryText(base_types._BaseDataType_String):

	_pattern = r"([0-9A-F][0-9A-F]){1,8}"

