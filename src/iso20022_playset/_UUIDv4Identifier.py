# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class UUIDv4Identifier(base_types._BaseDataType_String):

	_pattern = r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}"