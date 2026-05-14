# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CommunicationMethod4Code(base_types._BaseDataType_String):

	_values = {
		"EMAL",
		"FAXI",
		"FILE",
		"ONLI",
		"PHON",
		"POST",
		"PROP",
		"SWMT",
		"SWMX",
	}