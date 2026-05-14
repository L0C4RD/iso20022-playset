from . import base_types
from ._SaleToPOIDeviceResponseV08 import SaleToPOIDeviceResponseV08

class CASP_017_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIDvcRspn"]
		@property
		def SaleToPOIDvcRspn(self):
			return self._SaleToPOIDvcRspn

		@SaleToPOIDvcRspn.setter
		def SaleToPOIDvcRspn(self, value):
			self._SaleToPOIDvcRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOIDvcRspn")

		@SaleToPOIDvcRspn.deleter
		def SaleToPOIDvcRspn(self):
			del self._SaleToPOIDvcRspn
			self._SaleToPOIDvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIDvcRspn', type=SaleToPOIDeviceResponseV08, min=1, max=1, mutex_group=None, array=False),
		))

