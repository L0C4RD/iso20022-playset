from . import base_types
from .SecuritiesAccountReportV01 import SecuritiesAccountReportV01

class REDA_021_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAcctRpt"]
		@property
		def SctiesAcctRpt(self):
			return self._SctiesAcctRpt

		@SctiesAcctRpt.setter
		def SctiesAcctRpt(self, value):
			self._SctiesAcctRpt = value if type(value) != base_types.auto else self.make_default("SctiesAcctRpt")

		@SctiesAcctRpt.deleter
		def SctiesAcctRpt(self):
			del self._SctiesAcctRpt
			self._SctiesAcctRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctRpt', type=SecuritiesAccountReportV01, min=1, max=1, mutex_group=None, array=False),
		))

