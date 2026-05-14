# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CardholderVerificationCapability5Code(base_types._BaseDataType_String):

	_values = {
		"APKI",
		"NOVF",
		"FBIG",
		"FBIO",
		"FDSG",
		"FCPN",
		"FEPN",
		"NBIO",
		"NPIN",
		"OTHN",
		"OTHP",
		"SIGN",
		"UNSP",
		"VORN",
		"PKIS",
		"NOPN",
		"NOOP",
	}