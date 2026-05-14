# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ATMServiceType7Code(base_types._BaseDataType_String):

	_values = {
		"CHSN",
		"PINC",
		"PINR",
		"PINU",
		"PATH",
		"PRFL",
		"STDR",
		"SPRV",
		"TRFC",
		"TRFI",
		"DPSN",
		"DPSV",
		"MCHG",
		"TRFP",
	}