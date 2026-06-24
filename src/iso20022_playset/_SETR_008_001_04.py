# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SubscriptionBulkOrderCancellationRequestV04 import SubscriptionBulkOrderCancellationRequestV04

class SETR_008_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.008.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SbcptBlkOrdrCxlReq"]
		@property
		def SbcptBlkOrdrCxlReq(self):
			return self._SbcptBlkOrdrCxlReq

		@SbcptBlkOrdrCxlReq.setter
		def SbcptBlkOrdrCxlReq(self, value):
			self._SbcptBlkOrdrCxlReq = value if type(value) != base_types.auto else self.make_default("SbcptBlkOrdrCxlReq")

		@SbcptBlkOrdrCxlReq.deleter
		def SbcptBlkOrdrCxlReq(self):
			del self._SbcptBlkOrdrCxlReq
			self._SbcptBlkOrdrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdrCxlReq', type=SubscriptionBulkOrderCancellationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))