from . import base_types
from .ISODate import ISODate

class EligibilityDates1(base_types._BaseFieldType):

	__slots__ = ["_EntitlmntFxgDt"]
	@property
	def EntitlmntFxgDt(self):
		return self._EntitlmntFxgDt

	@EntitlmntFxgDt.setter
	def EntitlmntFxgDt(self, value):
		self._EntitlmntFxgDt = value if type(value) != auto else self.make_default("EntitlmntFxgDt")

	@EntitlmntFxgDt.deleter
	def EntitlmntFxgDt(self):
		del self._EntitlmntFxgDt
		self._EntitlmntFxgDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EntitlmntFxgDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

