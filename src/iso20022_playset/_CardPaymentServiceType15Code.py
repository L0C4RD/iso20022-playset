# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CardPaymentServiceType15Code(base_types._BaseDataType_String):

	_values = {
		"IRES",
		"URES",
		"PRES",
		"ARES",
		"FREC",
		"RREC",
		"GOPT",
		"DFCL",
	}