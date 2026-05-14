# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TransferUnmatchedReason3Code(base_types._BaseDataType_String):

	_values = {
		"CMIS",
		"CPCA",
		"DELN",
		"DSEC",
		"PHYS",
		"PODU",
		"DEPT",
		"DDAT",
		"DQUA",
		"ICUS",
		"SAFE",
	}