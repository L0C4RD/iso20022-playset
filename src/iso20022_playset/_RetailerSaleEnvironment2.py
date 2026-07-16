# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import LoyaltyHandling1Code
from . import SaleCapabilities1Code
from . import TrueFalseIndicator

class RetailerSaleEnvironment2(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_DbtPrefrdFlg", "_LltyHdlg", "_MaxCshBckAmt", "_MinAmtToDlvr", "_MinSpltAmt", "_SaleCpblties"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def DbtPrefrdFlg(self):
		return self._DbtPrefrdFlg

	@DbtPrefrdFlg.setter
	def DbtPrefrdFlg(self, value):
		self._DbtPrefrdFlg = value if value is not None else base_types.UninitialisedField(self, 'DbtPrefrdFlg', TrueFalseIndicator, False)

	@DbtPrefrdFlg.deleter
	def DbtPrefrdFlg(self):
		del self._DbtPrefrdFlg
		self._DbtPrefrdFlg = base_types.UninitialisedField(self, 'DbtPrefrdFlg', TrueFalseIndicator, False)

	@property
	def LltyHdlg(self):
		return self._LltyHdlg

	@LltyHdlg.setter
	def LltyHdlg(self, value):
		self._LltyHdlg = value if value is not None else base_types.UninitialisedField(self, 'LltyHdlg', LoyaltyHandling1Code, False)

	@LltyHdlg.deleter
	def LltyHdlg(self):
		del self._LltyHdlg
		self._LltyHdlg = base_types.UninitialisedField(self, 'LltyHdlg', LoyaltyHandling1Code, False)

	@property
	def MaxCshBckAmt(self):
		return self._MaxCshBckAmt

	@MaxCshBckAmt.setter
	def MaxCshBckAmt(self, value):
		self._MaxCshBckAmt = value if value is not None else base_types.UninitialisedField(self, 'MaxCshBckAmt', ImpliedCurrencyAndAmount, False)

	@MaxCshBckAmt.deleter
	def MaxCshBckAmt(self):
		del self._MaxCshBckAmt
		self._MaxCshBckAmt = base_types.UninitialisedField(self, 'MaxCshBckAmt', ImpliedCurrencyAndAmount, False)

	@property
	def MinAmtToDlvr(self):
		return self._MinAmtToDlvr

	@MinAmtToDlvr.setter
	def MinAmtToDlvr(self, value):
		self._MinAmtToDlvr = value if value is not None else base_types.UninitialisedField(self, 'MinAmtToDlvr', ImpliedCurrencyAndAmount, False)

	@MinAmtToDlvr.deleter
	def MinAmtToDlvr(self):
		del self._MinAmtToDlvr
		self._MinAmtToDlvr = base_types.UninitialisedField(self, 'MinAmtToDlvr', ImpliedCurrencyAndAmount, False)

	@property
	def MinSpltAmt(self):
		return self._MinSpltAmt

	@MinSpltAmt.setter
	def MinSpltAmt(self, value):
		self._MinSpltAmt = value if value is not None else base_types.UninitialisedField(self, 'MinSpltAmt', ImpliedCurrencyAndAmount, False)

	@MinSpltAmt.deleter
	def MinSpltAmt(self):
		del self._MinSpltAmt
		self._MinSpltAmt = base_types.UninitialisedField(self, 'MinSpltAmt', ImpliedCurrencyAndAmount, False)

	@property
	def SaleCpblties(self):
		return self._SaleCpblties

	@SaleCpblties.setter
	def SaleCpblties(self, value):
		self._SaleCpblties = value if value is not None else base_types.UninitialisedField(self, 'SaleCpblties', SaleCapabilities1Code, True)

	@SaleCpblties.deleter
	def SaleCpblties(self):
		del self._SaleCpblties
		self._SaleCpblties = base_types.UninitialisedField(self, 'SaleCpblties', SaleCapabilities1Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtPrefrdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyHdlg', type=LoyaltyHandling1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxCshBckAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinAmtToDlvr', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSpltAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleCpblties', type=SaleCapabilities1Code, min=0, max=None, mutex_group=None, array=True),
	))