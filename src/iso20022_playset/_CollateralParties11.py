# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet3
from . import PartyIdentification136
from . import PartyIdentification232
from . import SecuritiesAccount19

class CollateralParties11(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_ClntPtyB", "_CollAcct", "_PtyB", "_TrptyAgt"]
	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@property
	def ClntPtyB(self):
		return self._ClntPtyB

	@ClntPtyB.setter
	def ClntPtyB(self, value):
		self._ClntPtyB = value if value is not None else base_types.UninitialisedField(self, 'ClntPtyB', PartyIdentification232, False)

	@ClntPtyB.deleter
	def ClntPtyB(self):
		del self._ClntPtyB
		self._ClntPtyB = base_types.UninitialisedField(self, 'ClntPtyB', PartyIdentification232, False)

	@property
	def CollAcct(self):
		return self._CollAcct

	@CollAcct.setter
	def CollAcct(self, value):
		self._CollAcct = value if value is not None else base_types.UninitialisedField(self, 'CollAcct', SecuritiesAccount19, False)

	@CollAcct.deleter
	def CollAcct(self):
		del self._CollAcct
		self._CollAcct = base_types.UninitialisedField(self, 'CollAcct', SecuritiesAccount19, False)

	@property
	def PtyB(self):
		return self._PtyB

	@PtyB.setter
	def PtyB(self, value):
		self._PtyB = value if value is not None else base_types.UninitialisedField(self, 'PtyB', PartyIdentification232, False)

	@PtyB.deleter
	def PtyB(self):
		del self._PtyB
		self._PtyB = base_types.UninitialisedField(self, 'PtyB', PartyIdentification232, False)

	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgt', PartyIdentification136, False)

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = base_types.UninitialisedField(self, 'TrptyAgt', PartyIdentification136, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntPtyB', type=PartyIdentification232, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyB', type=PartyIdentification232, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgt', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))