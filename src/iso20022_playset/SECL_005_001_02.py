from . import base_types
from .MarginReportV02 import MarginReportV02

class SECL_005_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MrgnRpt"]
		@property
		def MrgnRpt(self):
			return self._MrgnRpt

		@MrgnRpt.setter
		def MrgnRpt(self, value):
			self._MrgnRpt = value if type(value) != base_types.auto else self.make_default("MrgnRpt")

		@MrgnRpt.deleter
		def MrgnRpt(self):
			del self._MrgnRpt
			self._MrgnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MrgnRpt', type=MarginReportV02, min=1, max=1, mutex_group=None, array=False),
		))

