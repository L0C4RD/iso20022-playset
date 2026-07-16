# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarketIdentification1Choice
from . import PercentageRate
from . import TrueFalseIndicator

class PenaltyRate1(base_types._BaseFieldType):

	__slots__ = ["_MktId", "_Rate", "_SMEGrwthMkt"]
	@property
	def MktId(self):
		return self._MktId

	@MktId.setter
	def MktId(self, value):
		self._MktId = value if value is not None else base_types.UninitialisedField(self, 'MktId', MarketIdentification1Choice, False)

	@MktId.deleter
	def MktId(self):
		del self._MktId
		self._MktId = base_types.UninitialisedField(self, 'MktId', MarketIdentification1Choice, False)

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

	@property
	def SMEGrwthMkt(self):
		return self._SMEGrwthMkt

	@SMEGrwthMkt.setter
	def SMEGrwthMkt(self, value):
		self._SMEGrwthMkt = value if value is not None else base_types.UninitialisedField(self, 'SMEGrwthMkt', TrueFalseIndicator, False)

	@SMEGrwthMkt.deleter
	def SMEGrwthMkt(self):
		del self._SMEGrwthMkt
		self._SMEGrwthMkt = base_types.UninitialisedField(self, 'SMEGrwthMkt', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktId', type=MarketIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SMEGrwthMkt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))