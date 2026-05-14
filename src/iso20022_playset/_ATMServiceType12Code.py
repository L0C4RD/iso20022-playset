# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ATMServiceType12Code(base_types._BaseDataType_String):

	_values = {
		"ASTS",
		"CDVF",
		"DCCS",
		"XRTD",
		"XRTW",
		"EMVS",
		"CMPF",
		"BLCQ",
		"ACCD",
		"MINI",
	}