# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class EnergyLoadType1Code(base_types._BaseDataType_String):

	_values = {
		"BSLD",
		"GASD",
		"HABH",
		"OFFP",
		"OTHR",
		"PKLD",
		"SHPD",
	}