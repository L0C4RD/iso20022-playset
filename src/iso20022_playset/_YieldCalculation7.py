# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CalculationType1Code
from . import DateTimePeriod1Choice
from . import ISODate
from . import PercentageRate
from . import Price14

class YieldCalculation7(base_types._BaseFieldType):

	__slots__ = ["_ClctnDt", "_ClctnTp", "_RedPric", "_Val", "_ValDt", "_ValPrd"]
	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if value is not None else base_types.UninitialisedField(self, 'ClctnDt', ISODate, False)

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = base_types.UninitialisedField(self, 'ClctnDt', ISODate, False)

	@property
	def ClctnTp(self):
		return self._ClctnTp

	@ClctnTp.setter
	def ClctnTp(self, value):
		self._ClctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClctnTp', CalculationType1Code, False)

	@ClctnTp.deleter
	def ClctnTp(self):
		del self._ClctnTp
		self._ClctnTp = base_types.UninitialisedField(self, 'ClctnTp', CalculationType1Code, False)

	@property
	def RedPric(self):
		return self._RedPric

	@RedPric.setter
	def RedPric(self, value):
		self._RedPric = value if value is not None else base_types.UninitialisedField(self, 'RedPric', Price14, False)

	@RedPric.deleter
	def RedPric(self):
		del self._RedPric
		self._RedPric = base_types.UninitialisedField(self, 'RedPric', Price14, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PercentageRate, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PercentageRate, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@property
	def ValPrd(self):
		return self._ValPrd

	@ValPrd.setter
	def ValPrd(self, value):
		self._ValPrd = value if value is not None else base_types.UninitialisedField(self, 'ValPrd', DateTimePeriod1Choice, False)

	@ValPrd.deleter
	def ValPrd(self):
		del self._ValPrd
		self._ValPrd = base_types.UninitialisedField(self, 'ValPrd', DateTimePeriod1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnTp', type=CalculationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValPrd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
	))