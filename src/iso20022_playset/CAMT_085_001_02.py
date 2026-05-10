from . import base_types
from .IntraBalanceMovementPendingReportV02 import IntraBalanceMovementPendingReportV02

class CAMT_085_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntPdgRpt"]
		@property
		def IntraBalMvmntPdgRpt(self):
			return self._IntraBalMvmntPdgRpt

		@IntraBalMvmntPdgRpt.setter
		def IntraBalMvmntPdgRpt(self, value):
			self._IntraBalMvmntPdgRpt = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntPdgRpt")

		@IntraBalMvmntPdgRpt.deleter
		def IntraBalMvmntPdgRpt(self):
			del self._IntraBalMvmntPdgRpt
			self._IntraBalMvmntPdgRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntPdgRpt', type=IntraBalanceMovementPendingReportV02, min=1, max=1, mutex_group=None, array=False),
		))

