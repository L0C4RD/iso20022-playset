# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Verification3Code(base_types._BaseDataType_String):

	_values = {
		"FAIL",
		"FUTA",
		"MISS",
		"NOSP",
		"NOVF",
		"OTHN",
		"OTHP",
		"PART",
		"SUCC",
		"ERRR",
	}