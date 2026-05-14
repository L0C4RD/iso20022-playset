# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RejectReason1Code(base_types._BaseDataType_String):

	_values = {
		"UNPR",
		"IMSG",
		"PARS",
		"SECU",
		"INTP",
		"RCPP",
		"DPMG",
		"VERS",
		"MSGT",
	}