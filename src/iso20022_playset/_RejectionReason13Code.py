# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RejectionReason13Code(base_types._BaseDataType_String):

	_values = {
		"FAIL",
		"SAID",
		"INID",
		"REFI",
		"MICA",
	}