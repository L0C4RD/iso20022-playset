import base_types
import ImpliedCurrencyAndAmount
import Max10000Binary
import ActiveCurrencyCode
import TrueFalseIndicator
import ISODate

class CardPaymentTransactionDetails50(base_types._BaseFieldType):

	__slots__ = ["_KeepAuthstnOpn", "_VldtyDt", "_Ccy", "_ICCRltdData", "_TtlAmt"]
	@property
	def KeepAuthstnOpn(self):
		return self._KeepAuthstnOpn

	@KeepAuthstnOpn.setter
	def KeepAuthstnOpn(self, value):
		self._KeepAuthstnOpn = value if type(value) != auto else self.make_default("KeepAuthstnOpn")

	@KeepAuthstnOpn.deleter
	def KeepAuthstnOpn(self):
		del self._KeepAuthstnOpn
		self._KeepAuthstnOpn = None

	@property
	def VldtyDt(self):
		return self._VldtyDt

	@VldtyDt.setter
	def VldtyDt(self, value):
		self._VldtyDt = value if type(value) != auto else self.make_default("VldtyDt")

	@VldtyDt.deleter
	def VldtyDt(self):
		del self._VldtyDt
		self._VldtyDt = None

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
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='KeepAuthstnOpn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

