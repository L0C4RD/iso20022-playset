# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PortfolioTransferNotification002V07

class SESE_037_002_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.037.002.07"
		_docname = "sese.037.002.07"

		__slots__ = ["_PrtflTrfNtfctn"]
		@property
		def PrtflTrfNtfctn(self):
			return self._PrtflTrfNtfctn

		@PrtflTrfNtfctn.setter
		def PrtflTrfNtfctn(self, value):
			self._PrtflTrfNtfctn = value if value is not None else base_types.UninitialisedField(self, 'PrtflTrfNtfctn', PortfolioTransferNotification002V07, False)

		@PrtflTrfNtfctn.deleter
		def PrtflTrfNtfctn(self):
			del self._PrtflTrfNtfctn
			self._PrtflTrfNtfctn = base_types.UninitialisedField(self, 'PrtflTrfNtfctn', PortfolioTransferNotification002V07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfNtfctn', type=PortfolioTransferNotification002V07, min=1, max=1, mutex_group=None, array=False),
		))