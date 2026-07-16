# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PortfolioTransferCompletionV02

class SESE_043_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.043.001.02"
		_docname = "sese.043.001.02"

		__slots__ = ["_PrtflTrfCmpltn"]
		@property
		def PrtflTrfCmpltn(self):
			return self._PrtflTrfCmpltn

		@PrtflTrfCmpltn.setter
		def PrtflTrfCmpltn(self, value):
			self._PrtflTrfCmpltn = value if value is not None else base_types.UninitialisedField(self, 'PrtflTrfCmpltn', PortfolioTransferCompletionV02, False)

		@PrtflTrfCmpltn.deleter
		def PrtflTrfCmpltn(self):
			del self._PrtflTrfCmpltn
			self._PrtflTrfCmpltn = base_types.UninitialisedField(self, 'PrtflTrfCmpltn', PortfolioTransferCompletionV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfCmpltn', type=PortfolioTransferCompletionV02, min=1, max=1, mutex_group=None, array=False),
		))