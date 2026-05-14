# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class AgreementItemAction1Code(base_types._BaseDataType_String):

	_values = {
		"DEAC",
		"HOLD",
		"MDFY",
		"REAC",
		"OPEN",
		"SYNC",
		"VRFY",
	}