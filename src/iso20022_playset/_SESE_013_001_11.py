# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PortfolioTransferConfirmationV11

class SESE_013_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.013.001.11"
		_docname = "sese.013.001.11"

		__slots__ = ["_PrtflTrfConf"]
		@property
		def PrtflTrfConf(self):
			return self._PrtflTrfConf

		@PrtflTrfConf.setter
		def PrtflTrfConf(self, value):
			self._PrtflTrfConf = value if value is not None else base_types.UninitialisedField(self, 'PrtflTrfConf', PortfolioTransferConfirmationV11, False)

		@PrtflTrfConf.deleter
		def PrtflTrfConf(self):
			del self._PrtflTrfConf
			self._PrtflTrfConf = base_types.UninitialisedField(self, 'PrtflTrfConf', PortfolioTransferConfirmationV11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfConf', type=PortfolioTransferConfirmationV11, min=1, max=1, mutex_group=None, array=False),
		))