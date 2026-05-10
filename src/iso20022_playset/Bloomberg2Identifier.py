import base_types

class Bloomberg2Identifier(base_types._BaseDataType_String):

	_pattern = r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d"

