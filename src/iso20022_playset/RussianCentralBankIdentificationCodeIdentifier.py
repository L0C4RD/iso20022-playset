import base_types

class RussianCentralBankIdentificationCodeIdentifier(base_types._BaseDataType_String):

	_pattern = r"RU[0-9]{9,9}"

