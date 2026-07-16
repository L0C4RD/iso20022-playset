# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import CancellationReason33Choice
from . import CashAccount40
from . import ISODate
from . import Max140Text

class DebitAuthorisation3(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AddtlCxlRsnInf", "_AmtToDbt", "_CxlRsn", "_ValDtToDbt"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@property
	def AddtlCxlRsnInf(self):
		return self._AddtlCxlRsnInf

	@AddtlCxlRsnInf.setter
	def AddtlCxlRsnInf(self, value):
		self._AddtlCxlRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlCxlRsnInf', Max140Text, True)

	@AddtlCxlRsnInf.deleter
	def AddtlCxlRsnInf(self):
		del self._AddtlCxlRsnInf
		self._AddtlCxlRsnInf = base_types.UninitialisedField(self, 'AddtlCxlRsnInf', Max140Text, True)

	@property
	def AmtToDbt(self):
		return self._AmtToDbt

	@AmtToDbt.setter
	def AmtToDbt(self, value):
		self._AmtToDbt = value if value is not None else base_types.UninitialisedField(self, 'AmtToDbt', ActiveOrHistoricCurrencyAndAmount, False)

	@AmtToDbt.deleter
	def AmtToDbt(self):
		del self._AmtToDbt
		self._AmtToDbt = base_types.UninitialisedField(self, 'AmtToDbt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', CancellationReason33Choice, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', CancellationReason33Choice, False)

	@property
	def ValDtToDbt(self):
		return self._ValDtToDbt

	@ValDtToDbt.setter
	def ValDtToDbt(self, value):
		self._ValDtToDbt = value if value is not None else base_types.UninitialisedField(self, 'ValDtToDbt', ISODate, False)

	@ValDtToDbt.deleter
	def ValDtToDbt(self):
		del self._ValDtToDbt
		self._ValDtToDbt = base_types.UninitialisedField(self, 'ValDtToDbt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlCxlRsnInf', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtToDbt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=CancellationReason33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDtToDbt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))