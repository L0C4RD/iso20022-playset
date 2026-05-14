# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TaxType9Code(base_types._BaseDataType_String):

	_values = {
		"PROV",
		"NATI",
		"STAT",
		"WITH",
		"STAM",
		"COAX",
		"VATA",
		"CUST",
	}