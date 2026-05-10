from . import base_types
from .NonFinancialInstitutionSector10 import NonFinancialInstitutionSector10
from .FinancialInstitutionSector1 import FinancialInstitutionSector1
from .NoReasonCode import NoReasonCode

class CounterpartyTradeNature15Choice(base_types._BaseFieldType):

	__slots__ = ["_NFI", "_Othr", "_FI", "_CntrlCntrPty"]
	@property
	def NFI(self):
		return self._NFI

	@NFI.setter
	def NFI(self, value):
		self._NFI = value if type(value) != auto else self.make_default("NFI")

	@NFI.deleter
	def NFI(self):
		del self._NFI
		self._NFI = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if type(value) != auto else self.make_default("FI")

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = None

	@property
	def CntrlCntrPty(self):
		return self._CntrlCntrPty

	@CntrlCntrPty.setter
	def CntrlCntrPty(self, value):
		self._CntrlCntrPty = value if type(value) != auto else self.make_default("CntrlCntrPty")

	@CntrlCntrPty.deleter
	def CntrlCntrPty(self):
		del self._CntrlCntrPty
		self._CntrlCntrPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NFI', type=NonFinancialInstitutionSector10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FI', type=FinancialInstitutionSector1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CntrlCntrPty', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

