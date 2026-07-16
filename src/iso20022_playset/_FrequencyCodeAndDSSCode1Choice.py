# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EventFrequency1Code
from . import GenericIdentification7

class FrequencyCodeAndDSSCode1Choice(base_types._BaseFieldType):

	__slots__ = ["_FrqcyAsCd", "_FrqcyAsDSS"]
	@property
	def FrqcyAsCd(self):
		return self._FrqcyAsCd

	@FrqcyAsCd.setter
	def FrqcyAsCd(self, value):
		self._FrqcyAsCd = value if value is not None else base_types.UninitialisedField(self, 'FrqcyAsCd', EventFrequency1Code, False)

	@FrqcyAsCd.deleter
	def FrqcyAsCd(self):
		del self._FrqcyAsCd
		self._FrqcyAsCd = base_types.UninitialisedField(self, 'FrqcyAsCd', EventFrequency1Code, False)

	@property
	def FrqcyAsDSS(self):
		return self._FrqcyAsDSS

	@FrqcyAsDSS.setter
	def FrqcyAsDSS(self, value):
		self._FrqcyAsDSS = value if value is not None else base_types.UninitialisedField(self, 'FrqcyAsDSS', GenericIdentification7, False)

	@FrqcyAsDSS.deleter
	def FrqcyAsDSS(self):
		del self._FrqcyAsDSS
		self._FrqcyAsDSS = base_types.UninitialisedField(self, 'FrqcyAsDSS', GenericIdentification7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrqcyAsCd', type=EventFrequency1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrqcyAsDSS', type=GenericIdentification7, min=0, max=1, mutex_group=1, array=False),
	))