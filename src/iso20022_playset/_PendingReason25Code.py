# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PendingReason25Code(base_types._BaseDataType_String):

	_values = {
		"ADEA",
		"ADDM",
		"DQUA",
		"DREM",
		"FULL",
		"IPOA",
		"IPOS",
		"LACK",
		"LATE",
		"NPOS",
		"IREG",
		"OTHR",
		"PRXY",
		"PENR",
		"IPED",
	}