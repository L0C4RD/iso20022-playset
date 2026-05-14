# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class HellenicBankIdentificationCodeIdentifier(base_types._BaseDataType_String):

	_pattern = r"GR[0-9]{7,7}"