from . import base_types
from ._PartyIdentificationAndAccount178 import PartyIdentificationAndAccount178
from ._PartyIdentificationAndAccount177 import PartyIdentificationAndAccount177

class CashParties38(base_types._BaseFieldType):

	__slots__ = ["_CdtrAgt", "_DbtrAgt", "_Dbtr", "_Cdtr", "_Intrmy"]
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
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != base_types.auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != base_types.auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

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
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if type(value) != base_types.auto else self.make_default("Intrmy")

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrAgt', type=PartyIdentificationAndAccount178, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=PartyIdentificationAndAccount178, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentificationAndAccount177, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentificationAndAccount177, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy', type=PartyIdentificationAndAccount178, min=0, max=1, mutex_group=None, array=False),
	))

