# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Max15NumericText

class NumberAndSumOfTransactions1(base_types._BaseFieldType):

	__slots__ = ["_NbOfNtries", "_Sum"]
	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if value is not None else base_types.UninitialisedField(self, 'NbOfNtries', Max15NumericText, False)

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = base_types.UninitialisedField(self, 'NbOfNtries', Max15NumericText, False)

	@property
	def Sum(self):
		return self._Sum

	@Sum.setter
	def Sum(self, value):
		self._Sum = value if value is not None else base_types.UninitialisedField(self, 'Sum', DecimalNumber, False)

	@Sum.deleter
	def Sum(self):
		del self._Sum
		self._Sum = base_types.UninitialisedField(self, 'Sum', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfNtries', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))