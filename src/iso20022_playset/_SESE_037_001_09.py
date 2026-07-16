# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PortfolioTransferNotificationV09

class SESE_037_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.037.001.09"
		_docname = "sese.037.001.09"

		__slots__ = ["_PrtflTrfNtfctn"]
		@property
		def PrtflTrfNtfctn(self):
			return self._PrtflTrfNtfctn

		@PrtflTrfNtfctn.setter
		def PrtflTrfNtfctn(self, value):
			self._PrtflTrfNtfctn = value if value is not None else base_types.UninitialisedField(self, 'PrtflTrfNtfctn', PortfolioTransferNotificationV09, False)

		@PrtflTrfNtfctn.deleter
		def PrtflTrfNtfctn(self):
			del self._PrtflTrfNtfctn
			self._PrtflTrfNtfctn = base_types.UninitialisedField(self, 'PrtflTrfNtfctn', PortfolioTransferNotificationV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfNtfctn', type=PortfolioTransferNotificationV09, min=1, max=1, mutex_group=None, array=False),
		))