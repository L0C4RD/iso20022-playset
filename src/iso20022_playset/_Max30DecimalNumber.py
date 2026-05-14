# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max30DecimalNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 30
	_max_fractiondigits = 29