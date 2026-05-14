# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ExchangeRateAgreementType1Code(base_types._BaseDataType_String):

	_values = {
		"FWCT",
		"NORM",
		"OTHN",
		"OTHP",
		"SPOT",
	}