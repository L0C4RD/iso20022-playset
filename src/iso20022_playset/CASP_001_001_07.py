import base_types
import SaleToPOIServiceRequestV07

class CASP_001_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOISvcReq"]
		@property
		def SaleToPOISvcReq(self):
			return self._SaleToPOISvcReq

		@SaleToPOISvcReq.setter
		def SaleToPOISvcReq(self, value):
			self._SaleToPOISvcReq = value if type(value) != auto else self.make_default("SaleToPOISvcReq")

		@SaleToPOISvcReq.deleter
		def SaleToPOISvcReq(self):
			del self._SaleToPOISvcReq
			self._SaleToPOISvcReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISvcReq', type=SaleToPOIServiceRequestV07, min=1, max=1, mutex_group=None, array=False),
		))

