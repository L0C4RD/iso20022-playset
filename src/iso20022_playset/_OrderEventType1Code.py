# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class OrderEventType1Code(base_types._BaseDataType_String):

	_values = {
		"CAME",
		"CAMO",
		"CHME",
		"CHMO",
		"EXPI",
		"FILL",
		"NEWO",
		"PARF",
		"REMA",
		"REMO",
		"REMH",
		"REME",
		"TRIG",
		"RFQS",
		"RFQR",
	}