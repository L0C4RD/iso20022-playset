from . import base_types
import IntraBalanceMovementCancellationReportV02

class CAMT_083_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntCxlRpt"]
		@property
		def IntraBalMvmntCxlRpt(self):
			return self._IntraBalMvmntCxlRpt

		@IntraBalMvmntCxlRpt.setter
		def IntraBalMvmntCxlRpt(self, value):
			self._IntraBalMvmntCxlRpt = value if type(value) != auto else self.make_default("IntraBalMvmntCxlRpt")

		@IntraBalMvmntCxlRpt.deleter
		def IntraBalMvmntCxlRpt(self):
			del self._IntraBalMvmntCxlRpt
			self._IntraBalMvmntCxlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlRpt', type=IntraBalanceMovementCancellationReportV02, min=1, max=1, mutex_group=None, array=False),
		))

