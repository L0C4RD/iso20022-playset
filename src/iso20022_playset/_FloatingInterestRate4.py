# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BenchmarkCurveName4Choice
from . import InterestRateContractTerm1
from . import Number

class FloatingInterestRate4(base_types._BaseFieldType):

	__slots__ = ["_BsisPtSprd", "_RefRate", "_Term"]
	@property
	def BsisPtSprd(self):
		return self._BsisPtSprd

	@BsisPtSprd.setter
	def BsisPtSprd(self, value):
		self._BsisPtSprd = value if value is not None else base_types.UninitialisedField(self, 'BsisPtSprd', Number, False)

	@BsisPtSprd.deleter
	def BsisPtSprd(self):
		del self._BsisPtSprd
		self._BsisPtSprd = base_types.UninitialisedField(self, 'BsisPtSprd', Number, False)

	@property
	def RefRate(self):
		return self._RefRate

	@RefRate.setter
	def RefRate(self, value):
		self._RefRate = value if value is not None else base_types.UninitialisedField(self, 'RefRate', BenchmarkCurveName4Choice, False)

	@RefRate.deleter
	def RefRate(self):
		del self._RefRate
		self._RefRate = base_types.UninitialisedField(self, 'RefRate', BenchmarkCurveName4Choice, False)

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if value is not None else base_types.UninitialisedField(self, 'Term', InterestRateContractTerm1, False)

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = base_types.UninitialisedField(self, 'Term', InterestRateContractTerm1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisPtSprd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefRate', type=BenchmarkCurveName4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=InterestRateContractTerm1, min=1, max=1, mutex_group=None, array=False),
	))