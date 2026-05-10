from . import base_types
from ._SecuritiesAccount34 import SecuritiesAccount34
from ._PartyIdentification156 import PartyIdentification156
from ._AggregateBalanceInformation43 import AggregateBalanceInformation43
from ._YesNoIndicator import YesNoIndicator
from ._BlockChainAddressWallet9 import BlockChainAddressWallet9

class SubAccountIdentification68(base_types._BaseFieldType):

	__slots__ = ["_BalForSubAcct", "_SfkpgAcct", "_ActvtyInd", "_AcctOwnr", "_BlckChainAdrOrWllt"]
	@property
	def BalForSubAcct(self):
		return self._BalForSubAcct

	@BalForSubAcct.setter
	def BalForSubAcct(self, value):
		self._BalForSubAcct = value if type(value) != base_types.auto else self.make_default("BalForSubAcct")

	@BalForSubAcct.deleter
	def BalForSubAcct(self):
		del self._BalForSubAcct
		self._BalForSubAcct = None

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
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != base_types.auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalForSubAcct', type=AggregateBalanceInformation43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification156, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet9, min=0, max=1, mutex_group=None, array=False),
	))

