# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class BalanceType15Code(base_types._BaseDataType_String):

	_values = {
		"AMOH",
		"AMTO",
		"AMTD",
		"CRDL",
		"OTHN",
		"OTHP",
		"AVLB",
		"CLRI",
		"LDGR",
		"PNTS",
	}