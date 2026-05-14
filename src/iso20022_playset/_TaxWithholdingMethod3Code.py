# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TaxWithholdingMethod3Code(base_types._BaseDataType_String):

	_values = {
		"MITX",
		"INVE",
		"ACCT",
		"EXMT",
		"REPT",
		"CRTF",
		"WHCO",
		"WTHD",
		"WTRE",
	}