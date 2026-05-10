from . import base_types
import SaleToPOIDeviceRequestV07

class CASP_016_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIDvcReq"]
		@property
		def SaleToPOIDvcReq(self):
			return self._SaleToPOIDvcReq

		@SaleToPOIDvcReq.setter
		def SaleToPOIDvcReq(self, value):
			self._SaleToPOIDvcReq = value if type(value) != auto else self.make_default("SaleToPOIDvcReq")

		@SaleToPOIDvcReq.deleter
		def SaleToPOIDvcReq(self):
			del self._SaleToPOIDvcReq
			self._SaleToPOIDvcReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIDvcReq', type=SaleToPOIDeviceRequestV07, min=1, max=1, mutex_group=None, array=False),
		))

