from . import base_types
from .AdministrativeResponseV02 import AdministrativeResponseV02

class CAAD_009_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AdmstvRspn"]
		@property
		def AdmstvRspn(self):
			return self._AdmstvRspn

		@AdmstvRspn.setter
		def AdmstvRspn(self, value):
			self._AdmstvRspn = value if type(value) != base_types.auto else self.make_default("AdmstvRspn")

		@AdmstvRspn.deleter
		def AdmstvRspn(self):
			del self._AdmstvRspn
			self._AdmstvRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdmstvRspn', type=AdministrativeResponseV02, min=1, max=1, mutex_group=None, array=False),
		))

