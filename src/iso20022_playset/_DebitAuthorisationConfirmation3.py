from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max140Text import Max140Text
from ._TrueFalseIndicator import TrueFalseIndicator
from ._CashAccount40 import CashAccount40
from ._Max52Text import Max52Text
from ._ISODate import ISODate

class DebitAuthorisationConfirmation3(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_CmonTxId", "_AmtToDbt", "_DbtAuthstn", "_ValDtToDbt", "_Rsn"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def CmonTxId(self):
		return self._CmonTxId

	@CmonTxId.setter
	def CmonTxId(self, value):
		self._CmonTxId = value if type(value) != base_types.auto else self.make_default("CmonTxId")

	@CmonTxId.deleter
	def CmonTxId(self):
		del self._CmonTxId
		self._CmonTxId = None

	@property
	def AmtToDbt(self):
		return self._AmtToDbt

	@AmtToDbt.setter
	def AmtToDbt(self, value):
		self._AmtToDbt = value if type(value) != base_types.auto else self.make_default("AmtToDbt")

	@AmtToDbt.deleter
	def AmtToDbt(self):
		del self._AmtToDbt
		self._AmtToDbt = None

	@property
	def DbtAuthstn(self):
		return self._DbtAuthstn

	@DbtAuthstn.setter
	def DbtAuthstn(self, value):
		self._DbtAuthstn = value if type(value) != base_types.auto else self.make_default("DbtAuthstn")

	@DbtAuthstn.deleter
	def DbtAuthstn(self):
		del self._DbtAuthstn
		self._DbtAuthstn = None

	@property
	def ValDtToDbt(self):
		return self._ValDtToDbt

	@ValDtToDbt.setter
	def ValDtToDbt(self, value):
		self._ValDtToDbt = value if type(value) != base_types.auto else self.make_default("ValDtToDbt")

	@ValDtToDbt.deleter
	def ValDtToDbt(self):
		del self._ValDtToDbt
		self._ValDtToDbt = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonTxId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtToDbt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtAuthstn', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDtToDbt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

