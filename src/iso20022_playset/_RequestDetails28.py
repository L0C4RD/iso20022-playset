from . import base_types
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._CollateralParties4 import CollateralParties4
from ._Reference21 import Reference21
from ._RemovalTypeAndReason1 import RemovalTypeAndReason1
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._RemovalProcessing2Choice import RemovalProcessing2Choice

class RequestDetails28(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_Rmvl", "_SfkpgAcct", "_FinInstrmAndAttrbts", "_Ref", "_CtrPty"]
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
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if type(value) != base_types.auto else self.make_default("CtrPty")

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = None

	@property
	def FinInstrmAndAttrbts(self):
		return self._FinInstrmAndAttrbts

	@FinInstrmAndAttrbts.setter
	def FinInstrmAndAttrbts(self, value):
		self._FinInstrmAndAttrbts = value if type(value) != base_types.auto else self.make_default("FinInstrmAndAttrbts")

	@FinInstrmAndAttrbts.deleter
	def FinInstrmAndAttrbts(self):
		del self._FinInstrmAndAttrbts
		self._FinInstrmAndAttrbts = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def Rmvl(self):
		return self._Rmvl

	@Rmvl.setter
	def Rmvl(self, value):
		self._Rmvl = value if type(value) != base_types.auto else self.make_default("Rmvl")

	@Rmvl.deleter
	def Rmvl(self):
		del self._Rmvl
		self._Rmvl = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=CollateralParties4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAndAttrbts', type=RemovalProcessing2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=Reference21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rmvl', type=RemovalTypeAndReason1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
	))

