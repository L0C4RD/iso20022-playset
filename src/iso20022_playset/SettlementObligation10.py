import base_types
import AmountAndDirection27
import Price14
import ISODate
import ReceiveDelivery1Code
import FinancialInstrumentQuantity1Choice
import ObligationType1Choice
import Max35Text
import Reference24
import DeliveryReceiptType2Code
import CurrencyCode

class SettlementObligation10(base_types._BaseFieldType):

	__slots__ = ["_SctiesMvmntTp", "_OblgtnTp", "_SttlmDt", "_Qty", "_SttlmAmt", "_NetPosPric", "_Refs", "_TradgCcy", "_Desc", "_Pmt", "_RltdSttlmOblgtnId", "_TradDt"]
	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

	@property
	def OblgtnTp(self):
		return self._OblgtnTp

	@OblgtnTp.setter
	def OblgtnTp(self, value):
		self._OblgtnTp = value if type(value) != auto else self.make_default("OblgtnTp")

	@OblgtnTp.deleter
	def OblgtnTp(self):
		del self._OblgtnTp
		self._OblgtnTp = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

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
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def NetPosPric(self):
		return self._NetPosPric

	@NetPosPric.setter
	def NetPosPric(self, value):
		self._NetPosPric = value if type(value) != auto else self.make_default("NetPosPric")

	@NetPosPric.deleter
	def NetPosPric(self):
		del self._NetPosPric
		self._NetPosPric = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	@property
	def TradgCcy(self):
		return self._TradgCcy

	@TradgCcy.setter
	def TradgCcy(self, value):
		self._TradgCcy = value if type(value) != auto else self.make_default("TradgCcy")

	@TradgCcy.deleter
	def TradgCcy(self):
		del self._TradgCcy
		self._TradgCcy = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def RltdSttlmOblgtnId(self):
		return self._RltdSttlmOblgtnId

	@RltdSttlmOblgtnId.setter
	def RltdSttlmOblgtnId(self, value):
		self._RltdSttlmOblgtnId = value if type(value) != auto else self.make_default("RltdSttlmOblgtnId")

	@RltdSttlmOblgtnId.deleter
	def RltdSttlmOblgtnId(self):
		del self._RltdSttlmOblgtnId
		self._RltdSttlmOblgtnId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnTp', type=ObligationType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection27, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetPosPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=Reference24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCcy', type=CurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmOblgtnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

