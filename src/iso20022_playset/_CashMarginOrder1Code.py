# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CashMarginOrder1Code(base_types._BaseDataType_String):

	_values = {
		"CASH",
		"MRGO",
		"MRGC",
	}