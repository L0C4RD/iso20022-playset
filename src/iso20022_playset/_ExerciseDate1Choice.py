# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import PriceStatus2Code

class ExerciseDate1Choice(base_types._BaseFieldType):

	__slots__ = ["_FrstExrcDt", "_PdgDtAplbl"]
	@property
	def FrstExrcDt(self):
		return self._FrstExrcDt

	@FrstExrcDt.setter
	def FrstExrcDt(self, value):
		self._FrstExrcDt = value if value is not None else base_types.UninitialisedField(self, 'FrstExrcDt', ISODate, False)

	@FrstExrcDt.deleter
	def FrstExrcDt(self):
		del self._FrstExrcDt
		self._FrstExrcDt = base_types.UninitialisedField(self, 'FrstExrcDt', ISODate, False)

	@property
	def PdgDtAplbl(self):
		return self._PdgDtAplbl

	@PdgDtAplbl.setter
	def PdgDtAplbl(self, value):
		self._PdgDtAplbl = value if value is not None else base_types.UninitialisedField(self, 'PdgDtAplbl', PriceStatus2Code, False)

	@PdgDtAplbl.deleter
	def PdgDtAplbl(self):
		del self._PdgDtAplbl
		self._PdgDtAplbl = base_types.UninitialisedField(self, 'PdgDtAplbl', PriceStatus2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstExrcDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgDtAplbl', type=PriceStatus2Code, min=0, max=1, mutex_group=1, array=False),
	))