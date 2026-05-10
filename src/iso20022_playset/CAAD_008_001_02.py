from . import base_types
from .AdministrativeInitiationV02 import AdministrativeInitiationV02

class CAAD_008_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AdmstvInitn"]
		@property
		def AdmstvInitn(self):
			return self._AdmstvInitn

		@AdmstvInitn.setter
		def AdmstvInitn(self, value):
			self._AdmstvInitn = value if type(value) != base_types.auto else self.make_default("AdmstvInitn")

		@AdmstvInitn.deleter
		def AdmstvInitn(self):
			del self._AdmstvInitn
			self._AdmstvInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdmstvInitn', type=AdministrativeInitiationV02, min=1, max=1, mutex_group=None, array=False),
		))

