import base_types
import Max35Text
import ActiveOrHistoricCurrencyAndAmount
import Purpose2Choice
import CashAccount40
import CreditDebitCode
import References74Choice

class TransactionAllocation1(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_CdtDbtInd", "_Ref", "_Amt", "_RltdRefs", "_Purp"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def RltdRefs(self):
		return self._RltdRefs

	@RltdRefs.setter
	def RltdRefs(self, value):
		self._RltdRefs = value if type(value) != auto else self.make_default("RltdRefs")

	@RltdRefs.deleter
	def RltdRefs(self):
		del self._RltdRefs
		self._RltdRefs = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRefs', type=References74Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=1, max=1, mutex_group=None, array=False),
	))

