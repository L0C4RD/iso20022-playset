# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PercentageBoundedRate(base_types._BaseDataType_Decimal):

	_max_totaldigits = 11
	_max_fractiondigits = 10
	_min_inclusive = 0
	_max_inclusive = 100