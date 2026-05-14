# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class OrderStatus4Code(base_types._BaseDataType_String):

	_values = {
		"PACK",
		"COSE",
		"STNP",
		"RECE",
		"SETT",
		"CPNP",
		"CNFC",
		"DONE",
		"DONF",
		"OPOD",
		"IACO",
	}