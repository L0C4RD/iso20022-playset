# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class VoteInstruction5Code(base_types._BaseDataType_String):

	_values = {
		"ABST",
		"CAGS",
		"CHRM",
		"CFOR",
		"NOAC",
		"WTHH",
		"ONEY",
		"THRY",
		"TWOY",
		"BLNK",
		"NREC",
	}