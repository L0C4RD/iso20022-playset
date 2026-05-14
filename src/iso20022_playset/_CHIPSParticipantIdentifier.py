# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CHIPSParticipantIdentifier(base_types._BaseDataType_String):

	_pattern = r"CP[0-9]{4,4}"