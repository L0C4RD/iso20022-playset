from . import base_types
from .CreditDebitCode import CreditDebitCode
from .Account10Choice import Account10Choice
from .ISODate import ISODate
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .DateAndDateTime2Choice import DateAndDateTime2Choice

class CashOption109(base_types._BaseFieldType):

	__slots__ = ["_ValDt", "_PstngAmt", "_PstngDt", "_CdtDbtInd", "_OrgnlPstngDt", "_Acct"]
	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def PstngAmt(self):
		return self._PstngAmt

	@PstngAmt.setter
	def PstngAmt(self, value):
		self._PstngAmt = value if type(value) != base_types.auto else self.make_default("PstngAmt")

	@PstngAmt.deleter
	def PstngAmt(self):
		del self._PstngAmt
		self._PstngAmt = None

	@property
	def PstngDt(self):
		return self._PstngDt

	@PstngDt.setter
	def PstngDt(self, value):
		self._PstngDt = value if type(value) != base_types.auto else self.make_default("PstngDt")

	@PstngDt.deleter
	def PstngDt(self):
		del self._PstngDt
		self._PstngDt = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def OrgnlPstngDt(self):
		return self._OrgnlPstngDt

	@OrgnlPstngDt.setter
	def OrgnlPstngDt(self, value):
		self._OrgnlPstngDt = value if type(value) != base_types.auto else self.make_default("OrgnlPstngDt")

	@OrgnlPstngDt.deleter
	def OrgnlPstngDt(self):
		del self._OrgnlPstngDt
		self._OrgnlPstngDt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPstngDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=Account10Choice, min=0, max=1, mutex_group=None, array=False),
	))

