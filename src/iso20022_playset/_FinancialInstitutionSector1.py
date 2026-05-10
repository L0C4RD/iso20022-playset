from . import base_types
from ._FinancialPartyClassification2Choice import FinancialPartyClassification2Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class FinancialInstitutionSector1(base_types._BaseFieldType):

	__slots__ = ["_ClrThrshld", "_Sctr"]
	@property
	def ClrThrshld(self):
		return self._ClrThrshld

	@ClrThrshld.setter
	def ClrThrshld(self, value):
		self._ClrThrshld = value if type(value) != base_types.auto else self.make_default("ClrThrshld")

	@ClrThrshld.deleter
	def ClrThrshld(self):
		del self._ClrThrshld
		self._ClrThrshld = None

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != base_types.auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrThrshld', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=FinancialPartyClassification2Choice, min=1, max=None, mutex_group=None, array=True),
	))

