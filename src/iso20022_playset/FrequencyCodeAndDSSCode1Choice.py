from . import base_types
import GenericIdentification7
import EventFrequency1Code

class FrequencyCodeAndDSSCode1Choice(base_types._BaseFieldType):

	__slots__ = ["_FrqcyAsCd", "_FrqcyAsDSS"]
	@property
	def FrqcyAsCd(self):
		return self._FrqcyAsCd

	@FrqcyAsCd.setter
	def FrqcyAsCd(self, value):
		self._FrqcyAsCd = value if type(value) != auto else self.make_default("FrqcyAsCd")

	@FrqcyAsCd.deleter
	def FrqcyAsCd(self):
		del self._FrqcyAsCd
		self._FrqcyAsCd = None

	@property
	def FrqcyAsDSS(self):
		return self._FrqcyAsDSS

	@FrqcyAsDSS.setter
	def FrqcyAsDSS(self, value):
		self._FrqcyAsDSS = value if type(value) != auto else self.make_default("FrqcyAsDSS")

	@FrqcyAsDSS.deleter
	def FrqcyAsDSS(self):
		del self._FrqcyAsDSS
		self._FrqcyAsDSS = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrqcyAsCd', type=EventFrequency1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrqcyAsDSS', type=GenericIdentification7, min=0, max=1, mutex_group=1, array=False),
	))

