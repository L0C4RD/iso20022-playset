from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .TransactionIdentifier1 import TransactionIdentifier1
from .Max35Text import Max35Text
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .CardPaymentServiceType13Code import CardPaymentServiceType13Code
from .Max70Text import Max70Text

class CardAcquisitionRequest3(base_types._BaseFieldType):

	__slots__ = ["_ForceCstmrSelctnFlg", "_SaleToIssrData", "_SaleTxId", "_AllwdPmtBrnd", "_SaleToAcqrrData", "_TtlAmt", "_SaleToPOIData", "_CshBckFlg", "_PmtTp", "_AllwdLltyBrnd"]
	@property
	def ForceCstmrSelctnFlg(self):
		return self._ForceCstmrSelctnFlg

	@ForceCstmrSelctnFlg.setter
	def ForceCstmrSelctnFlg(self, value):
		self._ForceCstmrSelctnFlg = value if type(value) != base_types.auto else self.make_default("ForceCstmrSelctnFlg")

	@ForceCstmrSelctnFlg.deleter
	def ForceCstmrSelctnFlg(self):
		del self._ForceCstmrSelctnFlg
		self._ForceCstmrSelctnFlg = None

	@property
	def SaleToIssrData(self):
		return self._SaleToIssrData

	@SaleToIssrData.setter
	def SaleToIssrData(self, value):
		self._SaleToIssrData = value if type(value) != base_types.auto else self.make_default("SaleToIssrData")

	@SaleToIssrData.deleter
	def SaleToIssrData(self):
		del self._SaleToIssrData
		self._SaleToIssrData = None

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if type(value) != base_types.auto else self.make_default("SaleTxId")

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = None

	@property
	def AllwdPmtBrnd(self):
		return self._AllwdPmtBrnd

	@AllwdPmtBrnd.setter
	def AllwdPmtBrnd(self, value):
		self._AllwdPmtBrnd = value if type(value) != base_types.auto else self.make_default("AllwdPmtBrnd")

	@AllwdPmtBrnd.deleter
	def AllwdPmtBrnd(self):
		del self._AllwdPmtBrnd
		self._AllwdPmtBrnd = None

	@property
	def SaleToAcqrrData(self):
		return self._SaleToAcqrrData

	@SaleToAcqrrData.setter
	def SaleToAcqrrData(self, value):
		self._SaleToAcqrrData = value if type(value) != base_types.auto else self.make_default("SaleToAcqrrData")

	@SaleToAcqrrData.deleter
	def SaleToAcqrrData(self):
		del self._SaleToAcqrrData
		self._SaleToAcqrrData = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def SaleToPOIData(self):
		return self._SaleToPOIData

	@SaleToPOIData.setter
	def SaleToPOIData(self, value):
		self._SaleToPOIData = value if type(value) != base_types.auto else self.make_default("SaleToPOIData")

	@SaleToPOIData.deleter
	def SaleToPOIData(self):
		del self._SaleToPOIData
		self._SaleToPOIData = None

	@property
	def CshBckFlg(self):
		return self._CshBckFlg

	@CshBckFlg.setter
	def CshBckFlg(self, value):
		self._CshBckFlg = value if type(value) != base_types.auto else self.make_default("CshBckFlg")

	@CshBckFlg.deleter
	def CshBckFlg(self):
		del self._CshBckFlg
		self._CshBckFlg = None

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if type(value) != base_types.auto else self.make_default("PmtTp")

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = None

	@property
	def AllwdLltyBrnd(self):
		return self._AllwdLltyBrnd

	@AllwdLltyBrnd.setter
	def AllwdLltyBrnd(self, value):
		self._AllwdLltyBrnd = value if type(value) != base_types.auto else self.make_default("AllwdLltyBrnd")

	@AllwdLltyBrnd.deleter
	def AllwdLltyBrnd(self):
		del self._AllwdLltyBrnd
		self._AllwdLltyBrnd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ForceCstmrSelctnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleToIssrData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllwdPmtBrnd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleToAcqrrData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleToPOIData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshBckFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTp', type=CardPaymentServiceType13Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllwdLltyBrnd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))

