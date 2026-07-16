# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LiquidityCreditTransferV07

class CAMT_050_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.050.001.07"
		_docname = "camt.050.001.07"

		__slots__ = ["_LqdtyCdtTrf"]
		@property
		def LqdtyCdtTrf(self):
			return self._LqdtyCdtTrf

		@LqdtyCdtTrf.setter
		def LqdtyCdtTrf(self, value):
			self._LqdtyCdtTrf = value if value is not None else base_types.UninitialisedField(self, 'LqdtyCdtTrf', LiquidityCreditTransferV07, False)

		@LqdtyCdtTrf.deleter
		def LqdtyCdtTrf(self):
			del self._LqdtyCdtTrf
			self._LqdtyCdtTrf = base_types.UninitialisedField(self, 'LqdtyCdtTrf', LiquidityCreditTransferV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='LqdtyCdtTrf', type=LiquidityCreditTransferV07, min=1, max=1, mutex_group=None, array=False),
		))