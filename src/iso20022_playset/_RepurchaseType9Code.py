# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RepurchaseType9Code(base_types._BaseDataType_String):

	_values = {
		"PAIR",
		"PADJ",
		"RATE",
		"CALL",
		"ROLP",
		"CADJ",
		"TOPU",
		"WTHD",
	}