from . import base_types
from ._RestrictedFINActiveCurrencyAndAmount import RestrictedFINActiveCurrencyAndAmount
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._CreditDebitCode import CreditDebitCode
from ._ISODate import ISODate
from ._Account12Choice import Account12Choice

class CashOption112(base_types._BaseFieldType):

	__slots__ = ["_OrgnlPstngDt", "_PstngAmt", "_Acct", "_ValDt", "_PstngDt", "_CdtDbtInd"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlPstngDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngAmt', type=RestrictedFINActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=Account12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
	))

