# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementFailsDailyInstructionType1Choice

class SettlementFailsDailyCSD3(base_types._BaseFieldType):

	__slots__ = ["_CrossCSD", "_IntraCSD"]
	@property
	def CrossCSD(self):
		return self._CrossCSD

	@CrossCSD.setter
	def CrossCSD(self, value):
		self._CrossCSD = value if value is not None else base_types.UninitialisedField(self, 'CrossCSD', SettlementFailsDailyInstructionType1Choice, False)

	@CrossCSD.deleter
	def CrossCSD(self):
		del self._CrossCSD
		self._CrossCSD = base_types.UninitialisedField(self, 'CrossCSD', SettlementFailsDailyInstructionType1Choice, False)

	@property
	def IntraCSD(self):
		return self._IntraCSD

	@IntraCSD.setter
	def IntraCSD(self, value):
		self._IntraCSD = value if value is not None else base_types.UninitialisedField(self, 'IntraCSD', SettlementFailsDailyInstructionType1Choice, False)

	@IntraCSD.deleter
	def IntraCSD(self):
		del self._IntraCSD
		self._IntraCSD = base_types.UninitialisedField(self, 'IntraCSD', SettlementFailsDailyInstructionType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrossCSD', type=SettlementFailsDailyInstructionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraCSD', type=SettlementFailsDailyInstructionType1Choice, min=1, max=1, mutex_group=None, array=False),
	))