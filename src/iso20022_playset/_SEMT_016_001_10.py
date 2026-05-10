from . import base_types
from .IntraPositionMovementPostingReportV10 import IntraPositionMovementPostingReportV10

class SEMT_016_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraPosMvmntPstngRpt"]
		@property
		def IntraPosMvmntPstngRpt(self):
			return self._IntraPosMvmntPstngRpt

		@IntraPosMvmntPstngRpt.setter
		def IntraPosMvmntPstngRpt(self, value):
			self._IntraPosMvmntPstngRpt = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntPstngRpt")

		@IntraPosMvmntPstngRpt.deleter
		def IntraPosMvmntPstngRpt(self):
			del self._IntraPosMvmntPstngRpt
			self._IntraPosMvmntPstngRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntPstngRpt', type=IntraPositionMovementPostingReportV10, min=1, max=1, mutex_group=None, array=False),
		))

