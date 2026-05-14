# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ActiveCurrencyAnd24Amount_SimpleType(base_types._BaseDataType_Decimal):

	_max_totaldigits = 24
	_max_fractiondigits = 5
	_min_inclusive = 0