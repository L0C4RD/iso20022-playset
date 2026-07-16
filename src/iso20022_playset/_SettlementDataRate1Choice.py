# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate

class SettlementDataRate1Choice(base_types._BaseFieldType):

	__slots__ = ["_NbOfInstrs", "_ValOfInstrs"]
	@property
	def NbOfInstrs(self):
		return self._NbOfInstrs

	@NbOfInstrs.setter
	def NbOfInstrs(self, value):
		self._NbOfInstrs = value if value is not None else base_types.UninitialisedField(self, 'NbOfInstrs', PercentageRate, False)

	@NbOfInstrs.deleter
	def NbOfInstrs(self):
		del self._NbOfInstrs
		self._NbOfInstrs = base_types.UninitialisedField(self, 'NbOfInstrs', PercentageRate, False)

	@property
	def ValOfInstrs(self):
		return self._ValOfInstrs

	@ValOfInstrs.setter
	def ValOfInstrs(self, value):
		self._ValOfInstrs = value if value is not None else base_types.UninitialisedField(self, 'ValOfInstrs', PercentageRate, False)

	@ValOfInstrs.deleter
	def ValOfInstrs(self):
		del self._ValOfInstrs
		self._ValOfInstrs = base_types.UninitialisedField(self, 'ValOfInstrs', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfInstrs', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ValOfInstrs', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))