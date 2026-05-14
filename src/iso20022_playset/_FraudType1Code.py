# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class FraudType1Code(base_types._BaseDataType_String):

	_values = {
		"ACTO",
		"CWUI",
		"CRNT",
		"FRAC",
		"FRAP",
		"CWKA",
		"CRDL",
		"MISC",
		"OTHN",
		"OTHP",
		"CRDS",
		"CNPA",
		"MUFD",
		"COSN",
	}