# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._CollateralEntryType1Code import CollateralEntryType1Code
from ._FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from ._Max35Text import Max35Text
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SecurityIdentification19 import SecurityIdentification19
from ._YesNoIndicator import YesNoIndicator

class SecuritiesMovement9(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_ClntSctiesMvmntId", "_CollMvmnt", "_FinInstrmId", "_Qty", "_SctiesMvmntTp", "_SfkpgAcct", "_TrptyAgtSvcPrvdrSctiesMvmntId"]
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
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

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
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=CollateralEntryType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrSctiesMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))