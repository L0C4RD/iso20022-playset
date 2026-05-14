# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class FinancialInstrumentContractType1Code(base_types._BaseDataType_String):

	_values = {
		"CFDS",
		"FORW",
		"FRAS",
		"FUTR",
		"OPTN",
		"OTHR",
		"SPDB",
		"SWAP",
		"SWPT",
		"FONS",
		"PSWP",
		"FFAS",
		"FWOS",
	}