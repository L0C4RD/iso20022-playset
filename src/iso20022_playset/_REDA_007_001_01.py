from . import base_types
from ._SecurityMaintenanceRequestV01 import SecurityMaintenanceRequestV01

class REDA_007_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyMntncReq"]
		@property
		def SctyMntncReq(self):
			return self._SctyMntncReq

		@SctyMntncReq.setter
		def SctyMntncReq(self, value):
			self._SctyMntncReq = value if type(value) != base_types.auto else self.make_default("SctyMntncReq")

		@SctyMntncReq.deleter
		def SctyMntncReq(self):
			del self._SctyMntncReq
			self._SctyMntncReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyMntncReq', type=SecurityMaintenanceRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

