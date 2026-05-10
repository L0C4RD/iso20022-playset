from . import base_types

class ItalianDomesticIdentifier(base_types._BaseDataType_String):

	_pattern = r"IT[0-9]{10,10}"

