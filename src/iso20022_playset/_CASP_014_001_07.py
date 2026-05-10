from . import base_types
from ._SaleToPOIMessageStatusRequestV07 import SaleToPOIMessageStatusRequestV07

class CASP_014_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIMsgStsReq"]
		@property
		def SaleToPOIMsgStsReq(self):
			return self._SaleToPOIMsgStsReq

		@SaleToPOIMsgStsReq.setter
		def SaleToPOIMsgStsReq(self, value):
			self._SaleToPOIMsgStsReq = value if type(value) != base_types.auto else self.make_default("SaleToPOIMsgStsReq")

		@SaleToPOIMsgStsReq.deleter
		def SaleToPOIMsgStsReq(self):
			del self._SaleToPOIMsgStsReq
			self._SaleToPOIMsgStsReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIMsgStsReq', type=SaleToPOIMessageStatusRequestV07, min=1, max=1, mutex_group=None, array=False),
		))

