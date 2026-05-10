from . import base_types
from .SettlementObligationReportV04 import SettlementObligationReportV04

class SECL_010_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SttlmOblgtnRpt"]
		@property
		def SttlmOblgtnRpt(self):
			return self._SttlmOblgtnRpt

		@SttlmOblgtnRpt.setter
		def SttlmOblgtnRpt(self, value):
			self._SttlmOblgtnRpt = value if type(value) != auto else self.make_default("SttlmOblgtnRpt")

		@SttlmOblgtnRpt.deleter
		def SttlmOblgtnRpt(self):
			del self._SttlmOblgtnRpt
			self._SttlmOblgtnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmOblgtnRpt', type=SettlementObligationReportV04, min=1, max=1, mutex_group=None, array=False),
		))

