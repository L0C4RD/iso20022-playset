# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet11
from . import IBAN2007Identifier
from . import RestrictedFINX2Max34Text

class CashAccountIdentification11Choice(base_types._BaseFieldType):

	__slots__ = ["_BlckChainCshWllt", "_IBAN", "_Prtry"]
	@property
	def BlckChainCshWllt(self):
		return self._BlckChainCshWllt

	@BlckChainCshWllt.setter
	def BlckChainCshWllt(self, value):
		self._BlckChainCshWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainCshWllt', BlockChainAddressWallet11, False)

	@BlckChainCshWllt.deleter
	def BlckChainCshWllt(self):
		del self._BlckChainCshWllt
		self._BlckChainCshWllt = base_types.UninitialisedField(self, 'BlckChainCshWllt', BlockChainAddressWallet11, False)

	@property
	def IBAN(self):
		return self._IBAN

	@IBAN.setter
	def IBAN(self, value):
		self._IBAN = value if value is not None else base_types.UninitialisedField(self, 'IBAN', IBAN2007Identifier, False)

	@IBAN.deleter
	def IBAN(self):
		del self._IBAN
		self._IBAN = base_types.UninitialisedField(self, 'IBAN', IBAN2007Identifier, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', RestrictedFINX2Max34Text, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', RestrictedFINX2Max34Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainCshWllt', type=BlockChainAddressWallet11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=RestrictedFINX2Max34Text, min=0, max=1, mutex_group=1, array=False),
	))