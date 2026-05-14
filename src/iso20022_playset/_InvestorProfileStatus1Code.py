# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class InvestorProfileStatus1Code(base_types._BaseDataType_String):

	_values = {
		"DISA",
		"DISG",
		"ENAB",
		"ENBG",
		"ADMI",
		"ANLY",
		"NAPP",
		"PSUS",
		"PEND",
		"SUPS",
	}