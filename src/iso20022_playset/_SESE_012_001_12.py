# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PortfolioTransferInstructionV12 import PortfolioTransferInstructionV12

class SESE_012_001_12():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.012.001.12"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
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
			base_types.FieldEntry(name='PrtflTrfInstr', type=PortfolioTransferInstructionV12, min=1, max=1, mutex_group=None, array=False),
		))