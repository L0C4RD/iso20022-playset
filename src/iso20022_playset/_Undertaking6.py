from . import base_types
from ._Max35Text import Max35Text
from ._PartyIdentification43 import PartyIdentification43

class Undertaking6(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_BnfcryRefNb", "_Id"]
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
	def BnfcryRefNb(self):
		return self._BnfcryRefNb

	@BnfcryRefNb.setter
	def BnfcryRefNb(self, value):
		self._BnfcryRefNb = value if type(value) != base_types.auto else self.make_default("BnfcryRefNb")

	@BnfcryRefNb.deleter
	def BnfcryRefNb(self):
		del self._BnfcryRefNb
		self._BnfcryRefNb = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

