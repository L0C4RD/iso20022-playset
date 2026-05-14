# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CardPaymentServiceType2Code(base_types._BaseDataType_String):

	_values = {
		"AGGR",
		"DCCV",
		"GRTT",
		"INSP",
		"LOYT",
		"NRES",
		"PUCO",
		"RECP",
		"SOAF",
		"UNAF",
		"VCAU",
	}