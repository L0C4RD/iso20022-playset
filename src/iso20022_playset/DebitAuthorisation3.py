import base_types
import ActiveOrHistoricCurrencyAndAmount
import CashAccount40
import ISODate
import CancellationReason33Choice
import Max140Text

class DebitAuthorisation3(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_Acct", "_AddtlCxlRsnInf", "_ValDtToDbt", "_AmtToDbt"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

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
	def AddtlCxlRsnInf(self):
		return self._AddtlCxlRsnInf

	@AddtlCxlRsnInf.setter
	def AddtlCxlRsnInf(self, value):
		self._AddtlCxlRsnInf = value if type(value) != auto else self.make_default("AddtlCxlRsnInf")

	@AddtlCxlRsnInf.deleter
	def AddtlCxlRsnInf(self):
		del self._AddtlCxlRsnInf
		self._AddtlCxlRsnInf = None

	@property
	def ValDtToDbt(self):
		return self._ValDtToDbt

	@ValDtToDbt.setter
	def ValDtToDbt(self, value):
		self._ValDtToDbt = value if type(value) != auto else self.make_default("ValDtToDbt")

	@ValDtToDbt.deleter
	def ValDtToDbt(self):
		del self._ValDtToDbt
		self._ValDtToDbt = None

	@property
	def AmtToDbt(self):
		return self._AmtToDbt

	@AmtToDbt.setter
	def AmtToDbt(self, value):
		self._AmtToDbt = value if type(value) != auto else self.make_default("AmtToDbt")

	@AmtToDbt.deleter
	def AmtToDbt(self):
		del self._AmtToDbt
		self._AmtToDbt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=CancellationReason33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlCxlRsnInf', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValDtToDbt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtToDbt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

