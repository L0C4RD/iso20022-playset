# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TypeOfPrice10Code(base_types._BaseDataType_String):

	_values = {
		"BIDE",
		"OFFR",
		"NAVL",
		"CREA",
		"CANC",
		"INTE",
		"SWNG",
		"MIDD",
		"RINV",
		"SWIC",
		"DDVR",
		"ACTU",
	}