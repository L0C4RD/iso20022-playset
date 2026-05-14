# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PendingStatusReason1Code(base_types._BaseDataType_String):

	_values = {
		"KYCM",
		"FRDM",
		"RIGH",
		"ATHR",
		"ATHP",
		"MODI",
	}