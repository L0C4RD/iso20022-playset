# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class FileActionType2Code(base_types._BaseDataType_String):

	_values = {
		"ADDD",
		"BRPT",
		"DELT",
		"DLSP",
		"ENQR",
		"OTHN",
		"OTHP",
		"REPL",
		"REQU",
		"UPDT",
	}