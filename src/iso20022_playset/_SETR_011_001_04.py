# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SubscriptionOrderCancellationRequestV04

class SETR_011_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.011.001.04"
		_docname = "setr.011.001.04"

		__slots__ = ["_SbcptOrdrCxlReq"]
		@property
		def SbcptOrdrCxlReq(self):
			return self._SbcptOrdrCxlReq

		@SbcptOrdrCxlReq.setter
		def SbcptOrdrCxlReq(self, value):
			self._SbcptOrdrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'SbcptOrdrCxlReq', SubscriptionOrderCancellationRequestV04, False)

		@SbcptOrdrCxlReq.deleter
		def SbcptOrdrCxlReq(self):
			del self._SbcptOrdrCxlReq
			self._SbcptOrdrCxlReq = base_types.UninitialisedField(self, 'SbcptOrdrCxlReq', SubscriptionOrderCancellationRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdrCxlReq', type=SubscriptionOrderCancellationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))