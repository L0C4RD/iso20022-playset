# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate
from . import PercentageRate

class ExchangeRateOrPercentage1Choice(base_types._BaseFieldType):

	__slots__ = ["_Pctg", "_Rate"]
	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if value is not None else base_types.UninitialisedField(self, 'Pctg', PercentageRate, False)

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = base_types.UninitialisedField(self, 'Pctg', PercentageRate, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', BaseOneRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
	))