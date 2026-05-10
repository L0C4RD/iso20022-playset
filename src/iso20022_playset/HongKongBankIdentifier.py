import base_types

class HongKongBankIdentifier(base_types._BaseDataType_String):

	_pattern = r"HK[0-9]{3,3}"

