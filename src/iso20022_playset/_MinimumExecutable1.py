from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .FinancialInstrumentQuantity25Choice import FinancialInstrumentQuantity25Choice

class MinimumExecutable1(base_types._BaseFieldType):

	__slots__ = ["_Sz", "_FrstExctnOnly"]
	@property
	def Sz(self):
		return self._Sz

	@Sz.setter
	def Sz(self, value):
		self._Sz = value if type(value) != base_types.auto else self.make_default("Sz")

	@Sz.deleter
	def Sz(self):
		del self._Sz
		self._Sz = None

	@property
	def FrstExctnOnly(self):
		return self._FrstExctnOnly

	@FrstExctnOnly.setter
	def FrstExctnOnly(self, value):
		self._FrstExctnOnly = value if type(value) != base_types.auto else self.make_default("FrstExctnOnly")

	@FrstExctnOnly.deleter
	def FrstExctnOnly(self):
		del self._FrstExctnOnly
		self._FrstExctnOnly = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sz', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstExctnOnly', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

