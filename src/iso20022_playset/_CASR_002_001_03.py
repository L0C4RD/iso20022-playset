# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementReportingResponseV03

class CASR_002_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casr.002.001.03"
		_docname = "casr.002.001.03"

		__slots__ = ["_SttlmRptgRspn"]
		@property
		def SttlmRptgRspn(self):
			return self._SttlmRptgRspn

		@SttlmRptgRspn.setter
		def SttlmRptgRspn(self, value):
			self._SttlmRptgRspn = value if value is not None else base_types.UninitialisedField(self, 'SttlmRptgRspn', SettlementReportingResponseV03, False)

		@SttlmRptgRspn.deleter
		def SttlmRptgRspn(self):
			del self._SttlmRptgRspn
			self._SttlmRptgRspn = base_types.UninitialisedField(self, 'SttlmRptgRspn', SettlementReportingResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmRptgRspn', type=SettlementReportingResponseV03, min=1, max=1, mutex_group=None, array=False),
		))