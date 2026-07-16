# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalFeeReconciliation3
from . import CreditDebit3Code
from . import FinancialReconciliation3
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import MessageReconciliation3
from . import Min2Max3NumericText

class TransactionTotals14(base_types._BaseFieldType):

	__slots__ = ["_AddtlFeeRcncltn", "_Amt", "_Ccy", "_CdtDbt", "_ChckptRef", "_Dt", "_Fin", "_Id", "_Msg"]
	@property
	def AddtlFeeRcncltn(self):
		return self._AddtlFeeRcncltn

	@AddtlFeeRcncltn.setter
	def AddtlFeeRcncltn(self, value):
		self._AddtlFeeRcncltn = value if value is not None else base_types.UninitialisedField(self, 'AddtlFeeRcncltn', AdditionalFeeReconciliation3, True)

	@AddtlFeeRcncltn.deleter
	def AddtlFeeRcncltn(self):
		del self._AddtlFeeRcncltn
		self._AddtlFeeRcncltn = base_types.UninitialisedField(self, 'AddtlFeeRcncltn', AdditionalFeeReconciliation3, True)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', Min2Max3NumericText, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', Min2Max3NumericText, False)

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@property
	def ChckptRef(self):
		return self._ChckptRef

	@ChckptRef.setter
	def ChckptRef(self, value):
		self._ChckptRef = value if value is not None else base_types.UninitialisedField(self, 'ChckptRef', Max35Text, False)

	@ChckptRef.deleter
	def ChckptRef(self):
		del self._ChckptRef
		self._ChckptRef = base_types.UninitialisedField(self, 'ChckptRef', Max35Text, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def Fin(self):
		return self._Fin

	@Fin.setter
	def Fin(self, value):
		self._Fin = value if value is not None else base_types.UninitialisedField(self, 'Fin', FinancialReconciliation3, True)

	@Fin.deleter
	def Fin(self):
		del self._Fin
		self._Fin = base_types.UninitialisedField(self, 'Fin', FinancialReconciliation3, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def Msg(self):
		return self._Msg

	@Msg.setter
	def Msg(self, value):
		self._Msg = value if value is not None else base_types.UninitialisedField(self, 'Msg', MessageReconciliation3, True)

	@Msg.deleter
	def Msg(self):
		del self._Msg
		self._Msg = base_types.UninitialisedField(self, 'Msg', MessageReconciliation3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlFeeRcncltn', type=AdditionalFeeReconciliation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=Min2Max3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckptRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fin', type=FinancialReconciliation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Msg', type=MessageReconciliation3, min=0, max=None, mutex_group=None, array=True),
	))