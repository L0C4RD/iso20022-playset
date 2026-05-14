# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Action1Code(base_types._BaseDataType_String):

	_values = {
		"SBTW",
		"RSTW",
		"RSBS",
		"ARDM",
		"ARCS",
		"ARES",
		"WAIT",
		"UPDT",
		"SBDS",
		"ARBA",
	}