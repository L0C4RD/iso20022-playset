import base_types

class ISO18245MerchantCategoryCode(base_types._BaseDataType_String):

	_pattern = r"[0-9]{4,4}"

