from . import base_types
from .InvestmentAccountOwnershipInformation17 import InvestmentAccountOwnershipInformation17

class AccountParties13Choice(base_types._BaseFieldType):

	__slots__ = ["_JntOwnr", "_PmryOwnr", "_Nmnee", "_Trstee"]
	@property
	def JntOwnr(self):
		return self._JntOwnr

	@JntOwnr.setter
	def JntOwnr(self, value):
		self._JntOwnr = value if type(value) != base_types.auto else self.make_default("JntOwnr")

	@JntOwnr.deleter
	def JntOwnr(self):
		del self._JntOwnr
		self._JntOwnr = None

	@property
	def PmryOwnr(self):
		return self._PmryOwnr

	@PmryOwnr.setter
	def PmryOwnr(self, value):
		self._PmryOwnr = value if type(value) != base_types.auto else self.make_default("PmryOwnr")

	@PmryOwnr.deleter
	def PmryOwnr(self):
		del self._PmryOwnr
		self._PmryOwnr = None

	@property
	def Nmnee(self):
		return self._Nmnee

	@Nmnee.setter
	def Nmnee(self, value):
		self._Nmnee = value if type(value) != base_types.auto else self.make_default("Nmnee")

	@Nmnee.deleter
	def Nmnee(self):
		del self._Nmnee
		self._Nmnee = None

	@property
	def Trstee(self):
		return self._Trstee

	@Trstee.setter
	def Trstee(self, value):
		self._Trstee = value if type(value) != base_types.auto else self.make_default("Trstee")

	@Trstee.deleter
	def Trstee(self):
		del self._Trstee
		self._Trstee = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='JntOwnr', type=InvestmentAccountOwnershipInformation17, min=1, max=5, mutex_group=1, array=True),
		base_types.FieldEntry(name='PmryOwnr', type=InvestmentAccountOwnershipInformation17, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nmnee', type=InvestmentAccountOwnershipInformation17, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Trstee', type=InvestmentAccountOwnershipInformation17, min=1, max=5, mutex_group=1, array=True),
	))

