import base_types
import SecurityMaintenanceStatusAdviceV01

class REDA_029_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyMntncStsAdvc"]
		@property
		def SctyMntncStsAdvc(self):
			return self._SctyMntncStsAdvc

		@SctyMntncStsAdvc.setter
		def SctyMntncStsAdvc(self, value):
			self._SctyMntncStsAdvc = value if type(value) != auto else self.make_default("SctyMntncStsAdvc")

		@SctyMntncStsAdvc.deleter
		def SctyMntncStsAdvc(self):
			del self._SctyMntncStsAdvc
			self._SctyMntncStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyMntncStsAdvc', type=SecurityMaintenanceStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

