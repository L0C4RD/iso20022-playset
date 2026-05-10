from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._PercentageRate import PercentageRate
from ._EqualisationMethodologyType1Code import EqualisationMethodologyType1Code

class Equalisation4(base_types._BaseFieldType):

	__slots__ = ["_CntngntLqdtnPerUnit", "_DprctnDpstPerUnit", "_Amt", "_EqulstnCdtPerUnit", "_HghWtrmrk", "_GrssAsstVal", "_Rate", "_EqulstnMthdlgyTp"]
	@property
	def CntngntLqdtnPerUnit(self):
		return self._CntngntLqdtnPerUnit

	@CntngntLqdtnPerUnit.setter
	def CntngntLqdtnPerUnit(self, value):
		self._CntngntLqdtnPerUnit = value if type(value) != base_types.auto else self.make_default("CntngntLqdtnPerUnit")

	@CntngntLqdtnPerUnit.deleter
	def CntngntLqdtnPerUnit(self):
		del self._CntngntLqdtnPerUnit
		self._CntngntLqdtnPerUnit = None

	@property
	def DprctnDpstPerUnit(self):
		return self._DprctnDpstPerUnit

	@DprctnDpstPerUnit.setter
	def DprctnDpstPerUnit(self, value):
		self._DprctnDpstPerUnit = value if type(value) != base_types.auto else self.make_default("DprctnDpstPerUnit")

	@DprctnDpstPerUnit.deleter
	def DprctnDpstPerUnit(self):
		del self._DprctnDpstPerUnit
		self._DprctnDpstPerUnit = None

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
	def EqulstnCdtPerUnit(self):
		return self._EqulstnCdtPerUnit

	@EqulstnCdtPerUnit.setter
	def EqulstnCdtPerUnit(self, value):
		self._EqulstnCdtPerUnit = value if type(value) != base_types.auto else self.make_default("EqulstnCdtPerUnit")

	@EqulstnCdtPerUnit.deleter
	def EqulstnCdtPerUnit(self):
		del self._EqulstnCdtPerUnit
		self._EqulstnCdtPerUnit = None

	@property
	def HghWtrmrk(self):
		return self._HghWtrmrk

	@HghWtrmrk.setter
	def HghWtrmrk(self, value):
		self._HghWtrmrk = value if type(value) != base_types.auto else self.make_default("HghWtrmrk")

	@HghWtrmrk.deleter
	def HghWtrmrk(self):
		del self._HghWtrmrk
		self._HghWtrmrk = None

	@property
	def GrssAsstVal(self):
		return self._GrssAsstVal

	@GrssAsstVal.setter
	def GrssAsstVal(self, value):
		self._GrssAsstVal = value if type(value) != base_types.auto else self.make_default("GrssAsstVal")

	@GrssAsstVal.deleter
	def GrssAsstVal(self):
		del self._GrssAsstVal
		self._GrssAsstVal = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def EqulstnMthdlgyTp(self):
		return self._EqulstnMthdlgyTp

	@EqulstnMthdlgyTp.setter
	def EqulstnMthdlgyTp(self, value):
		self._EqulstnMthdlgyTp = value if type(value) != base_types.auto else self.make_default("EqulstnMthdlgyTp")

	@EqulstnMthdlgyTp.deleter
	def EqulstnMthdlgyTp(self):
		del self._EqulstnMthdlgyTp
		self._EqulstnMthdlgyTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntngntLqdtnPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DprctnDpstPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnCdtPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghWtrmrk', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAsstVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnMthdlgyTp', type=EqualisationMethodologyType1Code, min=0, max=1, mutex_group=None, array=False),
	))

