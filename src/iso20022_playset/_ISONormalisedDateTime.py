# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ISONormalisedDateTime(base_types._BaseDataType_DateTime):

	_pattern = r".*Z"