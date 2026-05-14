# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class HongKongBankIdentifier(base_types._BaseDataType_String):

	_pattern = r"HK[0-9]{3,3}"