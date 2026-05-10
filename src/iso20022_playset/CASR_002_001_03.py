from . import base_types
import SettlementReportingResponseV03

class CASR_002_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SttlmRptgRspn"]
		@property
		def SttlmRptgRspn(self):
			return self._SttlmRptgRspn

		@SttlmRptgRspn.setter
		def SttlmRptgRspn(self, value):
			self._SttlmRptgRspn = value if type(value) != auto else self.make_default("SttlmRptgRspn")

		@SttlmRptgRspn.deleter
		def SttlmRptgRspn(self):
			del self._SttlmRptgRspn
			self._SttlmRptgRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmRptgRspn', type=SettlementReportingResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

