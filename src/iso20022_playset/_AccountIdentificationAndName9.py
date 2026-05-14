# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._GenericAccountIdentification1 import GenericAccountIdentification1
from ._IBAN2007Identifier import IBAN2007Identifier
from ._Max35Text import Max35Text

class AccountIdentificationAndName9(base_types._BaseFieldType):

	__slots__ = ["_BlckChainCshWllt", "_IBAN", "_Nm", "_Othr"]
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
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainCshWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericAccountIdentification1, min=0, max=1, mutex_group=None, array=False),
	))