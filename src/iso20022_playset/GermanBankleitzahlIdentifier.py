import base_types

class GermanBankleitzahlIdentifier(base_types._BaseDataType_String):

	_pattern = r"BL[0-9]{8,8}"

