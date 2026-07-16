# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentServiceType13Code
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Max70Text
from . import TransactionIdentifier1
from . import TrueFalseIndicator

class CardAcquisitionRequest3(base_types._BaseFieldType):

	__slots__ = ["_AllwdLltyBrnd", "_AllwdPmtBrnd", "_CshBckFlg", "_ForceCstmrSelctnFlg", "_PmtTp", "_SaleToAcqrrData", "_SaleToIssrData", "_SaleToPOIData", "_SaleTxId", "_TtlAmt"]
	@property
	def AllwdLltyBrnd(self):
		return self._AllwdLltyBrnd

	@AllwdLltyBrnd.setter
	def AllwdLltyBrnd(self, value):
		self._AllwdLltyBrnd = value if value is not None else base_types.UninitialisedField(self, 'AllwdLltyBrnd', Max35Text, True)

	@AllwdLltyBrnd.deleter
	def AllwdLltyBrnd(self):
		del self._AllwdLltyBrnd
		self._AllwdLltyBrnd = base_types.UninitialisedField(self, 'AllwdLltyBrnd', Max35Text, True)

	@property
	def AllwdPmtBrnd(self):
		return self._AllwdPmtBrnd

	@AllwdPmtBrnd.setter
	def AllwdPmtBrnd(self, value):
		self._AllwdPmtBrnd = value if value is not None else base_types.UninitialisedField(self, 'AllwdPmtBrnd', Max35Text, True)

	@AllwdPmtBrnd.deleter
	def AllwdPmtBrnd(self):
		del self._AllwdPmtBrnd
		self._AllwdPmtBrnd = base_types.UninitialisedField(self, 'AllwdPmtBrnd', Max35Text, True)

	@property
	def CshBckFlg(self):
		return self._CshBckFlg

	@CshBckFlg.setter
	def CshBckFlg(self, value):
		self._CshBckFlg = value if value is not None else base_types.UninitialisedField(self, 'CshBckFlg', TrueFalseIndicator, False)

	@CshBckFlg.deleter
	def CshBckFlg(self):
		del self._CshBckFlg
		self._CshBckFlg = base_types.UninitialisedField(self, 'CshBckFlg', TrueFalseIndicator, False)

	@property
	def ForceCstmrSelctnFlg(self):
		return self._ForceCstmrSelctnFlg

	@ForceCstmrSelctnFlg.setter
	def ForceCstmrSelctnFlg(self, value):
		self._ForceCstmrSelctnFlg = value if value is not None else base_types.UninitialisedField(self, 'ForceCstmrSelctnFlg', TrueFalseIndicator, False)

	@ForceCstmrSelctnFlg.deleter
	def ForceCstmrSelctnFlg(self):
		del self._ForceCstmrSelctnFlg
		self._ForceCstmrSelctnFlg = base_types.UninitialisedField(self, 'ForceCstmrSelctnFlg', TrueFalseIndicator, False)

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if value is not None else base_types.UninitialisedField(self, 'PmtTp', CardPaymentServiceType13Code, False)

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = base_types.UninitialisedField(self, 'PmtTp', CardPaymentServiceType13Code, False)

	@property
	def SaleToAcqrrData(self):
		return self._SaleToAcqrrData

	@SaleToAcqrrData.setter
	def SaleToAcqrrData(self, value):
		self._SaleToAcqrrData = value if value is not None else base_types.UninitialisedField(self, 'SaleToAcqrrData', Max70Text, False)

	@SaleToAcqrrData.deleter
	def SaleToAcqrrData(self):
		del self._SaleToAcqrrData
		self._SaleToAcqrrData = base_types.UninitialisedField(self, 'SaleToAcqrrData', Max70Text, False)

	@property
	def SaleToIssrData(self):
		return self._SaleToIssrData

	@SaleToIssrData.setter
	def SaleToIssrData(self, value):
		self._SaleToIssrData = value if value is not None else base_types.UninitialisedField(self, 'SaleToIssrData', Max70Text, False)

	@SaleToIssrData.deleter
	def SaleToIssrData(self):
		del self._SaleToIssrData
		self._SaleToIssrData = base_types.UninitialisedField(self, 'SaleToIssrData', Max70Text, False)

	@property
	def SaleToPOIData(self):
		return self._SaleToPOIData

	@SaleToPOIData.setter
	def SaleToPOIData(self, value):
		self._SaleToPOIData = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIData', Max70Text, False)

	@SaleToPOIData.deleter
	def SaleToPOIData(self):
		del self._SaleToPOIData
		self._SaleToPOIData = base_types.UninitialisedField(self, 'SaleToPOIData', Max70Text, False)

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if value is not None else base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllwdLltyBrnd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllwdPmtBrnd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshBckFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ForceCstmrSelctnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTp', type=CardPaymentServiceType13Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleToAcqrrData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleToIssrData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleToPOIData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))