# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CollateralType6Code(base_types._BaseDataType_String):

	_values = {
		"GBBK",
		"BOND",
		"CASH",
		"COMM",
		"INSU",
		"LCRE",
		"OTHR",
		"PHYS",
		"SECU",
		"STCF",
	}