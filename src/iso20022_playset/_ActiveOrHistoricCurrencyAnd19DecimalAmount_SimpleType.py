# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ActiveOrHistoricCurrencyAnd19DecimalAmount_SimpleType(base_types._BaseDataType_Decimal):

	_max_totaldigits = 25
	_max_fractiondigits = 19
	_min_inclusive = 0