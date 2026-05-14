# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TaxType16Code(base_types._BaseDataType_String):

	_values = {
		"COAX",
		"CTAX",
		"EUTR",
		"LEVY",
		"LOCL",
		"NATI",
		"PROV",
		"STAM",
		"STAT",
		"STEX",
		"TRAN",
		"TRAX",
		"VATA",
		"WITH",
		"NKAP",
		"KAPA",
	}