# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PendingStatus4Code(base_types._BaseDataType_String):

	_values = {
		"ACPD",
		"VALD",
		"MATD",
		"AUTD",
		"INVD",
		"UMAC",
		"STLE",
		"STLM",
		"SSPD",
		"PCAN",
		"PSTL",
		"PFST",
		"SMLR",
		"RMLR",
		"SRBL",
		"AVLB",
		"SRML",
	}