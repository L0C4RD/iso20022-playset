# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForeignExchangeTradeInstructionAmendmentV06 import ForeignExchangeTradeInstructionAmendmentV06

class FXTR_015_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradInstrAmdmnt"]
		@property
		def FXTradInstrAmdmnt(self):
			return self._FXTradInstrAmdmnt

		@FXTradInstrAmdmnt.setter
		def FXTradInstrAmdmnt(self, value):
			self._FXTradInstrAmdmnt = value if type(value) != base_types.auto else self.make_default("FXTradInstrAmdmnt")

		@FXTradInstrAmdmnt.deleter
		def FXTradInstrAmdmnt(self):
			del self._FXTradInstrAmdmnt
			self._FXTradInstrAmdmnt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradInstrAmdmnt', type=ForeignExchangeTradeInstructionAmendmentV06, min=1, max=1, mutex_group=None, array=False),
		))