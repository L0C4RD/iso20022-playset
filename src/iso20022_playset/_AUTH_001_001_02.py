from . import base_types
from .InformationRequestOpeningV02 import InformationRequestOpeningV02

class AUTH_001_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InfReqOpng"]
		@property
		def InfReqOpng(self):
			return self._InfReqOpng

		@InfReqOpng.setter
		def InfReqOpng(self, value):
			self._InfReqOpng = value if type(value) != base_types.auto else self.make_default("InfReqOpng")

		@InfReqOpng.deleter
		def InfReqOpng(self):
			del self._InfReqOpng
			self._InfReqOpng = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InfReqOpng', type=InformationRequestOpeningV02, min=1, max=1, mutex_group=None, array=False),
		))

