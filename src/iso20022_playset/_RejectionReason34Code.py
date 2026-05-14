# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RejectionReason34Code(base_types._BaseDataType_String):

	_values = {
		"ADEA",
		"LATE",
		"CASH",
		"NRGM",
		"NRGN",
		"OTHR",
		"REFE",
	}