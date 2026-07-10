# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SettlementReportingResponseV04 import SettlementReportingResponseV04

class CASR_002_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casr.002.001.04"
		_docname = "casr.002.001.04"

		__slots__ = ["_SttlmRptgRspn"]
		@property
		def SttlmRptgRspn(self):
			return self._SttlmRptgRspn

		@SttlmRptgRspn.setter
		def SttlmRptgRspn(self, value):
			self._SttlmRptgRspn = value if type(value) != base_types.auto else self.make_default("SttlmRptgRspn")

		@SttlmRptgRspn.deleter
		def SttlmRptgRspn(self):
			del self._SttlmRptgRspn
			self._SttlmRptgRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmRptgRspn', type=SettlementReportingResponseV04, min=1, max=1, mutex_group=None, array=False),
		))