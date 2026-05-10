from . import base_types
from .AdditionalInformation15 import AdditionalInformation15
from .TargetMarket1Choice import TargetMarket1Choice
from .Max35Text import Max35Text

class OtherTargetMarketRiskTolerance1(base_types._BaseFieldType):

	__slots__ = ["_Trgt", "_RskTlrnceTp", "_AddtlInf"]
	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if type(value) != base_types.auto else self.make_default("Trgt")

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = None

	@property
	def RskTlrnceTp(self):
		return self._RskTlrnceTp

	@RskTlrnceTp.setter
	def RskTlrnceTp(self, value):
		self._RskTlrnceTp = value if type(value) != base_types.auto else self.make_default("RskTlrnceTp")

	@RskTlrnceTp.deleter
	def RskTlrnceTp(self):
		del self._RskTlrnceTp
		self._RskTlrnceTp = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trgt', type=TargetMarket1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrnceTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
	))

