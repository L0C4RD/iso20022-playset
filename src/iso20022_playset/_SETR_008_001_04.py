# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SubscriptionBulkOrderCancellationRequestV04

class SETR_008_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.008.001.04"
		_docname = "setr.008.001.04"

		__slots__ = ["_SbcptBlkOrdrCxlReq"]
		@property
		def SbcptBlkOrdrCxlReq(self):
			return self._SbcptBlkOrdrCxlReq

		@SbcptBlkOrdrCxlReq.setter
		def SbcptBlkOrdrCxlReq(self, value):
			self._SbcptBlkOrdrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'SbcptBlkOrdrCxlReq', SubscriptionBulkOrderCancellationRequestV04, False)

		@SbcptBlkOrdrCxlReq.deleter
		def SbcptBlkOrdrCxlReq(self):
			del self._SbcptBlkOrdrCxlReq
			self._SbcptBlkOrdrCxlReq = base_types.UninitialisedField(self, 'SbcptBlkOrdrCxlReq', SubscriptionBulkOrderCancellationRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdrCxlReq', type=SubscriptionBulkOrderCancellationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))