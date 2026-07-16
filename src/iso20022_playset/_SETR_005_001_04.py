# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RedemptionOrderCancellationRequestV04

class SETR_005_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.005.001.04"
		_docname = "setr.005.001.04"

		__slots__ = ["_RedOrdrCxlReq"]
		@property
		def RedOrdrCxlReq(self):
			return self._RedOrdrCxlReq

		@RedOrdrCxlReq.setter
		def RedOrdrCxlReq(self, value):
			self._RedOrdrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'RedOrdrCxlReq', RedemptionOrderCancellationRequestV04, False)

		@RedOrdrCxlReq.deleter
		def RedOrdrCxlReq(self):
			del self._RedOrdrCxlReq
			self._RedOrdrCxlReq = base_types.UninitialisedField(self, 'RedOrdrCxlReq', RedemptionOrderCancellationRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdrCxlReq', type=RedemptionOrderCancellationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))