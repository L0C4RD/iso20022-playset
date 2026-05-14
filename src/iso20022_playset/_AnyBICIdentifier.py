# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class AnyBICIdentifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}"