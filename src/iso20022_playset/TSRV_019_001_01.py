from . import base_types
from .UndertakingStatusReportV01 import UndertakingStatusReportV01

class TSRV_019_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgStsRpt"]
		@property
		def UdrtkgStsRpt(self):
			return self._UdrtkgStsRpt

		@UdrtkgStsRpt.setter
		def UdrtkgStsRpt(self, value):
			self._UdrtkgStsRpt = value if type(value) != auto else self.make_default("UdrtkgStsRpt")

		@UdrtkgStsRpt.deleter
		def UdrtkgStsRpt(self):
			del self._UdrtkgStsRpt
			self._UdrtkgStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgStsRpt', type=UndertakingStatusReportV01, min=1, max=1, mutex_group=None, array=False),
		))

