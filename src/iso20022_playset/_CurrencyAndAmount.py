# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyCode

class CurrencyAndAmount(base_types._BaseDataType_Decimal):

	attrib = None
	_attrib_defs = frozenset((
		base_types.AttributeEntry(name='Ccy', type=CurrencyCode, required=True),
	))

	_max_totaldigits = 18
	_max_fractiondigits = 5
	_min_inclusive = 0