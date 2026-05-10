from . import base_types
from .Max35Text import Max35Text
from .AccountIdentification26 import AccountIdentification26

class SubAccount4(base_types._BaseFieldType):

	__slots__ = ["_Chrtc", "_Nm", "_Id"]
	@property
	def Chrtc(self):
		return self._Chrtc

	@Chrtc.setter
	def Chrtc(self, value):
		self._Chrtc = value if type(value) != auto else self.make_default("Chrtc")

	@Chrtc.deleter
	def Chrtc(self):
		del self._Chrtc
		self._Chrtc = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chrtc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentification26, min=1, max=1, mutex_group=None, array=False),
	))

