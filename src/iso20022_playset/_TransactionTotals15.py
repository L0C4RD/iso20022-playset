from . import base_types
from ._AdditionalFeeReconciliation4 import AdditionalFeeReconciliation4
from ._CreditDebit3Code import CreditDebit3Code
from ._FinancialReconciliation4 import FinancialReconciliation4
from ._ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from ._ISODate import ISODate
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text
from ._MessageReconciliation4 import MessageReconciliation4

class TransactionTotals15(base_types._BaseFieldType):

	__slots__ = ["_AddtlFeeRcncltn", "_Amt", "_Ccy", "_CdtDbt", "_ChckptRef", "_Dt", "_Fin", "_Id", "_Msg"]
	@property
	def AddtlFeeRcncltn(self):
		return self._AddtlFeeRcncltn

	@AddtlFeeRcncltn.setter
	def AddtlFeeRcncltn(self, value):
		self._AddtlFeeRcncltn = value if type(value) != base_types.auto else self.make_default("AddtlFeeRcncltn")

	@AddtlFeeRcncltn.deleter
	def AddtlFeeRcncltn(self):
		del self._AddtlFeeRcncltn
		self._AddtlFeeRcncltn = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != base_types.auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def ChckptRef(self):
		return self._ChckptRef

	@ChckptRef.setter
	def ChckptRef(self, value):
		self._ChckptRef = value if type(value) != base_types.auto else self.make_default("ChckptRef")

	@ChckptRef.deleter
	def ChckptRef(self):
		del self._ChckptRef
		self._ChckptRef = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Fin(self):
		return self._Fin

	@Fin.setter
	def Fin(self, value):
		self._Fin = value if type(value) != base_types.auto else self.make_default("Fin")

	@Fin.deleter
	def Fin(self):
		del self._Fin
		self._Fin = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Msg(self):
		return self._Msg

	@Msg.setter
	def Msg(self, value):
		self._Msg = value if type(value) != base_types.auto else self.make_default("Msg")

	@Msg.deleter
	def Msg(self):
		del self._Msg
		self._Msg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlFeeRcncltn', type=AdditionalFeeReconciliation4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckptRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fin', type=FinancialReconciliation4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Msg', type=MessageReconciliation4, min=0, max=None, mutex_group=None, array=True),
	))

