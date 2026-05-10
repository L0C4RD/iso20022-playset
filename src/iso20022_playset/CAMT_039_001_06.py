from . import base_types
from .CaseStatusReportV06 import CaseStatusReportV06

class CAMT_039_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CaseStsRpt"]
		@property
		def CaseStsRpt(self):
			return self._CaseStsRpt

		@CaseStsRpt.setter
		def CaseStsRpt(self, value):
			self._CaseStsRpt = value if type(value) != auto else self.make_default("CaseStsRpt")

		@CaseStsRpt.deleter
		def CaseStsRpt(self):
			del self._CaseStsRpt
			self._CaseStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CaseStsRpt', type=CaseStatusReportV06, min=1, max=1, mutex_group=None, array=False),
		))

