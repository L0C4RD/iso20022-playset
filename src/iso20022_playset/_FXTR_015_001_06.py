# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeInstructionAmendmentV06

class FXTR_015_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.015.001.06"
		_docname = "fxtr.015.001.06"

		__slots__ = ["_FXTradInstrAmdmnt"]
		@property
		def FXTradInstrAmdmnt(self):
			return self._FXTradInstrAmdmnt

		@FXTradInstrAmdmnt.setter
		def FXTradInstrAmdmnt(self, value):
			self._FXTradInstrAmdmnt = value if value is not None else base_types.UninitialisedField(self, 'FXTradInstrAmdmnt', ForeignExchangeTradeInstructionAmendmentV06, False)

		@FXTradInstrAmdmnt.deleter
		def FXTradInstrAmdmnt(self):
			del self._FXTradInstrAmdmnt
			self._FXTradInstrAmdmnt = base_types.UninitialisedField(self, 'FXTradInstrAmdmnt', ForeignExchangeTradeInstructionAmendmentV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradInstrAmdmnt', type=ForeignExchangeTradeInstructionAmendmentV06, min=1, max=1, mutex_group=None, array=False),
		))