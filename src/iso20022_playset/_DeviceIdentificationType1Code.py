from . import base_types

class DeviceIdentificationType1Code(base_types._BaseDataType_String):

	_values = {
		"IMEI",
		"OTHN",
		"OTHP",
		"SEID",
		"SENU",
	}

