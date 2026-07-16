# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BenchmarkCurveName5Choice
from . import InterestRateContractTerm2

class FloatingInterestRate8(base_types._BaseFieldType):

	__slots__ = ["_RefRate", "_Term"]
	@property
	def RefRate(self):
		return self._RefRate

	@RefRate.setter
	def RefRate(self, value):
		self._RefRate = value if value is not None else base_types.UninitialisedField(self, 'RefRate', BenchmarkCurveName5Choice, False)

	@RefRate.deleter
	def RefRate(self):
		del self._RefRate
		self._RefRate = base_types.UninitialisedField(self, 'RefRate', BenchmarkCurveName5Choice, False)

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if value is not None else base_types.UninitialisedField(self, 'Term', InterestRateContractTerm2, False)

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = base_types.UninitialisedField(self, 'Term', InterestRateContractTerm2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefRate', type=BenchmarkCurveName5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=InterestRateContractTerm2, min=0, max=1, mutex_group=None, array=False),
	))