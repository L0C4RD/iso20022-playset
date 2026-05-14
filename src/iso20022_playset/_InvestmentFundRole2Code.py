# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class InvestmentFundRole2Code(base_types._BaseDataType_String):

	_values = {
		"FMCO",
		"REGI",
		"TRAG",
		"INTR",
		"DIST",
		"CONC",
		"UCL1",
		"UCL2",
		"TRAN",
	}