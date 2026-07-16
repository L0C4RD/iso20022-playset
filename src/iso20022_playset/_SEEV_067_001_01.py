# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyerProtectionInstructionReportV01

class SEEV_067_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.067.001.01"
		_docname = "seev.067.001.01"

		__slots__ = ["_BuyrPrtcnInstrRpt"]
		@property
		def BuyrPrtcnInstrRpt(self):
			return self._BuyrPrtcnInstrRpt

		@BuyrPrtcnInstrRpt.setter
		def BuyrPrtcnInstrRpt(self, value):
			self._BuyrPrtcnInstrRpt = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstrRpt', BuyerProtectionInstructionReportV01, False)

		@BuyrPrtcnInstrRpt.deleter
		def BuyrPrtcnInstrRpt(self):
			del self._BuyrPrtcnInstrRpt
			self._BuyrPrtcnInstrRpt = base_types.UninitialisedField(self, 'BuyrPrtcnInstrRpt', BuyerProtectionInstructionReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrRpt', type=BuyerProtectionInstructionReportV01, min=1, max=1, mutex_group=None, array=False),
		))