# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CardholderVerificationCapability1Code(base_types._BaseDataType_String):

	_values = {
		"MNSG",
		"NPIN",
		"FCPN",
		"FEPN",
		"FDSG",
		"FBIO",
		"MNVR",
		"FBIG",
		"APKI",
		"PKIS",
		"CHDT",
		"SCEC",
	}