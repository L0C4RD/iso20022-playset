# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class FedwireRoutingNumberIdentifier(base_types._BaseDataType_String):

	_pattern = r"FW[0-9]{9,9}"