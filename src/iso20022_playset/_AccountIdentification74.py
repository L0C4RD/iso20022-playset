from . import base_types
from ._CorporateActionEventAndBalance27 import CorporateActionEventAndBalance27
from ._RestrictedFINXMax140Text import RestrictedFINXMax140Text
from ._PartyIdentification136Choice import PartyIdentification136Choice
from ._SafekeepingPlaceFormat46Choice import SafekeepingPlaceFormat46Choice
from ._RestrictedFINXMax35Text import RestrictedFINXMax35Text

class AccountIdentification74(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_SfkpgPlc", "_SfkpgAcct", "_CorpActnEvtAndBal", "_AcctOwnr"]
	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def CorpActnEvtAndBal(self):
		return self._CorpActnEvtAndBal

	@CorpActnEvtAndBal.setter
	def CorpActnEvtAndBal(self, value):
		self._CorpActnEvtAndBal = value if type(value) != base_types.auto else self.make_default("CorpActnEvtAndBal")

	@CorpActnEvtAndBal.deleter
	def CorpActnEvtAndBal(self):
		del self._CorpActnEvtAndBal
		self._CorpActnEvtAndBal = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat46Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtAndBal', type=CorporateActionEventAndBalance27, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136Choice, min=0, max=1, mutex_group=None, array=False),
	))

