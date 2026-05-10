from . import base_types

class RejectReason2Code(base_types._BaseDataType_String):

	_values = {
		"UNPR",
		"IMSG",
		"PARS",
		"SECU",
		"INTP",
		"RCPP",
		"VERS",
		"MSGT",
	}

