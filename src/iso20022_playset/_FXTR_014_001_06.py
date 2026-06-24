# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForeignExchangeTradeInstructionV06 import ForeignExchangeTradeInstructionV06

class FXTR_014_001_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.06",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_FXTradInstr"]
		@property
		def FXTradInstr(self):
			return self._FXTradInstr

		@FXTradInstr.setter
		def FXTradInstr(self, value):
			self._FXTradInstr = value if type(value) != base_types.auto else self.make_default("FXTradInstr")

		@FXTradInstr.deleter
		def FXTradInstr(self):
			del self._FXTradInstr
			self._FXTradInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradInstr', type=ForeignExchangeTradeInstructionV06, min=1, max=1, mutex_group=None, array=False),
		))