import base_types

class UKDomesticSortCodeIdentifier(base_types._BaseDataType_String):

	_pattern = r"SC[0-9]{6,6}"

