from . import base_types
from .SaleToPOIAdministrativeRequestV07 import SaleToPOIAdministrativeRequestV07

class CASP_007_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIAdmstvReq"]
		@property
		def SaleToPOIAdmstvReq(self):
			return self._SaleToPOIAdmstvReq

		@SaleToPOIAdmstvReq.setter
		def SaleToPOIAdmstvReq(self, value):
			self._SaleToPOIAdmstvReq = value if type(value) != base_types.auto else self.make_default("SaleToPOIAdmstvReq")

		@SaleToPOIAdmstvReq.deleter
		def SaleToPOIAdmstvReq(self):
			del self._SaleToPOIAdmstvReq
			self._SaleToPOIAdmstvReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIAdmstvReq', type=SaleToPOIAdministrativeRequestV07, min=1, max=1, mutex_group=None, array=False),
		))

