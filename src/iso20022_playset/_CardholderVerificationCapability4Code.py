# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CardholderVerificationCapability4Code(base_types._BaseDataType_String):

	_values = {
		"APKI",
		"CHDT",
		"MNSG",
		"MNVR",
		"FBIG",
		"FBIO",
		"FDSG",
		"FCPN",
		"FEPN",
		"NPIN",
		"PKIS",
		"SCEC",
		"NBIO",
		"NOVF",
		"OTHR",
	}