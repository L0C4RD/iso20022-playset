# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import Frequency3Code
from . import GracePeriod1
from . import Max35Text
from . import Number

class RecurringTransaction7(base_types._BaseFieldType):

	__slots__ = ["_GracePrd", "_PlanId", "_PlanNtce", "_PrdUnit", "_SeqNb"]
	@property
	def GracePrd(self):
		return self._GracePrd

	@GracePrd.setter
	def GracePrd(self, value):
		self._GracePrd = value if value is not None else base_types.UninitialisedField(self, 'GracePrd', GracePeriod1, True)

	@GracePrd.deleter
	def GracePrd(self):
		del self._GracePrd
		self._GracePrd = base_types.UninitialisedField(self, 'GracePrd', GracePeriod1, True)

	@property
	def PlanId(self):
		return self._PlanId

	@PlanId.setter
	def PlanId(self, value):
		self._PlanId = value if value is not None else base_types.UninitialisedField(self, 'PlanId', Max35Text, False)

	@PlanId.deleter
	def PlanId(self):
		del self._PlanId
		self._PlanId = base_types.UninitialisedField(self, 'PlanId', Max35Text, False)

	@property
	def PlanNtce(self):
		return self._PlanNtce

	@PlanNtce.setter
	def PlanNtce(self, value):
		self._PlanNtce = value if value is not None else base_types.UninitialisedField(self, 'PlanNtce', ActionMessage12, True)

	@PlanNtce.deleter
	def PlanNtce(self):
		del self._PlanNtce
		self._PlanNtce = base_types.UninitialisedField(self, 'PlanNtce', ActionMessage12, True)

	@property
	def PrdUnit(self):
		return self._PrdUnit

	@PrdUnit.setter
	def PrdUnit(self, value):
		self._PrdUnit = value if value is not None else base_types.UninitialisedField(self, 'PrdUnit', Frequency3Code, False)

	@PrdUnit.deleter
	def PrdUnit(self):
		del self._PrdUnit
		self._PrdUnit = base_types.UninitialisedField(self, 'PrdUnit', Frequency3Code, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GracePrd', type=GracePeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlanId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanNtce', type=ActionMessage12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrdUnit', type=Frequency3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
	))