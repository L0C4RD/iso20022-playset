from . import base_types
from .YesNoIndicator import YesNoIndicator

class ReconciliationCategory4(base_types._BaseFieldType):

	__slots__ = ["_FrthrMod", "_Rvvd"]
	@property
	def FrthrMod(self):
		return self._FrthrMod

	@FrthrMod.setter
	def FrthrMod(self, value):
		self._FrthrMod = value if type(value) != base_types.auto else self.make_default("FrthrMod")

	@FrthrMod.deleter
	def FrthrMod(self):
		del self._FrthrMod
		self._FrthrMod = None

	@property
	def Rvvd(self):
		return self._Rvvd

	@Rvvd.setter
	def Rvvd(self, value):
		self._Rvvd = value if type(value) != base_types.auto else self.make_default("Rvvd")

	@Rvvd.deleter
	def Rvvd(self):
		del self._Rvvd
		self._Rvvd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrthrMod', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvvd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

