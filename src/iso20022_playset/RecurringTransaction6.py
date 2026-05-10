from . import base_types
from .Max35Text import Max35Text
from .GracePeriod1 import GracePeriod1
from .Number import Number
from .Frequency3Code import Frequency3Code
from .ActionMessage11 import ActionMessage11

class RecurringTransaction6(base_types._BaseFieldType):

	__slots__ = ["_PrdUnit", "_SeqNb", "_PlanId", "_GracePrd", "_PlanNtce"]
	@property
	def PrdUnit(self):
		return self._PrdUnit

	@PrdUnit.setter
	def PrdUnit(self, value):
		self._PrdUnit = value if type(value) != auto else self.make_default("PrdUnit")

	@PrdUnit.deleter
	def PrdUnit(self):
		del self._PrdUnit
		self._PrdUnit = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def PlanId(self):
		return self._PlanId

	@PlanId.setter
	def PlanId(self, value):
		self._PlanId = value if type(value) != auto else self.make_default("PlanId")

	@PlanId.deleter
	def PlanId(self):
		del self._PlanId
		self._PlanId = None

	@property
	def GracePrd(self):
		return self._GracePrd

	@GracePrd.setter
	def GracePrd(self, value):
		self._GracePrd = value if type(value) != auto else self.make_default("GracePrd")

	@GracePrd.deleter
	def GracePrd(self):
		del self._GracePrd
		self._GracePrd = None

	@property
	def PlanNtce(self):
		return self._PlanNtce

	@PlanNtce.setter
	def PlanNtce(self, value):
		self._PlanNtce = value if type(value) != auto else self.make_default("PlanNtce")

	@PlanNtce.deleter
	def PlanNtce(self):
		del self._PlanNtce
		self._PlanNtce = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrdUnit', type=Frequency3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GracePrd', type=GracePeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlanNtce', type=ActionMessage11, min=0, max=None, mutex_group=None, array=True),
	))

