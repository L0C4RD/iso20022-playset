from . import base_types

class IrishNSCIdentifier(base_types._BaseDataType_String):

	_pattern = r"IE[0-9]{6,6}"

