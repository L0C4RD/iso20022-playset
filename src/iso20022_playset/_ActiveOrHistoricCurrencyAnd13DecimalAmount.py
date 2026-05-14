# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class ActiveOrHistoricCurrencyAnd13DecimalAmount(base_types._BaseDataType_Decimal):

	attrib = {
		"Ccy" : None,
	}

	_attrib_defs = frozenset((
		base_types.AttributeEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, required=True),
	))

	_max_totaldigits = 18
	_max_fractiondigits = 13
	_min_inclusive = 0