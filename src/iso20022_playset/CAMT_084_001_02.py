from . import base_types
from .IntraBalanceMovementPostingReportV02 import IntraBalanceMovementPostingReportV02

class CAMT_084_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntPstngRpt"]
		@property
		def IntraBalMvmntPstngRpt(self):
			return self._IntraBalMvmntPstngRpt

		@IntraBalMvmntPstngRpt.setter
		def IntraBalMvmntPstngRpt(self, value):
			self._IntraBalMvmntPstngRpt = value if type(value) != auto else self.make_default("IntraBalMvmntPstngRpt")

		@IntraBalMvmntPstngRpt.deleter
		def IntraBalMvmntPstngRpt(self):
			del self._IntraBalMvmntPstngRpt
			self._IntraBalMvmntPstngRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntPstngRpt', type=IntraBalanceMovementPostingReportV02, min=1, max=1, mutex_group=None, array=False),
		))

