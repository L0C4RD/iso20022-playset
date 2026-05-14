# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CommissionType9Code(base_types._BaseDataType_String):

	_values = {
		"CLDI",
		"STEP",
		"SOFT",
		"PERN",
		"FLAT",
		"PERU",
		"PWCD",
		"PWEU",
		"BRKR",
		"DFDP",
		"PBOC",
	}