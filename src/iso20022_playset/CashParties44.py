from . import base_types
from .PartyIdentificationAndAccount232 import PartyIdentificationAndAccount232
from .PartyIdentificationAndAccount231 import PartyIdentificationAndAccount231

class CashParties44(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAgt", "_MktClmCtrPty"]
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
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != base_types.auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentificationAndAccount231, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=PartyIdentificationAndAccount232, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmCtrPty', type=PartyIdentificationAndAccount231, min=0, max=1, mutex_group=None, array=False),
	))

