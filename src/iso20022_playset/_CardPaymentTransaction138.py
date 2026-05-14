# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardDataReading8Code import CardDataReading8Code
from ._CardPaymentServiceType12Code import CardPaymentServiceType12Code
from ._CardPaymentServiceType15Code import CardPaymentServiceType15Code
from ._CardPaymentServiceType9Code import CardPaymentServiceType9Code
from ._CardPaymentTransactionResult4 import CardPaymentTransactionResult4
from ._GenericIdentification32 import GenericIdentification32
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._TransactionIdentifier1 import TransactionIdentifier1

class CardPaymentTransaction138(base_types._BaseFieldType):

	__slots__ = ["_AddtlSvc", "_CardDataNtryMd", "_InitrTxId", "_POIId", "_RcptTxId", "_SaleRefId", "_SvcAttr", "_TxId", "_TxRslt", "_TxTp"]
	@property
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if type(value) != base_types.auto else self.make_default("AddtlSvc")

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = None

	@property
	def CardDataNtryMd(self):
		return self._CardDataNtryMd

	@CardDataNtryMd.setter
	def CardDataNtryMd(self, value):
		self._CardDataNtryMd = value if type(value) != base_types.auto else self.make_default("CardDataNtryMd")

	@CardDataNtryMd.deleter
	def CardDataNtryMd(self):
		del self._CardDataNtryMd
		self._CardDataNtryMd = None

	@property
	def InitrTxId(self):
		return self._InitrTxId

	@InitrTxId.setter
	def InitrTxId(self, value):
		self._InitrTxId = value if type(value) != base_types.auto else self.make_default("InitrTxId")

	@InitrTxId.deleter
	def InitrTxId(self):
		del self._InitrTxId
		self._InitrTxId = None

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if type(value) != base_types.auto else self.make_default("POIId")

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = None

	@property
	def RcptTxId(self):
		return self._RcptTxId

	@RcptTxId.setter
	def RcptTxId(self, value):
		self._RcptTxId = value if type(value) != base_types.auto else self.make_default("RcptTxId")

	@RcptTxId.deleter
	def RcptTxId(self):
		del self._RcptTxId
		self._RcptTxId = None

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if type(value) != base_types.auto else self.make_default("SaleRefId")

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = None

	@property
	def SvcAttr(self):
		return self._SvcAttr

	@SvcAttr.setter
	def SvcAttr(self, value):
		self._SvcAttr = value if type(value) != base_types.auto else self.make_default("SvcAttr")

	@SvcAttr.deleter
	def SvcAttr(self):
		del self._SvcAttr
		self._SvcAttr = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def TxRslt(self):
		return self._TxRslt

	@TxRslt.setter
	def TxRslt(self, value):
		self._TxRslt = value if type(value) != base_types.auto else self.make_default("TxRslt")

	@TxRslt.deleter
	def TxRslt(self):
		del self._TxRslt
		self._TxRslt = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != base_types.auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSvc', type=CardPaymentServiceType9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardDataNtryMd', type=CardDataReading8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptTxId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcAttr', type=CardPaymentServiceType15Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRslt', type=CardPaymentTransactionResult4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=CardPaymentServiceType12Code, min=1, max=1, mutex_group=None, array=False),
	))