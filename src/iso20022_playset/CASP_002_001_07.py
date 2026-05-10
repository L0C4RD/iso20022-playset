from . import base_types
from .SaleToPOIServiceResponseV07 import SaleToPOIServiceResponseV07

class CASP_002_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOISvcRspn"]
		@property
		def SaleToPOISvcRspn(self):
			return self._SaleToPOISvcRspn

		@SaleToPOISvcRspn.setter
		def SaleToPOISvcRspn(self, value):
			self._SaleToPOISvcRspn = value if type(value) != auto else self.make_default("SaleToPOISvcRspn")

		@SaleToPOISvcRspn.deleter
		def SaleToPOISvcRspn(self):
			del self._SaleToPOISvcRspn
			self._SaleToPOISvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISvcRspn', type=SaleToPOIServiceResponseV07, min=1, max=1, mutex_group=None, array=False),
		))

