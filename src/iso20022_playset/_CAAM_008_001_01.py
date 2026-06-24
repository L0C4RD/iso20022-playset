# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._HostToATMAcknowledgementV01 import HostToATMAcknowledgementV01

class CAAM_008_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caam.008.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_HstToATMAck"]
		@property
		def HstToATMAck(self):
			return self._HstToATMAck

		@HstToATMAck.setter
		def HstToATMAck(self, value):
			self._HstToATMAck = value if type(value) != base_types.auto else self.make_default("HstToATMAck")

		@HstToATMAck.deleter
		def HstToATMAck(self):
			del self._HstToATMAck
			self._HstToATMAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='HstToATMAck', type=HostToATMAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))