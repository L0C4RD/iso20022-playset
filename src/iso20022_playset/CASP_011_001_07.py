from . import base_types
from .SaleToPOIAbortV07 import SaleToPOIAbortV07

class CASP_011_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIAbrt"]
		@property
		def SaleToPOIAbrt(self):
			return self._SaleToPOIAbrt

		@SaleToPOIAbrt.setter
		def SaleToPOIAbrt(self, value):
			self._SaleToPOIAbrt = value if type(value) != base_types.auto else self.make_default("SaleToPOIAbrt")

		@SaleToPOIAbrt.deleter
		def SaleToPOIAbrt(self):
			del self._SaleToPOIAbrt
			self._SaleToPOIAbrt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIAbrt', type=SaleToPOIAbortV07, min=1, max=1, mutex_group=None, array=False),
		))

