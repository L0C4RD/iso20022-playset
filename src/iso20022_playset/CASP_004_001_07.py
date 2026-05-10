from . import base_types
from .SaleToPOIReconciliationResponseV07 import SaleToPOIReconciliationResponseV07

class CASP_004_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIRcncltnRspn"]
		@property
		def SaleToPOIRcncltnRspn(self):
			return self._SaleToPOIRcncltnRspn

		@SaleToPOIRcncltnRspn.setter
		def SaleToPOIRcncltnRspn(self, value):
			self._SaleToPOIRcncltnRspn = value if type(value) != auto else self.make_default("SaleToPOIRcncltnRspn")

		@SaleToPOIRcncltnRspn.deleter
		def SaleToPOIRcncltnRspn(self):
			del self._SaleToPOIRcncltnRspn
			self._SaleToPOIRcncltnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRcncltnRspn', type=SaleToPOIReconciliationResponseV07, min=1, max=1, mutex_group=None, array=False),
		))

