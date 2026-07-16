# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Number
from . import ReconciliationCategory1Code
from . import ReconciliationImpact1Code

class FinancialReconciliation3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Cnt", "_Impct", "_OthrTp", "_Tp"]
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
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if value is not None else base_types.UninitialisedField(self, 'Cnt', Number, False)

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = base_types.UninitialisedField(self, 'Cnt', Number, False)

	@property
	def Impct(self):
		return self._Impct

	@Impct.setter
	def Impct(self, value):
		self._Impct = value if value is not None else base_types.UninitialisedField(self, 'Impct', ReconciliationImpact1Code, False)

	@Impct.deleter
	def Impct(self):
		del self._Impct
		self._Impct = base_types.UninitialisedField(self, 'Impct', ReconciliationImpact1Code, False)

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ReconciliationCategory1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ReconciliationCategory1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnt', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Impct', type=ReconciliationImpact1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReconciliationCategory1Code, min=1, max=1, mutex_group=None, array=False),
	))