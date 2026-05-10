import base_types
import CountryCode
import AmountAndDirection53
import RegulatoryTradingCapacity1Code
import ISODateTime
import Max35Text
import DigitalTokenAmount2
import ImpliedCurrencyAndAmount
import SecuritiesTransactionPrice22Choice
import VariationType1Code
import Max52Text
import FinancialInstrumentQuantity25Choice
import MICIdentifier

class SecuritiesTransaction3(base_types._BaseFieldType):

	__slots__ = ["_TradVn", "_CtryOfBrnch", "_TradPlcMtchgId", "_Qty", "_DerivNtnlChng", "_DgtlTknQty", "_TradDt", "_CmplxTradCmpntId", "_UpFrntPmt", "_TradgCpcty", "_Pric", "_NetAmt"]
	@property
	def TradVn(self):
		return self._TradVn

	@TradVn.setter
	def TradVn(self, value):
		self._TradVn = value if type(value) != auto else self.make_default("TradVn")

	@TradVn.deleter
	def TradVn(self):
		del self._TradVn
		self._TradVn = None

	@property
	def CtryOfBrnch(self):
		return self._CtryOfBrnch

	@CtryOfBrnch.setter
	def CtryOfBrnch(self, value):
		self._CtryOfBrnch = value if type(value) != auto else self.make_default("CtryOfBrnch")

	@CtryOfBrnch.deleter
	def CtryOfBrnch(self):
		del self._CtryOfBrnch
		self._CtryOfBrnch = None

	@property
	def TradPlcMtchgId(self):
		return self._TradPlcMtchgId

	@TradPlcMtchgId.setter
	def TradPlcMtchgId(self, value):
		self._TradPlcMtchgId = value if type(value) != auto else self.make_default("TradPlcMtchgId")

	@TradPlcMtchgId.deleter
	def TradPlcMtchgId(self):
		del self._TradPlcMtchgId
		self._TradPlcMtchgId = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def DerivNtnlChng(self):
		return self._DerivNtnlChng

	@DerivNtnlChng.setter
	def DerivNtnlChng(self, value):
		self._DerivNtnlChng = value if type(value) != auto else self.make_default("DerivNtnlChng")

	@DerivNtnlChng.deleter
	def DerivNtnlChng(self):
		del self._DerivNtnlChng
		self._DerivNtnlChng = None

	@property
	def DgtlTknQty(self):
		return self._DgtlTknQty

	@DgtlTknQty.setter
	def DgtlTknQty(self, value):
		self._DgtlTknQty = value if type(value) != auto else self.make_default("DgtlTknQty")

	@DgtlTknQty.deleter
	def DgtlTknQty(self):
		del self._DgtlTknQty
		self._DgtlTknQty = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def CmplxTradCmpntId(self):
		return self._CmplxTradCmpntId

	@CmplxTradCmpntId.setter
	def CmplxTradCmpntId(self, value):
		self._CmplxTradCmpntId = value if type(value) != auto else self.make_default("CmplxTradCmpntId")

	@CmplxTradCmpntId.deleter
	def CmplxTradCmpntId(self):
		del self._CmplxTradCmpntId
		self._CmplxTradCmpntId = None

	@property
	def UpFrntPmt(self):
		return self._UpFrntPmt

	@UpFrntPmt.setter
	def UpFrntPmt(self, value):
		self._UpFrntPmt = value if type(value) != auto else self.make_default("UpFrntPmt")

	@UpFrntPmt.deleter
	def UpFrntPmt(self):
		del self._UpFrntPmt
		self._UpFrntPmt = None

	@property
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if type(value) != auto else self.make_default("TradgCpcty")

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradVn', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBrnch', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPlcMtchgId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity25Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivNtnlChng', type=VariationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlTknQty', type=DigitalTokenAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmplxTradCmpntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpFrntPmt', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCpcty', type=RegulatoryTradingCapacity1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice22Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

