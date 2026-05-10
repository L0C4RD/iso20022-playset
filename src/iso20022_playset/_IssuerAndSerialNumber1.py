from . import base_types
from ._CertificateIssuer1 import CertificateIssuer1
from ._Max35Binary import Max35Binary

class IssuerAndSerialNumber1(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_SrlNb"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if type(value) != base_types.auto else self.make_default("SrlNb")

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=CertificateIssuer1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Binary, min=1, max=1, mutex_group=None, array=False),
	))

