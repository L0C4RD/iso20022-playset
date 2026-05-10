import base_types
import InternalisationData2
import InternalisationDataRate1

class InternalisationData1(base_types._BaseFieldType):

	__slots__ = ["_Aggt", "_FaildRate"]
	@property
	def Aggt(self):
		return self._Aggt

	@Aggt.setter
	def Aggt(self, value):
		self._Aggt = value if type(value) != auto else self.make_default("Aggt")

	@Aggt.deleter
	def Aggt(self):
		del self._Aggt
		self._Aggt = None

	@property
	def FaildRate(self):
		return self._FaildRate

	@FaildRate.setter
	def FaildRate(self, value):
		self._FaildRate = value if type(value) != auto else self.make_default("FaildRate")

	@FaildRate.deleter
	def FaildRate(self):
		del self._FaildRate
		self._FaildRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Aggt', type=InternalisationData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaildRate', type=InternalisationDataRate1, min=1, max=1, mutex_group=None, array=False),
	))

