# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TypeOfPrice6Code(base_types._BaseDataType_String):

	_values = {
		"BIDE",
		"OFFR",
		"NAVL",
		"CREA",
		"CANC",
		"INTE",
		"SWNG",
		"OTHR",
		"MIDD",
		"RINV",
		"SWIC",
		"DDVR",
		"ACTU",
		"NAUP",
	}