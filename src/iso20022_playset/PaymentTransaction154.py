import base_types
import PaymentCancellationReason6
import SupplementaryData1
import OriginalTransactionReference42
import DateAndDateTime2Choice
import Max35Text
import ActiveOrHistoricCurrencyAndAmount
import UUIDv4Identifier
import ISODate
import Case6

class PaymentTransaction154(base_types._BaseFieldType):

	__slots__ = ["_OrgnlReqdColltnDt", "_OrgnlReqdExctnDt", "_CxlId", "_SplmtryData", "_OrgnlUETR", "_CxlRsnInf", "_Case", "_OrgnlTxRef", "_OrgnlInstdAmt", "_OrgnlEndToEndId", "_OrgnlInstrId"]
	@property
	def OrgnlReqdColltnDt(self):
		return self._OrgnlReqdColltnDt

	@OrgnlReqdColltnDt.setter
	def OrgnlReqdColltnDt(self, value):
		self._OrgnlReqdColltnDt = value if type(value) != auto else self.make_default("OrgnlReqdColltnDt")

	@OrgnlReqdColltnDt.deleter
	def OrgnlReqdColltnDt(self):
		del self._OrgnlReqdColltnDt
		self._OrgnlReqdColltnDt = None

	@property
	def OrgnlReqdExctnDt(self):
		return self._OrgnlReqdExctnDt

	@OrgnlReqdExctnDt.setter
	def OrgnlReqdExctnDt(self, value):
		self._OrgnlReqdExctnDt = value if type(value) != auto else self.make_default("OrgnlReqdExctnDt")

	@OrgnlReqdExctnDt.deleter
	def OrgnlReqdExctnDt(self):
		del self._OrgnlReqdExctnDt
		self._OrgnlReqdExctnDt = None

	@property
	def CxlId(self):
		return self._CxlId

	@CxlId.setter
	def CxlId(self, value):
		self._CxlId = value if type(value) != auto else self.make_default("CxlId")

	@CxlId.deleter
	def CxlId(self):
		del self._CxlId
		self._CxlId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if type(value) != auto else self.make_default("OrgnlUETR")

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = None

	@property
	def CxlRsnInf(self):
		return self._CxlRsnInf

	@CxlRsnInf.setter
	def CxlRsnInf(self, value):
		self._CxlRsnInf = value if type(value) != auto else self.make_default("CxlRsnInf")

	@CxlRsnInf.deleter
	def CxlRsnInf(self):
		del self._CxlRsnInf
		self._CxlRsnInf = None

	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if type(value) != auto else self.make_default("Case")

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = None

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if type(value) != auto else self.make_default("OrgnlTxRef")

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = None

	@property
	def OrgnlInstdAmt(self):
		return self._OrgnlInstdAmt

	@OrgnlInstdAmt.setter
	def OrgnlInstdAmt(self, value):
		self._OrgnlInstdAmt = value if type(value) != auto else self.make_default("OrgnlInstdAmt")

	@OrgnlInstdAmt.deleter
	def OrgnlInstdAmt(self):
		del self._OrgnlInstdAmt
		self._OrgnlInstdAmt = None

	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if type(value) != auto else self.make_default("OrgnlEndToEndId")

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = None

	@property
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if type(value) != auto else self.make_default("OrgnlInstrId")

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlReqdColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsnInf', type=PaymentCancellationReason6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

