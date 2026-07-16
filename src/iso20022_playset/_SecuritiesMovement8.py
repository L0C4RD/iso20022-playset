# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection44
from . import BlockChainAddressWallet3
from . import Max35Text
from . import Quantity51Choice
from . import ReceiveDelivery1Code
from . import SecuritiesAccount19
from . import SecuritiesMovementStatus1Choice
from . import SecurityIdentification19
from . import YesNoIndicator

class SecuritiesMovement8(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_ClntSctiesMvmntId", "_CollMvmnt", "_FinInstrmId", "_MrgndVal", "_MvmntSts", "_PosTp", "_SctiesMvmntTp", "_SctiesMvmntsApprvd", "_SctiesQty", "_SfkpgAcct", "_TrptyAgtSvcPrvdrSctiesMvmntId"]
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
	def ClntSctiesMvmntId(self):
		return self._ClntSctiesMvmntId

	@ClntSctiesMvmntId.setter
	def ClntSctiesMvmntId(self, value):
		self._ClntSctiesMvmntId = value if value is not None else base_types.UninitialisedField(self, 'ClntSctiesMvmntId', Max35Text, False)

	@ClntSctiesMvmntId.deleter
	def ClntSctiesMvmntId(self):
		del self._ClntSctiesMvmntId
		self._ClntSctiesMvmntId = base_types.UninitialisedField(self, 'ClntSctiesMvmntId', Max35Text, False)

	@property
	def CollMvmnt(self):
		return self._CollMvmnt

	@CollMvmnt.setter
	def CollMvmnt(self, value):
		self._CollMvmnt = value if value is not None else base_types.UninitialisedField(self, 'CollMvmnt', YesNoIndicator, False)

	@CollMvmnt.deleter
	def CollMvmnt(self):
		del self._CollMvmnt
		self._CollMvmnt = base_types.UninitialisedField(self, 'CollMvmnt', YesNoIndicator, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def MrgndVal(self):
		return self._MrgndVal

	@MrgndVal.setter
	def MrgndVal(self, value):
		self._MrgndVal = value if value is not None else base_types.UninitialisedField(self, 'MrgndVal', AmountAndDirection44, False)

	@MrgndVal.deleter
	def MrgndVal(self):
		del self._MrgndVal
		self._MrgndVal = base_types.UninitialisedField(self, 'MrgndVal', AmountAndDirection44, False)

	@property
	def MvmntSts(self):
		return self._MvmntSts

	@MvmntSts.setter
	def MvmntSts(self, value):
		self._MvmntSts = value if value is not None else base_types.UninitialisedField(self, 'MvmntSts', SecuritiesMovementStatus1Choice, False)

	@MvmntSts.deleter
	def MvmntSts(self):
		del self._MvmntSts
		self._MvmntSts = base_types.UninitialisedField(self, 'MvmntSts', SecuritiesMovementStatus1Choice, False)

	@property
	def PosTp(self):
		return self._PosTp

	@PosTp.setter
	def PosTp(self, value):
		self._PosTp = value if value is not None else base_types.UninitialisedField(self, 'PosTp', YesNoIndicator, False)

	@PosTp.deleter
	def PosTp(self):
		del self._PosTp
		self._PosTp = base_types.UninitialisedField(self, 'PosTp', YesNoIndicator, False)

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@property
	def SctiesMvmntsApprvd(self):
		return self._SctiesMvmntsApprvd

	@SctiesMvmntsApprvd.setter
	def SctiesMvmntsApprvd(self, value):
		self._SctiesMvmntsApprvd = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntsApprvd', YesNoIndicator, False)

	@SctiesMvmntsApprvd.deleter
	def SctiesMvmntsApprvd(self):
		del self._SctiesMvmntsApprvd
		self._SctiesMvmntsApprvd = base_types.UninitialisedField(self, 'SctiesMvmntsApprvd', YesNoIndicator, False)

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if value is not None else base_types.UninitialisedField(self, 'SctiesQty', Quantity51Choice, False)

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = base_types.UninitialisedField(self, 'SctiesQty', Quantity51Choice, False)

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

	@property
	def TrptyAgtSvcPrvdrSctiesMvmntId(self):
		return self._TrptyAgtSvcPrvdrSctiesMvmntId

	@TrptyAgtSvcPrvdrSctiesMvmntId.setter
	def TrptyAgtSvcPrvdrSctiesMvmntId(self, value):
		self._TrptyAgtSvcPrvdrSctiesMvmntId = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrSctiesMvmntId', Max35Text, False)

	@TrptyAgtSvcPrvdrSctiesMvmntId.deleter
	def TrptyAgtSvcPrvdrSctiesMvmntId(self):
		del self._TrptyAgtSvcPrvdrSctiesMvmntId
		self._TrptyAgtSvcPrvdrSctiesMvmntId = base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrSctiesMvmntId', Max35Text, False)

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