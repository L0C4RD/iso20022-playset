import base_types
import ImpliedCurrencyAndAmount
import ActiveCurrencyCode
import SaleCapabilities1Code
import TrueFalseIndicator
import LoyaltyHandling1Code

class RetailerSaleEnvironment2(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_LltyHdlg", "_MaxCshBckAmt", "_MinSpltAmt", "_SaleCpblties", "_MinAmtToDlvr", "_DbtPrefrdFlg"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def LltyHdlg(self):
		return self._LltyHdlg

	@LltyHdlg.setter
	def LltyHdlg(self, value):
		self._LltyHdlg = value if type(value) != auto else self.make_default("LltyHdlg")

	@LltyHdlg.deleter
	def LltyHdlg(self):
		del self._LltyHdlg
		self._LltyHdlg = None

	@property
	def MaxCshBckAmt(self):
		return self._MaxCshBckAmt

	@MaxCshBckAmt.setter
	def MaxCshBckAmt(self, value):
		self._MaxCshBckAmt = value if type(value) != auto else self.make_default("MaxCshBckAmt")

	@MaxCshBckAmt.deleter
	def MaxCshBckAmt(self):
		del self._MaxCshBckAmt
		self._MaxCshBckAmt = None

	@property
	def MinSpltAmt(self):
		return self._MinSpltAmt

	@MinSpltAmt.setter
	def MinSpltAmt(self, value):
		self._MinSpltAmt = value if type(value) != auto else self.make_default("MinSpltAmt")

	@MinSpltAmt.deleter
	def MinSpltAmt(self):
		del self._MinSpltAmt
		self._MinSpltAmt = None

	@property
	def SaleCpblties(self):
		return self._SaleCpblties

	@SaleCpblties.setter
	def SaleCpblties(self, value):
		self._SaleCpblties = value if type(value) != auto else self.make_default("SaleCpblties")

	@SaleCpblties.deleter
	def SaleCpblties(self):
		del self._SaleCpblties
		self._SaleCpblties = None

	@property
	def MinAmtToDlvr(self):
		return self._MinAmtToDlvr

	@MinAmtToDlvr.setter
	def MinAmtToDlvr(self, value):
		self._MinAmtToDlvr = value if type(value) != auto else self.make_default("MinAmtToDlvr")

	@MinAmtToDlvr.deleter
	def MinAmtToDlvr(self):
		del self._MinAmtToDlvr
		self._MinAmtToDlvr = None

	@property
	def DbtPrefrdFlg(self):
		return self._DbtPrefrdFlg

	@DbtPrefrdFlg.setter
	def DbtPrefrdFlg(self, value):
		self._DbtPrefrdFlg = value if type(value) != auto else self.make_default("DbtPrefrdFlg")

	@DbtPrefrdFlg.deleter
	def DbtPrefrdFlg(self):
		del self._DbtPrefrdFlg
		self._DbtPrefrdFlg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyHdlg', type=LoyaltyHandling1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxCshBckAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSpltAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleCpblties', type=SaleCapabilities1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MinAmtToDlvr', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtPrefrdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

