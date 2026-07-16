# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Frequency11Code
from . import InterestRateContractTerm1
from . import Standardisation1Code

class FinancialInstrumentAttributes88(base_types._BaseFieldType):

	__slots__ = ["_CtrctTerm", "_PmtFrqcy", "_Stdstn"]
	@property
	def CtrctTerm(self):
		return self._CtrctTerm

	@CtrctTerm.setter
	def CtrctTerm(self, value):
		self._CtrctTerm = value if value is not None else base_types.UninitialisedField(self, 'CtrctTerm', InterestRateContractTerm1, False)

	@CtrctTerm.deleter
	def CtrctTerm(self):
		del self._CtrctTerm
		self._CtrctTerm = base_types.UninitialisedField(self, 'CtrctTerm', InterestRateContractTerm1, False)

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PmtFrqcy', Frequency11Code, False)

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = base_types.UninitialisedField(self, 'PmtFrqcy', Frequency11Code, False)

	@property
	def Stdstn(self):
		return self._Stdstn

	@Stdstn.setter
	def Stdstn(self, value):
		self._Stdstn = value if value is not None else base_types.UninitialisedField(self, 'Stdstn', Standardisation1Code, True)

	@Stdstn.deleter
	def Stdstn(self):
		del self._Stdstn
		self._Stdstn = base_types.UninitialisedField(self, 'Stdstn', Standardisation1Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctTerm', type=InterestRateContractTerm1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency11Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stdstn', type=Standardisation1Code, min=0, max=3, mutex_group=None, array=True),
	))