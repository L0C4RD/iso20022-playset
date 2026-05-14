# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RestrictedFINActiveCurrencyAnd13DecimalAmount_SimpleType(base_types._BaseDataType_Decimal):

	_max_totaldigits = 14
	_max_fractiondigits = 13
	_min_inclusive = 0