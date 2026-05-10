from . import base_types
import SaleToPOIMessageStatusResponseV07

class CASP_015_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIMsgStsRspn"]
		@property
		def SaleToPOIMsgStsRspn(self):
			return self._SaleToPOIMsgStsRspn

		@SaleToPOIMsgStsRspn.setter
		def SaleToPOIMsgStsRspn(self, value):
			self._SaleToPOIMsgStsRspn = value if type(value) != auto else self.make_default("SaleToPOIMsgStsRspn")

		@SaleToPOIMsgStsRspn.deleter
		def SaleToPOIMsgStsRspn(self):
			del self._SaleToPOIMsgStsRspn
			self._SaleToPOIMsgStsRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIMsgStsRspn', type=SaleToPOIMessageStatusResponseV07, min=1, max=1, mutex_group=None, array=False),
		))

