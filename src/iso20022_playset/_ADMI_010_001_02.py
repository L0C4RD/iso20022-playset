from . import base_types
from ._StaticDataReportV02 import StaticDataReportV02

class ADMI_010_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StatcDataRpt"]
		@property
		def StatcDataRpt(self):
			return self._StatcDataRpt

		@StatcDataRpt.setter
		def StatcDataRpt(self, value):
			self._StatcDataRpt = value if type(value) != base_types.auto else self.make_default("StatcDataRpt")

		@StatcDataRpt.deleter
		def StatcDataRpt(self):
			del self._StatcDataRpt
			self._StatcDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StatcDataRpt', type=StaticDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))

