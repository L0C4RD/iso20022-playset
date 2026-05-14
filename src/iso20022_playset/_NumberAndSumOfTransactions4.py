# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountAndDirection35 import AmountAndDirection35
from ._DecimalNumber import DecimalNumber
from ._Max15NumericText import Max15NumericText

class NumberAndSumOfTransactions4(base_types._BaseFieldType):

	__slots__ = ["_NbOfNtries", "_Sum", "_TtlNetNtry"]
	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if type(value) != base_types.auto else self.make_default("NbOfNtries")

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = None

	@property
	def Sum(self):
		return self._Sum

	@Sum.setter
	def Sum(self, value):
		self._Sum = value if type(value) != base_types.auto else self.make_default("Sum")

	@Sum.deleter
	def Sum(self):
		del self._Sum
		self._Sum = None

	@property
	def TtlNetNtry(self):
		return self._TtlNetNtry

	@TtlNetNtry.setter
	def TtlNetNtry(self, value):
		self._TtlNetNtry = value if type(value) != base_types.auto else self.make_default("TtlNetNtry")

	@TtlNetNtry.deleter
	def TtlNetNtry(self):
		del self._TtlNetNtry
		self._TtlNetNtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfNtries', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNetNtry', type=AmountAndDirection35, min=0, max=1, mutex_group=None, array=False),
	))