# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode

class ActiveOrHistoricCurrencyAnd19DecimalAmount(base_types._BaseDataType_Decimal):

	attrib = {
		"Ccy" : None,
	}

	_attrib_defs = frozenset((
		base_types.AttributeEntry(name='Ccy', type=ActiveCurrencyCode, required=True),
	))

	_max_totaldigits = 25
	_max_fractiondigits = 19
	_min_inclusive = 0