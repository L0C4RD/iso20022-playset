from . import base_types

class SwissBCIdentifier(base_types._BaseDataType_String):

	_pattern = r"SW[0-9]{3,5}"

