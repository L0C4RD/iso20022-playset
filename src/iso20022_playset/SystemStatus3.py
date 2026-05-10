from . import base_types
from .SystemStatus2Choice import SystemStatus2Choice
from .DateTimePeriod1Choice import DateTimePeriod1Choice

class SystemStatus3(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_VldtyTm"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def VldtyTm(self):
		return self._VldtyTm

	@VldtyTm.setter
	def VldtyTm(self, value):
		self._VldtyTm = value if type(value) != auto else self.make_default("VldtyTm")

	@VldtyTm.deleter
	def VldtyTm(self):
		del self._VldtyTm
		self._VldtyTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=SystemStatus2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
	))

