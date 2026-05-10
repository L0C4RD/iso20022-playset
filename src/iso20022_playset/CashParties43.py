from . import base_types
from .PartyIdentificationAndAccount226 import PartyIdentificationAndAccount226
from .PartyIdentificationAndAccount225 import PartyIdentificationAndAccount225

class CashParties43(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_MktClmCtrPty", "_CdtrAgt"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != base_types.auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def MktClmCtrPty(self):
		return self._MktClmCtrPty

	@MktClmCtrPty.setter
	def MktClmCtrPty(self, value):
		self._MktClmCtrPty = value if type(value) != base_types.auto else self.make_default("MktClmCtrPty")

	@MktClmCtrPty.deleter
	def MktClmCtrPty(self):
		del self._MktClmCtrPty
		self._MktClmCtrPty = None

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != base_types.auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentificationAndAccount225, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmCtrPty', type=PartyIdentificationAndAccount225, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=PartyIdentificationAndAccount226, min=0, max=1, mutex_group=None, array=False),
	))

