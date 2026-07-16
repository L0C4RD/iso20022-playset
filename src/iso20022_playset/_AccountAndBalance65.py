# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionBalanceDetails46
from . import PartyIdentification136Choice
from . import RestrictedFINXMax140Text
from . import RestrictedFINXMax35Text
from . import SafekeepingPlaceFormat55Choice

class AccountAndBalance65(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_Bal", "_BlckChainAdrOrWllt", "_SfkpgAcct", "_SfkpgPlc"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification136Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification136Choice, False)

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', CorporateActionBalanceDetails46, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', CorporateActionBalanceDetails46, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', RestrictedFINXMax140Text, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', RestrictedFINXMax140Text, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', RestrictedFINXMax35Text, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', RestrictedFINXMax35Text, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat55Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat55Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=CorporateActionBalanceDetails46, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat55Choice, min=0, max=1, mutex_group=None, array=False),
	))