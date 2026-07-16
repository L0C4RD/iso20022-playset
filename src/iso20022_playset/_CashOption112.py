# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account12Choice
from . import CreditDebitCode
from . import DateAndDateTime2Choice
from . import ISODate
from . import RestrictedFINActiveCurrencyAndAmount

class CashOption112(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_CdtDbtInd", "_OrgnlPstngDt", "_PstngAmt", "_PstngDt", "_ValDt"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', Account12Choice, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', Account12Choice, False)

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def OrgnlPstngDt(self):
		return self._OrgnlPstngDt

	@OrgnlPstngDt.setter
	def OrgnlPstngDt(self, value):
		self._OrgnlPstngDt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPstngDt', DateAndDateTime2Choice, False)

	@OrgnlPstngDt.deleter
	def OrgnlPstngDt(self):
		del self._OrgnlPstngDt
		self._OrgnlPstngDt = base_types.UninitialisedField(self, 'OrgnlPstngDt', DateAndDateTime2Choice, False)

	@property
	def PstngAmt(self):
		return self._PstngAmt

	@PstngAmt.setter
	def PstngAmt(self, value):
		self._PstngAmt = value if value is not None else base_types.UninitialisedField(self, 'PstngAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@PstngAmt.deleter
	def PstngAmt(self):
		del self._PstngAmt
		self._PstngAmt = base_types.UninitialisedField(self, 'PstngAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def PstngDt(self):
		return self._PstngDt

	@PstngDt.setter
	def PstngDt(self, value):
		self._PstngDt = value if value is not None else base_types.UninitialisedField(self, 'PstngDt', DateAndDateTime2Choice, False)

	@PstngDt.deleter
	def PstngDt(self):
		del self._PstngDt
		self._PstngDt = base_types.UninitialisedField(self, 'PstngDt', DateAndDateTime2Choice, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=Account12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPstngDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngAmt', type=RestrictedFINActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))