# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class AuthenticationMethod1Code(base_types._BaseDataType_String):

	_values = {
		"UKNW",
		"BYPS",
		"NPIN",
		"FPIN",
		"CPSG",
		"PPSG",
		"MANU",
		"MERC",
		"SCRT",
		"SNCT",
		"SCNL",
	}