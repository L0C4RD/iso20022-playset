# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PendingOpeningStatusReason1Code(base_types._BaseDataType_String):

	_values = {
		"ATHR",
		"ATHP",
		"FRDM",
		"KYCM",
		"NOTO",
		"REST",
		"RIGH",
	}