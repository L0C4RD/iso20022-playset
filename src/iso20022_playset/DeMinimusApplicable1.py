from . import base_types
from .PercentageRate import PercentageRate
from .YesNoIndicator import YesNoIndicator

class DeMinimusApplicable1(base_types._BaseFieldType):

	__slots__ = ["_Pctg", "_NewIssePrmssn"]
	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if type(value) != base_types.auto else self.make_default("Pctg")

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = None

	@property
	def NewIssePrmssn(self):
		return self._NewIssePrmssn

	@NewIssePrmssn.setter
	def NewIssePrmssn(self, value):
		self._NewIssePrmssn = value if type(value) != base_types.auto else self.make_default("NewIssePrmssn")

	@NewIssePrmssn.deleter
	def NewIssePrmssn(self):
		del self._NewIssePrmssn
		self._NewIssePrmssn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewIssePrmssn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

