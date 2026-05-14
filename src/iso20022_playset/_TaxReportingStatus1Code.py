# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TaxReportingStatus1Code(base_types._BaseDataType_String):

	_values = {
		"ACPT",
		"RCVD",
		"RJCT",
		"INCF",
		"CRPT",
		"WARN",
		"ACTC",
		"PART",
	}