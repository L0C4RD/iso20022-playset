# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class IndianFinancialSystemCodeIdentifier(base_types._BaseDataType_String):

	_pattern = r"IN[a-zA-Z0-9]{11,11}"