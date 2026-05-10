import base_types
import ISODate
import PriceStatus2Code

class ExerciseDate1Choice(base_types._BaseFieldType):

	__slots__ = ["_PdgDtAplbl", "_FrstExrcDt"]
	@property
	def PdgDtAplbl(self):
		return self._PdgDtAplbl

	@PdgDtAplbl.setter
	def PdgDtAplbl(self, value):
		self._PdgDtAplbl = value if type(value) != auto else self.make_default("PdgDtAplbl")

	@PdgDtAplbl.deleter
	def PdgDtAplbl(self):
		del self._PdgDtAplbl
		self._PdgDtAplbl = None

	@property
	def FrstExrcDt(self):
		return self._FrstExrcDt

	@FrstExrcDt.setter
	def FrstExrcDt(self, value):
		self._FrstExrcDt = value if type(value) != auto else self.make_default("FrstExrcDt")

	@FrstExrcDt.deleter
	def FrstExrcDt(self):
		del self._FrstExrcDt
		self._FrstExrcDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgDtAplbl', type=PriceStatus2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrstExrcDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))

