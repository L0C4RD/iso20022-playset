# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RedemptionBulkOrderCancellationRequestV05

class SETR_002_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.002.001.05"
		_docname = "setr.002.001.05"

		__slots__ = ["_RedBlkOrdrCxlReq"]
		@property
		def RedBlkOrdrCxlReq(self):
			return self._RedBlkOrdrCxlReq

		@RedBlkOrdrCxlReq.setter
		def RedBlkOrdrCxlReq(self, value):
			self._RedBlkOrdrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'RedBlkOrdrCxlReq', RedemptionBulkOrderCancellationRequestV05, False)

		@RedBlkOrdrCxlReq.deleter
		def RedBlkOrdrCxlReq(self):
			del self._RedBlkOrdrCxlReq
			self._RedBlkOrdrCxlReq = base_types.UninitialisedField(self, 'RedBlkOrdrCxlReq', RedemptionBulkOrderCancellationRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedBlkOrdrCxlReq', type=RedemptionBulkOrderCancellationRequestV05, min=1, max=1, mutex_group=None, array=False),
		))