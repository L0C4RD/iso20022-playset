# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ActiveOrHistoricCurrencyAndAmount
from . import EqualisationMethodologyType2
from . import PercentageRate

class Equalisation3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_EqulstnMthdlgyTp", "_GrssAsstVal", "_HghWtrmrk", "_Rate"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def EqulstnMthdlgyTp(self):
		return self._EqulstnMthdlgyTp

	@EqulstnMthdlgyTp.setter
	def EqulstnMthdlgyTp(self, value):
		self._EqulstnMthdlgyTp = value if value is not None else base_types.UninitialisedField(self, 'EqulstnMthdlgyTp', EqualisationMethodologyType2, True)

	@EqulstnMthdlgyTp.deleter
	def EqulstnMthdlgyTp(self):
		del self._EqulstnMthdlgyTp
		self._EqulstnMthdlgyTp = base_types.UninitialisedField(self, 'EqulstnMthdlgyTp', EqualisationMethodologyType2, True)

	@property
	def GrssAsstVal(self):
		return self._GrssAsstVal

	@GrssAsstVal.setter
	def GrssAsstVal(self, value):
		self._GrssAsstVal = value if value is not None else base_types.UninitialisedField(self, 'GrssAsstVal', ActiveOrHistoricCurrencyAndAmount, False)

	@GrssAsstVal.deleter
	def GrssAsstVal(self):
		del self._GrssAsstVal
		self._GrssAsstVal = base_types.UninitialisedField(self, 'GrssAsstVal', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def HghWtrmrk(self):
		return self._HghWtrmrk

	@HghWtrmrk.setter
	def HghWtrmrk(self, value):
		self._HghWtrmrk = value if value is not None else base_types.UninitialisedField(self, 'HghWtrmrk', ActiveOrHistoricCurrencyAndAmount, False)

	@HghWtrmrk.deleter
	def HghWtrmrk(self):
		del self._HghWtrmrk
		self._HghWtrmrk = base_types.UninitialisedField(self, 'HghWtrmrk', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnMthdlgyTp', type=EqualisationMethodologyType2, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrssAsstVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghWtrmrk', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))