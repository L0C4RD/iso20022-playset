# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PortfolioTransferInstructionV12

class SESE_012_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.012.001.12"
		_docname = "sese.012.001.12"

		__slots__ = ["_PrtflTrfInstr"]
		@property
		def PrtflTrfInstr(self):
			return self._PrtflTrfInstr

		@PrtflTrfInstr.setter
		def PrtflTrfInstr(self, value):
			self._PrtflTrfInstr = value if value is not None else base_types.UninitialisedField(self, 'PrtflTrfInstr', PortfolioTransferInstructionV12, False)

		@PrtflTrfInstr.deleter
		def PrtflTrfInstr(self):
			del self._PrtflTrfInstr
			self._PrtflTrfInstr = base_types.UninitialisedField(self, 'PrtflTrfInstr', PortfolioTransferInstructionV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfInstr', type=PortfolioTransferInstructionV12, min=1, max=1, mutex_group=None, array=False),
		))