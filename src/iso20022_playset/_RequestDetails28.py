# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet3
from . import CollateralParties4
from . import Reference21
from . import RemovalProcessing2Choice
from . import RemovalTypeAndReason1
from . import SecuritiesAccount19

class RequestDetails28(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_CtrPty", "_FinInstrmAndAttrbts", "_Ref", "_Rmvl", "_SfkpgAcct"]
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
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if value is not None else base_types.UninitialisedField(self, 'CtrPty', CollateralParties4, False)

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = base_types.UninitialisedField(self, 'CtrPty', CollateralParties4, False)

	@property
	def FinInstrmAndAttrbts(self):
		return self._FinInstrmAndAttrbts

	@FinInstrmAndAttrbts.setter
	def FinInstrmAndAttrbts(self, value):
		self._FinInstrmAndAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAndAttrbts', RemovalProcessing2Choice, True)

	@FinInstrmAndAttrbts.deleter
	def FinInstrmAndAttrbts(self):
		del self._FinInstrmAndAttrbts
		self._FinInstrmAndAttrbts = base_types.UninitialisedField(self, 'FinInstrmAndAttrbts', RemovalProcessing2Choice, True)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Reference21, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Reference21, False)

	@property
	def Rmvl(self):
		return self._Rmvl

	@Rmvl.setter
	def Rmvl(self, value):
		self._Rmvl = value if value is not None else base_types.UninitialisedField(self, 'Rmvl', RemovalTypeAndReason1, False)

	@Rmvl.deleter
	def Rmvl(self):
		del self._Rmvl
		self._Rmvl = base_types.UninitialisedField(self, 'Rmvl', RemovalTypeAndReason1, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=CollateralParties4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAndAttrbts', type=RemovalProcessing2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=Reference21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rmvl', type=RemovalTypeAndReason1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
	))