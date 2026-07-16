# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection53
from . import CountryCode
from . import DigitalTokenAmount2
from . import FinancialInstrumentQuantity25Choice
from . import ISODateTime
from . import ImpliedCurrencyAndAmount
from . import MICIdentifier
from . import Max35Text
from . import Max52Text
from . import RegulatoryTradingCapacity1Code
from . import SecuritiesTransactionPrice22Choice
from . import VariationType1Code

class SecuritiesTransaction3(base_types._BaseFieldType):

	__slots__ = ["_CmplxTradCmpntId", "_CtryOfBrnch", "_DerivNtnlChng", "_DgtlTknQty", "_NetAmt", "_Pric", "_Qty", "_TradDt", "_TradPlcMtchgId", "_TradVn", "_TradgCpcty", "_UpFrntPmt"]
	@property
	def CmplxTradCmpntId(self):
		return self._CmplxTradCmpntId

	@CmplxTradCmpntId.setter
	def CmplxTradCmpntId(self, value):
		self._CmplxTradCmpntId = value if value is not None else base_types.UninitialisedField(self, 'CmplxTradCmpntId', Max35Text, False)

	@CmplxTradCmpntId.deleter
	def CmplxTradCmpntId(self):
		del self._CmplxTradCmpntId
		self._CmplxTradCmpntId = base_types.UninitialisedField(self, 'CmplxTradCmpntId', Max35Text, False)

	@property
	def CtryOfBrnch(self):
		return self._CtryOfBrnch

	@CtryOfBrnch.setter
	def CtryOfBrnch(self, value):
		self._CtryOfBrnch = value if value is not None else base_types.UninitialisedField(self, 'CtryOfBrnch', CountryCode, False)

	@CtryOfBrnch.deleter
	def CtryOfBrnch(self):
		del self._CtryOfBrnch
		self._CtryOfBrnch = base_types.UninitialisedField(self, 'CtryOfBrnch', CountryCode, False)

	@property
	def DerivNtnlChng(self):
		return self._DerivNtnlChng

	@DerivNtnlChng.setter
	def DerivNtnlChng(self, value):
		self._DerivNtnlChng = value if value is not None else base_types.UninitialisedField(self, 'DerivNtnlChng', VariationType1Code, False)

	@DerivNtnlChng.deleter
	def DerivNtnlChng(self):
		del self._DerivNtnlChng
		self._DerivNtnlChng = base_types.UninitialisedField(self, 'DerivNtnlChng', VariationType1Code, False)

	@property
	def DgtlTknQty(self):
		return self._DgtlTknQty

	@DgtlTknQty.setter
	def DgtlTknQty(self, value):
		self._DgtlTknQty = value if value is not None else base_types.UninitialisedField(self, 'DgtlTknQty', DigitalTokenAmount2, True)

	@DgtlTknQty.deleter
	def DgtlTknQty(self):
		del self._DgtlTknQty
		self._DgtlTknQty = base_types.UninitialisedField(self, 'DgtlTknQty', DigitalTokenAmount2, True)

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if value is not None else base_types.UninitialisedField(self, 'NetAmt', ImpliedCurrencyAndAmount, False)

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = base_types.UninitialisedField(self, 'NetAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice22Choice, False)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice22Choice, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity25Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity25Choice, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODateTime, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODateTime, False)

	@property
	def TradPlcMtchgId(self):
		return self._TradPlcMtchgId

	@TradPlcMtchgId.setter
	def TradPlcMtchgId(self, value):
		self._TradPlcMtchgId = value if value is not None else base_types.UninitialisedField(self, 'TradPlcMtchgId', Max52Text, False)

	@TradPlcMtchgId.deleter
	def TradPlcMtchgId(self):
		del self._TradPlcMtchgId
		self._TradPlcMtchgId = base_types.UninitialisedField(self, 'TradPlcMtchgId', Max52Text, False)

	@property
	def TradVn(self):
		return self._TradVn

	@TradVn.setter
	def TradVn(self, value):
		self._TradVn = value if value is not None else base_types.UninitialisedField(self, 'TradVn', MICIdentifier, False)

	@TradVn.deleter
	def TradVn(self):
		del self._TradVn
		self._TradVn = base_types.UninitialisedField(self, 'TradVn', MICIdentifier, False)

	@property
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if value is not None else base_types.UninitialisedField(self, 'TradgCpcty', RegulatoryTradingCapacity1Code, False)

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = base_types.UninitialisedField(self, 'TradgCpcty', RegulatoryTradingCapacity1Code, False)

	@property
	def UpFrntPmt(self):
		return self._UpFrntPmt

	@UpFrntPmt.setter
	def UpFrntPmt(self, value):
		self._UpFrntPmt = value if value is not None else base_types.UninitialisedField(self, 'UpFrntPmt', AmountAndDirection53, False)

	@UpFrntPmt.deleter
	def UpFrntPmt(self):
		del self._UpFrntPmt
		self._UpFrntPmt = base_types.UninitialisedField(self, 'UpFrntPmt', AmountAndDirection53, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmplxTradCmpntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBrnch', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivNtnlChng', type=VariationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlTknQty', type=DigitalTokenAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice22Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity25Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPlcMtchgId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradVn', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCpcty', type=RegulatoryTradingCapacity1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpFrntPmt', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
	))