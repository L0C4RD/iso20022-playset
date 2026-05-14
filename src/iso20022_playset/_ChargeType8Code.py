# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ChargeType8Code(base_types._BaseDataType_String):

	_values = {
		"SIGN",
		"STDE",
		"STOR",
		"PACK",
		"PICK",
		"DNGR",
		"SECU",
		"INSU",
		"COLF",
		"CHOR",
		"CHDE",
		"AIRF",
		"TRPT",
	}