from . import base_types
from .RestrictedFINXMax35Text import RestrictedFINXMax35Text
from .BalanceFormat14Choice import BalanceFormat14Choice
from .RestrictedFINXMax140Text import RestrictedFINXMax140Text

class AccountAndBalance54(base_types._BaseFieldType):

	__slots__ = ["_SfkpgAcct", "_BlckChainAdrOrWllt", "_ConfdBal"]
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
	def ConfdBal(self):
		return self._ConfdBal

	@ConfdBal.setter
	def ConfdBal(self, value):
		self._ConfdBal = value if type(value) != base_types.auto else self.make_default("ConfdBal")

	@ConfdBal.deleter
	def ConfdBal(self):
		del self._ConfdBal
		self._ConfdBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SfkpgAcct', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfdBal', type=BalanceFormat14Choice, min=1, max=1, mutex_group=None, array=False),
	))

