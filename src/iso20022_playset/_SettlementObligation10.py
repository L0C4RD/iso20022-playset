# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection27
from . import CurrencyCode
from . import DeliveryReceiptType2Code
from . import FinancialInstrumentQuantity1Choice
from . import ISODate
from . import Max35Text
from . import ObligationType1Choice
from . import Price14
from . import ReceiveDelivery1Code
from . import Reference24

class SettlementObligation10(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_NetPosPric", "_OblgtnTp", "_Pmt", "_Qty", "_Refs", "_RltdSttlmOblgtnId", "_SctiesMvmntTp", "_SttlmAmt", "_SttlmDt", "_TradDt", "_TradgCcy"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max35Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max35Text, False)

	@property
	def NetPosPric(self):
		return self._NetPosPric

	@NetPosPric.setter
	def NetPosPric(self, value):
		self._NetPosPric = value if value is not None else base_types.UninitialisedField(self, 'NetPosPric', Price14, False)

	@NetPosPric.deleter
	def NetPosPric(self):
		del self._NetPosPric
		self._NetPosPric = base_types.UninitialisedField(self, 'NetPosPric', Price14, False)

	@property
	def OblgtnTp(self):
		return self._OblgtnTp

	@OblgtnTp.setter
	def OblgtnTp(self, value):
		self._OblgtnTp = value if value is not None else base_types.UninitialisedField(self, 'OblgtnTp', ObligationType1Choice, False)

	@OblgtnTp.deleter
	def OblgtnTp(self):
		del self._OblgtnTp
		self._OblgtnTp = base_types.UninitialisedField(self, 'OblgtnTp', ObligationType1Choice, False)

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if value is not None else base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity1Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity1Choice, False)

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', Reference24, False)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', Reference24, False)

	@property
	def RltdSttlmOblgtnId(self):
		return self._RltdSttlmOblgtnId

	@RltdSttlmOblgtnId.setter
	def RltdSttlmOblgtnId(self, value):
		self._RltdSttlmOblgtnId = value if value is not None else base_types.UninitialisedField(self, 'RltdSttlmOblgtnId', Max35Text, False)

	@RltdSttlmOblgtnId.deleter
	def RltdSttlmOblgtnId(self):
		del self._RltdSttlmOblgtnId
		self._RltdSttlmOblgtnId = base_types.UninitialisedField(self, 'RltdSttlmOblgtnId', Max35Text, False)

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection27, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection27, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@property
	def TradgCcy(self):
		return self._TradgCcy

	@TradgCcy.setter
	def TradgCcy(self, value):
		self._TradgCcy = value if value is not None else base_types.UninitialisedField(self, 'TradgCcy', CurrencyCode, False)

	@TradgCcy.deleter
	def TradgCcy(self):
		del self._TradgCcy
		self._TradgCcy = base_types.UninitialisedField(self, 'TradgCcy', CurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetPosPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnTp', type=ObligationType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=Reference24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmOblgtnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection27, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCcy', type=CurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))