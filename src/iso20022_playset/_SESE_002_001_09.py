# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransferOutCancellationRequestV09 import TransferOutCancellationRequestV09

class SESE_002_001_09():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.002.001.09"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_TrfOutCxlReq"]
		@property
		def TrfOutCxlReq(self):
			return self._TrfOutCxlReq

		@TrfOutCxlReq.setter
		def TrfOutCxlReq(self, value):
			self._TrfOutCxlReq = value if type(value) != base_types.auto else self.make_default("TrfOutCxlReq")

		@TrfOutCxlReq.deleter
		def TrfOutCxlReq(self):
			del self._TrfOutCxlReq
			self._TrfOutCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfOutCxlReq', type=TransferOutCancellationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))