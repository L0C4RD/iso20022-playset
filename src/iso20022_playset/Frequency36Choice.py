import base_types
import Frequency6Code
import FrequencyPeriod1
import FrequencyAndMoment1

class Frequency36Choice(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_PtInTm", "_Prd"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def PtInTm(self):
		return self._PtInTm

	@PtInTm.setter
	def PtInTm(self, value):
		self._PtInTm = value if type(value) != auto else self.make_default("PtInTm")

	@PtInTm.deleter
	def PtInTm(self):
		del self._PtInTm
		self._PtInTm = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Frequency6Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtInTm', type=FrequencyAndMoment1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prd', type=FrequencyPeriod1, min=0, max=1, mutex_group=1, array=False),
	))

