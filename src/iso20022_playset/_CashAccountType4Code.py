# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CashAccountType4Code(base_types._BaseDataType_String):

	_values = {
		"CASH",
		"CHAR",
		"COMM",
		"TAXE",
		"CISH",
		"TRAS",
		"SACC",
		"CACC",
		"SVGS",
		"ONDP",
		"MGLD",
		"NREX",
		"MOMA",
		"LOAN",
		"SLRY",
		"ODFT",
	}