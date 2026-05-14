from . import base_types
from ._SecuritiesTransactionPostingReportV14 import SecuritiesTransactionPostingReportV14

class SEMT_017_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTxPstngRpt"]
		@property
		def SctiesTxPstngRpt(self):
			return self._SctiesTxPstngRpt

		@SctiesTxPstngRpt.setter
		def SctiesTxPstngRpt(self, value):
			self._SctiesTxPstngRpt = value if type(value) != base_types.auto else self.make_default("SctiesTxPstngRpt")

		@SctiesTxPstngRpt.deleter
		def SctiesTxPstngRpt(self):
			del self._SctiesTxPstngRpt
			self._SctiesTxPstngRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxPstngRpt', type=SecuritiesTransactionPostingReportV14, min=1, max=1, mutex_group=None, array=False),
		))

