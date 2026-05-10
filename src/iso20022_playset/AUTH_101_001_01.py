from . import base_types
from .SettlementFailsAnnualReportV01 import SettlementFailsAnnualReportV01

class AUTH_101_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SttlmFlsAnlRpt"]
		@property
		def SttlmFlsAnlRpt(self):
			return self._SttlmFlsAnlRpt

		@SttlmFlsAnlRpt.setter
		def SttlmFlsAnlRpt(self, value):
			self._SttlmFlsAnlRpt = value if type(value) != auto else self.make_default("SttlmFlsAnlRpt")

		@SttlmFlsAnlRpt.deleter
		def SttlmFlsAnlRpt(self):
			del self._SttlmFlsAnlRpt
			self._SttlmFlsAnlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmFlsAnlRpt', type=SettlementFailsAnnualReportV01, min=1, max=1, mutex_group=None, array=False),
		))

