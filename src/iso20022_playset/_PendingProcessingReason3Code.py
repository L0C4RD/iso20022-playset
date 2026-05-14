# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PendingProcessingReason3Code(base_types._BaseDataType_String):

	_values = {
		"ADEA",
		"BLOC",
		"MUNO",
		"NEXT",
		"MINO",
		"OTHR",
		"DENO",
		"CERT",
	}