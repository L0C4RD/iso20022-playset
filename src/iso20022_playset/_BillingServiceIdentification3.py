from . import base_types
from ._BillingServiceCommonIdentification1 import BillingServiceCommonIdentification1
from ._Max70Text import Max70Text
from ._Max35Text import Max35Text
from ._BankTransactionCodeStructure4 import BankTransactionCodeStructure4
from ._Max12Text import Max12Text
from ._BillingSubServiceIdentification1 import BillingSubServiceIdentification1

class BillingServiceIdentification3(base_types._BaseFieldType):

	__slots__ = ["_SubSvc", "_CmonCd", "_Desc", "_Id", "_BkTxCd", "_SvcTp"]
	@property
	def SubSvc(self):
		return self._SubSvc

	@SubSvc.setter
	def SubSvc(self, value):
		self._SubSvc = value if type(value) != base_types.auto else self.make_default("SubSvc")

	@SubSvc.deleter
	def SubSvc(self):
		del self._SubSvc
		self._SubSvc = None

	@property
	def CmonCd(self):
		return self._CmonCd

	@CmonCd.setter
	def CmonCd(self, value):
		self._CmonCd = value if type(value) != base_types.auto else self.make_default("CmonCd")

	@CmonCd.deleter
	def CmonCd(self):
		del self._CmonCd
		self._CmonCd = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def BkTxCd(self):
		return self._BkTxCd

	@BkTxCd.setter
	def BkTxCd(self, value):
		self._BkTxCd = value if type(value) != base_types.auto else self.make_default("BkTxCd")

	@BkTxCd.deleter
	def BkTxCd(self):
		del self._BkTxCd
		self._BkTxCd = None

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != base_types.auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubSvc', type=BillingSubServiceIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonCd', type=BillingServiceCommonIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkTxCd', type=BankTransactionCodeStructure4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=Max12Text, min=0, max=1, mutex_group=None, array=False),
	))

