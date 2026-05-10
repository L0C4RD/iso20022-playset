from . import base_types
from .RestrictedFINX2Max34Text import RestrictedFINX2Max34Text
from .BlockChainAddressWallet11 import BlockChainAddressWallet11
from .IBAN2007Identifier import IBAN2007Identifier

class CashAccountIdentification10Choice(base_types._BaseFieldType):

	__slots__ = ["_IBAN", "_Prtry", "_BlckChainCshWllt"]
	@property
	def IBAN(self):
		return self._IBAN

	@IBAN.setter
	def IBAN(self, value):
		self._IBAN = value if type(value) != base_types.auto else self.make_default("IBAN")

	@IBAN.deleter
	def IBAN(self):
		del self._IBAN
		self._IBAN = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def BlckChainCshWllt(self):
		return self._BlckChainCshWllt

	@BlckChainCshWllt.setter
	def BlckChainCshWllt(self, value):
		self._BlckChainCshWllt = value if type(value) != base_types.auto else self.make_default("BlckChainCshWllt")

	@BlckChainCshWllt.deleter
	def BlckChainCshWllt(self):
		del self._BlckChainCshWllt
		self._BlckChainCshWllt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=RestrictedFINX2Max34Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BlckChainCshWllt', type=BlockChainAddressWallet11, min=0, max=1, mutex_group=1, array=False),
	))

