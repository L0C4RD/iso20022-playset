# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyerProtectionInstructionReportRequestV01

class SEEV_066_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.066.001.01"
		_docname = "seev.066.001.01"

		__slots__ = ["_BuyrPrtcnInstrRptReq"]
		@property
		def BuyrPrtcnInstrRptReq(self):
			return self._BuyrPrtcnInstrRptReq

		@BuyrPrtcnInstrRptReq.setter
		def BuyrPrtcnInstrRptReq(self, value):
			self._BuyrPrtcnInstrRptReq = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstrRptReq', BuyerProtectionInstructionReportRequestV01, False)

		@BuyrPrtcnInstrRptReq.deleter
		def BuyrPrtcnInstrRptReq(self):
			del self._BuyrPrtcnInstrRptReq
			self._BuyrPrtcnInstrRptReq = base_types.UninitialisedField(self, 'BuyrPrtcnInstrRptReq', BuyerProtectionInstructionReportRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrRptReq', type=BuyerProtectionInstructionReportRequestV01, min=1, max=1, mutex_group=None, array=False),
		))