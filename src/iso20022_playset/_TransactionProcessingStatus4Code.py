from . import base_types

class TransactionProcessingStatus4Code(base_types._BaseDataType_String):

	_values = {
		"PACK",
		"PPRC",
		"REJT",
		"REPR",
		"CAND",
		"CANP",
		"CPRC",
		"MPRC",
	}

