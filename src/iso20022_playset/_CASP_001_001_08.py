from . import base_types
from ._SaleToPOIServiceRequestV08 import SaleToPOIServiceRequestV08

class CASP_001_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOISvcReq"]
		@property
		def SaleToPOISvcReq(self):
			return self._SaleToPOISvcReq

		@SaleToPOISvcReq.setter
		def SaleToPOISvcReq(self, value):
			self._SaleToPOISvcReq = value if type(value) != base_types.auto else self.make_default("SaleToPOISvcReq")

		@SaleToPOISvcReq.deleter
		def SaleToPOISvcReq(self):
			del self._SaleToPOISvcReq
			self._SaleToPOISvcReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISvcReq', type=SaleToPOIServiceRequestV08, min=1, max=1, mutex_group=None, array=False),
		))

