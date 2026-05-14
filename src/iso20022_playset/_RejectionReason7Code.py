# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RejectionReason7Code(base_types._BaseDataType_String):

	_values = {
		"DEAC",
		"FAIL",
		"PDEA",
		"INID",
		"REFI",
		"AGIN",
		"SAID",
		"DEAO",
		"INET",
		"INUS",
		"INPT",
		"INMV",
		"INDE",
		"INDT",
	}