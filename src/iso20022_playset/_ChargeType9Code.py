# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ChargeType9Code(base_types._BaseDataType_String):

	_values = {
		"MANF",
		"BEND",
		"FEND",
		"ADVI",
		"CUST",
		"PUBL",
		"ACCT",
		"EQUL",
		"PENA",
	}