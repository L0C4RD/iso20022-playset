from . import base_types
from ._AmountAndDirection44 import AmountAndDirection44
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._Max35Text import Max35Text
from ._Quantity51Choice import Quantity51Choice
from ._ReceiveDelivery1Code import ReceiveDelivery1Code
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SecuritiesMovementStatus1Choice import SecuritiesMovementStatus1Choice
from ._SecurityIdentification19 import SecurityIdentification19
from ._YesNoIndicator import YesNoIndicator

class SecuritiesMovement8(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_ClntSctiesMvmntId", "_CollMvmnt", "_FinInstrmId", "_MrgndVal", "_MvmntSts", "_PosTp", "_SctiesMvmntTp", "_SctiesMvmntsApprvd", "_SctiesQty", "_SfkpgAcct", "_TrptyAgtSvcPrvdrSctiesMvmntId"]
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
	def ClntSctiesMvmntId(self):
		return self._ClntSctiesMvmntId

	@ClntSctiesMvmntId.setter
	def ClntSctiesMvmntId(self, value):
		self._ClntSctiesMvmntId = value if type(value) != base_types.auto else self.make_default("ClntSctiesMvmntId")

	@ClntSctiesMvmntId.deleter
	def ClntSctiesMvmntId(self):
		del self._ClntSctiesMvmntId
		self._ClntSctiesMvmntId = None

	@property
	def CollMvmnt(self):
		return self._CollMvmnt

	@CollMvmnt.setter
	def CollMvmnt(self, value):
		self._CollMvmnt = value if type(value) != base_types.auto else self.make_default("CollMvmnt")

	@CollMvmnt.deleter
	def CollMvmnt(self):
		del self._CollMvmnt
		self._CollMvmnt = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def MrgndVal(self):
		return self._MrgndVal

	@MrgndVal.setter
	def MrgndVal(self, value):
		self._MrgndVal = value if type(value) != base_types.auto else self.make_default("MrgndVal")

	@MrgndVal.deleter
	def MrgndVal(self):
		del self._MrgndVal
		self._MrgndVal = None

	@property
	def MvmntSts(self):
		return self._MvmntSts

	@MvmntSts.setter
	def MvmntSts(self, value):
		self._MvmntSts = value if type(value) != base_types.auto else self.make_default("MvmntSts")

	@MvmntSts.deleter
	def MvmntSts(self):
		del self._MvmntSts
		self._MvmntSts = None

	@property
	def PosTp(self):
		return self._PosTp

	@PosTp.setter
	def PosTp(self, value):
		self._PosTp = value if type(value) != base_types.auto else self.make_default("PosTp")

	@PosTp.deleter
	def PosTp(self):
		del self._PosTp
		self._PosTp = None

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != base_types.auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

	@property
	def SctiesMvmntsApprvd(self):
		return self._SctiesMvmntsApprvd

	@SctiesMvmntsApprvd.setter
	def SctiesMvmntsApprvd(self, value):
		self._SctiesMvmntsApprvd = value if type(value) != base_types.auto else self.make_default("SctiesMvmntsApprvd")

	@SctiesMvmntsApprvd.deleter
	def SctiesMvmntsApprvd(self):
		del self._SctiesMvmntsApprvd
		self._SctiesMvmntsApprvd = None

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if type(value) != base_types.auto else self.make_default("SctiesQty")

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = None

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
	def TrptyAgtSvcPrvdrSctiesMvmntId(self):
		return self._TrptyAgtSvcPrvdrSctiesMvmntId

	@TrptyAgtSvcPrvdrSctiesMvmntId.setter
	def TrptyAgtSvcPrvdrSctiesMvmntId(self, value):
		self._TrptyAgtSvcPrvdrSctiesMvmntId = value if type(value) != base_types.auto else self.make_default("TrptyAgtSvcPrvdrSctiesMvmntId")

	@TrptyAgtSvcPrvdrSctiesMvmntId.deleter
	def TrptyAgtSvcPrvdrSctiesMvmntId(self):
		del self._TrptyAgtSvcPrvdrSctiesMvmntId
		self._TrptyAgtSvcPrvdrSctiesMvmntId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntSctiesMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMvmnt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgndVal', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntSts', type=SecuritiesMovementStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PosTp', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntsApprvd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=Quantity51Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrSctiesMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

