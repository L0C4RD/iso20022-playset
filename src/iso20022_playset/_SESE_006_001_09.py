# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransferInCancellationRequestV09

class SESE_006_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.006.001.09"
		_docname = "sese.006.001.09"

		__slots__ = ["_TrfInCxlReq"]
		@property
		def TrfInCxlReq(self):
			return self._TrfInCxlReq

		@TrfInCxlReq.setter
		def TrfInCxlReq(self, value):
			self._TrfInCxlReq = value if value is not None else base_types.UninitialisedField(self, 'TrfInCxlReq', TransferInCancellationRequestV09, False)

		@TrfInCxlReq.deleter
		def TrfInCxlReq(self):
			del self._TrfInCxlReq
			self._TrfInCxlReq = base_types.UninitialisedField(self, 'TrfInCxlReq', TransferInCancellationRequestV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfInCxlReq', type=TransferInCancellationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))