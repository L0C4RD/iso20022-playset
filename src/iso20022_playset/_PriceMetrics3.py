# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import Rates3

class PriceMetrics3(base_types._BaseFieldType):

	__slots__ = ["_LndgFee", "_Rates"]
	@property
	def LndgFee(self):
		return self._LndgFee

	@LndgFee.setter
	def LndgFee(self, value):
		self._LndgFee = value if value is not None else base_types.UninitialisedField(self, 'LndgFee', PercentageRate, False)

	@LndgFee.deleter
	def LndgFee(self):
		del self._LndgFee
		self._LndgFee = base_types.UninitialisedField(self, 'LndgFee', PercentageRate, False)

	@property
	def Rates(self):
		return self._Rates

	@Rates.setter
	def Rates(self, value):
		self._Rates = value if value is not None else base_types.UninitialisedField(self, 'Rates', Rates3, False)

	@Rates.deleter
	def Rates(self):
		del self._Rates
		self._Rates = base_types.UninitialisedField(self, 'Rates', Rates3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LndgFee', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rates', type=Rates3, min=0, max=1, mutex_group=None, array=False),
	))