from . import base_types
from ._Frequency11Code import Frequency11Code
from ._Standardisation1Code import Standardisation1Code
from ._InterestRateContractTerm1 import InterestRateContractTerm1

class FinancialInstrumentAttributes88(base_types._BaseFieldType):

	__slots__ = ["_CtrctTerm", "_Stdstn", "_PmtFrqcy"]
	@property
	def CtrctTerm(self):
		return self._CtrctTerm

	@CtrctTerm.setter
	def CtrctTerm(self, value):
		self._CtrctTerm = value if type(value) != base_types.auto else self.make_default("CtrctTerm")

	@CtrctTerm.deleter
	def CtrctTerm(self):
		del self._CtrctTerm
		self._CtrctTerm = None

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != base_types.auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	@property
	def Stdstn(self):
		return self._Stdstn

	@Stdstn.setter
	def Stdstn(self, value):
		self._Stdstn = value if type(value) != base_types.auto else self.make_default("Stdstn")

	@Stdstn.deleter
	def Stdstn(self):
		del self._Stdstn
		self._Stdstn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctTerm', type=InterestRateContractTerm1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency11Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stdstn', type=Standardisation1Code, min=0, max=3, mutex_group=None, array=True),
	))

