# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PortfolioTransferCancellationRequestV09

class SESE_014_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09"
		_docname = "sese.014.001.09"

		__slots__ = ["_PrtflTrfCxlReq"]
		@property
		def PrtflTrfCxlReq(self):
			return self._PrtflTrfCxlReq

		@PrtflTrfCxlReq.setter
		def PrtflTrfCxlReq(self, value):
			self._PrtflTrfCxlReq = value if value is not None else base_types.UninitialisedField(self, 'PrtflTrfCxlReq', PortfolioTransferCancellationRequestV09, False)

		@PrtflTrfCxlReq.deleter
		def PrtflTrfCxlReq(self):
			del self._PrtflTrfCxlReq
			self._PrtflTrfCxlReq = base_types.UninitialisedField(self, 'PrtflTrfCxlReq', PortfolioTransferCancellationRequestV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfCxlReq', type=PortfolioTransferCancellationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))