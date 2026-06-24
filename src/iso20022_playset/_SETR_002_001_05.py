# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RedemptionBulkOrderCancellationRequestV05 import RedemptionBulkOrderCancellationRequestV05

class SETR_002_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:setr.002.001.05",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_RedBlkOrdrCxlReq"]
		@property
		def RedBlkOrdrCxlReq(self):
			return self._RedBlkOrdrCxlReq

		@RedBlkOrdrCxlReq.setter
		def RedBlkOrdrCxlReq(self, value):
			self._RedBlkOrdrCxlReq = value if type(value) != base_types.auto else self.make_default("RedBlkOrdrCxlReq")

		@RedBlkOrdrCxlReq.deleter
		def RedBlkOrdrCxlReq(self):
			del self._RedBlkOrdrCxlReq
			self._RedBlkOrdrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedBlkOrdrCxlReq', type=RedemptionBulkOrderCancellationRequestV05, min=1, max=1, mutex_group=None, array=False),
		))