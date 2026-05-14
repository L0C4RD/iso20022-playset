# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class AuthenticationMethod6Code(base_types._BaseDataType_String):

	_values = {
		"NPIN",
		"PPSG",
		"PSWD",
		"SCRT",
		"SCNL",
		"SNCT",
		"CPSG",
		"ADDB",
		"BIOM",
		"CDHI",
		"CRYP",
		"CSCV",
		"PSVE",
		"CSEC",
		"ADDS",
		"MANU",
		"FPIN",
		"TOKP",
	}