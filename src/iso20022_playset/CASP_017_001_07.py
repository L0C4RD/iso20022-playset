import base_types
import SaleToPOIDeviceResponseV07

class CASP_017_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIDvcRspn"]
		@property
		def SaleToPOIDvcRspn(self):
			return self._SaleToPOIDvcRspn

		@SaleToPOIDvcRspn.setter
		def SaleToPOIDvcRspn(self, value):
			self._SaleToPOIDvcRspn = value if type(value) != auto else self.make_default("SaleToPOIDvcRspn")

		@SaleToPOIDvcRspn.deleter
		def SaleToPOIDvcRspn(self):
			del self._SaleToPOIDvcRspn
			self._SaleToPOIDvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIDvcRspn', type=SaleToPOIDeviceResponseV07, min=1, max=1, mutex_group=None, array=False),
		))

