import base_types
import ActiveCurrencyAndAmount
import PercentageRate
import ActiveOrHistoricCurrencyAndAmount
import EqualisationMethodologyType2

class Equalisation3(base_types._BaseFieldType):

	__slots__ = ["_GrssAsstVal", "_Amt", "_HghWtrmrk", "_Rate", "_EqulstnMthdlgyTp"]
	@property
	def GrssAsstVal(self):
		return self._GrssAsstVal

	@GrssAsstVal.setter
	def GrssAsstVal(self, value):
		self._GrssAsstVal = value if type(value) != auto else self.make_default("GrssAsstVal")

	@GrssAsstVal.deleter
	def GrssAsstVal(self):
		del self._GrssAsstVal
		self._GrssAsstVal = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def HghWtrmrk(self):
		return self._HghWtrmrk

	@HghWtrmrk.setter
	def HghWtrmrk(self, value):
		self._HghWtrmrk = value if type(value) != auto else self.make_default("HghWtrmrk")

	@HghWtrmrk.deleter
	def HghWtrmrk(self):
		del self._HghWtrmrk
		self._HghWtrmrk = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def EqulstnMthdlgyTp(self):
		return self._EqulstnMthdlgyTp

	@EqulstnMthdlgyTp.setter
	def EqulstnMthdlgyTp(self, value):
		self._EqulstnMthdlgyTp = value if type(value) != auto else self.make_default("EqulstnMthdlgyTp")

	@EqulstnMthdlgyTp.deleter
	def EqulstnMthdlgyTp(self):
		del self._EqulstnMthdlgyTp
		self._EqulstnMthdlgyTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrssAsstVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghWtrmrk', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnMthdlgyTp', type=EqualisationMethodologyType2, min=0, max=2, mutex_group=None, array=True),
	))

