from . import base_types
from ._SaleToPOIAdministrativeResponseV08 import SaleToPOIAdministrativeResponseV08

class CASP_008_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIAdmstvRspn"]
		@property
		def SaleToPOIAdmstvRspn(self):
			return self._SaleToPOIAdmstvRspn

		@SaleToPOIAdmstvRspn.setter
		def SaleToPOIAdmstvRspn(self, value):
			self._SaleToPOIAdmstvRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOIAdmstvRspn")

		@SaleToPOIAdmstvRspn.deleter
		def SaleToPOIAdmstvRspn(self):
			del self._SaleToPOIAdmstvRspn
			self._SaleToPOIAdmstvRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIAdmstvRspn', type=SaleToPOIAdministrativeResponseV08, min=1, max=1, mutex_group=None, array=False),
		))

