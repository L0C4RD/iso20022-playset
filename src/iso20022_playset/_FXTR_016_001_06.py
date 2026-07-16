# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeInstructionCancellationV06

class FXTR_016_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.016.001.06"
		_docname = "fxtr.016.001.06"

		__slots__ = ["_FXTradInstrCxl"]
		@property
		def FXTradInstrCxl(self):
			return self._FXTradInstrCxl

		@FXTradInstrCxl.setter
		def FXTradInstrCxl(self, value):
			self._FXTradInstrCxl = value if value is not None else base_types.UninitialisedField(self, 'FXTradInstrCxl', ForeignExchangeTradeInstructionCancellationV06, False)

		@FXTradInstrCxl.deleter
		def FXTradInstrCxl(self):
			del self._FXTradInstrCxl
			self._FXTradInstrCxl = base_types.UninitialisedField(self, 'FXTradInstrCxl', ForeignExchangeTradeInstructionCancellationV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradInstrCxl', type=ForeignExchangeTradeInstructionCancellationV06, min=1, max=1, mutex_group=None, array=False),
		))