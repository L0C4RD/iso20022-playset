from . import base_types
from ._SaleToPOIServiceResponseV08 import SaleToPOIServiceResponseV08

class CASP_002_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOISvcRspn"]
		@property
		def SaleToPOISvcRspn(self):
			return self._SaleToPOISvcRspn

		@SaleToPOISvcRspn.setter
		def SaleToPOISvcRspn(self, value):
			self._SaleToPOISvcRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOISvcRspn")

		@SaleToPOISvcRspn.deleter
		def SaleToPOISvcRspn(self):
			del self._SaleToPOISvcRspn
			self._SaleToPOISvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISvcRspn', type=SaleToPOIServiceResponseV08, min=1, max=1, mutex_group=None, array=False),
		))

