import base_types
import TargetMarket1Choice
import AdditionalInformation15
import Max35Text

class OtherTargetMarketRiskTolerance1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Trgt", "_RskTlrnceTp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if type(value) != auto else self.make_default("Trgt")

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = None

	@property
	def RskTlrnceTp(self):
		return self._RskTlrnceTp

	@RskTlrnceTp.setter
	def RskTlrnceTp(self, value):
		self._RskTlrnceTp = value if type(value) != auto else self.make_default("RskTlrnceTp")

	@RskTlrnceTp.deleter
	def RskTlrnceTp(self):
		del self._RskTlrnceTp
		self._RskTlrnceTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trgt', type=TargetMarket1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrnceTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

