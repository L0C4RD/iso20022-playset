# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankTransactionCodeStructure4
from . import BillingServiceCommonIdentification1
from . import BillingSubServiceIdentification1
from . import Max12Text
from . import Max35Text
from . import Max70Text

class BillingServiceIdentification3(base_types._BaseFieldType):

	__slots__ = ["_BkTxCd", "_CmonCd", "_Desc", "_Id", "_SubSvc", "_SvcTp"]
	@property
	def BkTxCd(self):
		return self._BkTxCd

	@BkTxCd.setter
	def BkTxCd(self, value):
		self._BkTxCd = value if value is not None else base_types.UninitialisedField(self, 'BkTxCd', BankTransactionCodeStructure4, False)

	@BkTxCd.deleter
	def BkTxCd(self):
		del self._BkTxCd
		self._BkTxCd = base_types.UninitialisedField(self, 'BkTxCd', BankTransactionCodeStructure4, False)

	@property
	def CmonCd(self):
		return self._CmonCd

	@CmonCd.setter
	def CmonCd(self, value):
		self._CmonCd = value if value is not None else base_types.UninitialisedField(self, 'CmonCd', BillingServiceCommonIdentification1, False)

	@CmonCd.deleter
	def CmonCd(self):
		del self._CmonCd
		self._CmonCd = base_types.UninitialisedField(self, 'CmonCd', BillingServiceCommonIdentification1, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max70Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max70Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def SubSvc(self):
		return self._SubSvc

	@SubSvc.setter
	def SubSvc(self, value):
		self._SubSvc = value if value is not None else base_types.UninitialisedField(self, 'SubSvc', BillingSubServiceIdentification1, False)

	@SubSvc.deleter
	def SubSvc(self):
		del self._SubSvc
		self._SubSvc = base_types.UninitialisedField(self, 'SubSvc', BillingSubServiceIdentification1, False)

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if value is not None else base_types.UninitialisedField(self, 'SvcTp', Max12Text, False)

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = base_types.UninitialisedField(self, 'SvcTp', Max12Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkTxCd', type=BankTransactionCodeStructure4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonCd', type=BillingServiceCommonIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubSvc', type=BillingSubServiceIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=Max12Text, min=0, max=1, mutex_group=None, array=False),
	))