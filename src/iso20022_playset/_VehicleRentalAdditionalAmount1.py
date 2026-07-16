# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CarRentalServiceType3Code
from . import CreditDebit3Code
from . import ImpliedCurrencyAndAmount
from . import TrueFalseIndicator

class VehicleRentalAdditionalAmount1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbt", "_CstmrNtfd", "_Tp"]
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
	def CstmrNtfd(self):
		return self._CstmrNtfd

	@CstmrNtfd.setter
	def CstmrNtfd(self, value):
		self._CstmrNtfd = value if value is not None else base_types.UninitialisedField(self, 'CstmrNtfd', TrueFalseIndicator, False)

	@CstmrNtfd.deleter
	def CstmrNtfd(self):
		del self._CstmrNtfd
		self._CstmrNtfd = base_types.UninitialisedField(self, 'CstmrNtfd', TrueFalseIndicator, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CarRentalServiceType3Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CarRentalServiceType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrNtfd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CarRentalServiceType3Code, min=0, max=1, mutex_group=None, array=False),
	))