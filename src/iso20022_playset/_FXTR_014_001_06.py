# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeInstructionV06

class FXTR_014_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.06"
		_docname = "fxtr.014.001.06"

		__slots__ = ["_FXTradInstr"]
		@property
		def FXTradInstr(self):
			return self._FXTradInstr

		@FXTradInstr.setter
		def FXTradInstr(self, value):
			self._FXTradInstr = value if value is not None else base_types.UninitialisedField(self, 'FXTradInstr', ForeignExchangeTradeInstructionV06, False)

		@FXTradInstr.deleter
		def FXTradInstr(self):
			del self._FXTradInstr
			self._FXTradInstr = base_types.UninitialisedField(self, 'FXTradInstr', ForeignExchangeTradeInstructionV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradInstr', type=ForeignExchangeTradeInstructionV06, min=1, max=1, mutex_group=None, array=False),
		))