import base_types

class SmallNetworkIdentifier(base_types._BaseDataType_String):

	_pattern = r"AU[0-9]{6,6}"

