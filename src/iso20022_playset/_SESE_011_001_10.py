# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransferInstructionStatusReportV10

class SESE_011_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.011.001.10"
		_docname = "sese.011.001.10"

		__slots__ = ["_TrfInstrStsRpt"]
		@property
		def TrfInstrStsRpt(self):
			return self._TrfInstrStsRpt

		@TrfInstrStsRpt.setter
		def TrfInstrStsRpt(self, value):
			self._TrfInstrStsRpt = value if value is not None else base_types.UninitialisedField(self, 'TrfInstrStsRpt', TransferInstructionStatusReportV10, False)

		@TrfInstrStsRpt.deleter
		def TrfInstrStsRpt(self):
			del self._TrfInstrStsRpt
			self._TrfInstrStsRpt = base_types.UninitialisedField(self, 'TrfInstrStsRpt', TransferInstructionStatusReportV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfInstrStsRpt', type=TransferInstructionStatusReportV10, min=1, max=1, mutex_group=None, array=False),
		))