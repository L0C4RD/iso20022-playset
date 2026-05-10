from . import base_types

class Max10DateText(base_types._BaseDataType_String):

	_pattern = r"([0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2})|([0-9]{2,2}-[0-9]{2,2})|([0-9]{4,4}-[0-9]{2,2})"

