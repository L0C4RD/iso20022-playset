# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceFormat14Choice
from . import PartyIdentification136Choice
from . import RestrictedFINXMax140Text
from . import RestrictedFINXMax35Text
from . import SafekeepingPlaceFormat54Choice

class AccountIdentification76(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BlckChainAdrOrWllt", "_ConfdBal", "_SfkpgAcct", "_SfkpgPlc"]
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
	def ConfdBal(self):
		return self._ConfdBal

	@ConfdBal.setter
	def ConfdBal(self, value):
		self._ConfdBal = value if value is not None else base_types.UninitialisedField(self, 'ConfdBal', BalanceFormat14Choice, False)

	@ConfdBal.deleter
	def ConfdBal(self):
		del self._ConfdBal
		self._ConfdBal = base_types.UninitialisedField(self, 'ConfdBal', BalanceFormat14Choice, False)

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
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat54Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat54Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfdBal', type=BalanceFormat14Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat54Choice, min=0, max=1, mutex_group=None, array=False),
	))