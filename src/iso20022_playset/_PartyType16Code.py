# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PartyType16Code(base_types._BaseDataType_String):

	_values = {
		"ACQR",
		"CISS",
		"DLIS",
		"ITAG",
		"OTRM",
		"BKAF",
		"BKAT",
		"ATMG",
	}