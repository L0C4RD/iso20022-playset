# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ReportingWaiverType3Code(base_types._BaseDataType_String):

	_values = {
		"BENC",
		"ACTX",
		"ILQD",
		"SIZE",
		"CANC",
		"AMND",
		"SDIV",
		"RPRI",
		"DUPL",
		"LRGS",
		"TNCP",
		"TPAC",
		"XFPH",
	}