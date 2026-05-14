# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class AcknowledgementReason5Code(base_types._BaseDataType_String):

	_values = {
		"ADEA",
		"SMPG",
		"OTHR",
		"CDCY",
		"CDRG",
		"CDRE",
		"NSTP",
		"RQWV",
		"LATE",
	}