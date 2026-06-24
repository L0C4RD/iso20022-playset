# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PortfolioTransferInstructionV11 import PortfolioTransferInstructionV11

class SESE_012_001_11():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:sese.012.001.11",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_PrtflTrfInstr"]
		@property
		def PrtflTrfInstr(self):
			return self._PrtflTrfInstr

		@PrtflTrfInstr.setter
		def PrtflTrfInstr(self, value):
			self._PrtflTrfInstr = value if type(value) != base_types.auto else self.make_default("PrtflTrfInstr")

		@PrtflTrfInstr.deleter
		def PrtflTrfInstr(self):
			del self._PrtflTrfInstr
			self._PrtflTrfInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfInstr', type=PortfolioTransferInstructionV11, min=1, max=1, mutex_group=None, array=False),
		))