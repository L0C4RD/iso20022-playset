# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class SpanishDomesticInterbankingIdentifier(base_types._BaseDataType_String):

	_pattern = r"ES[0-9]{8,9}"