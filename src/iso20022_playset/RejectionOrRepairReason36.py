from . import base_types
from .RejectionAndRepairReason36Choice import RejectionAndRepairReason36Choice
from .Max210Text import Max210Text

class RejectionOrRepairReason36(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_AddtlRsnInf"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if type(value) != auto else self.make_default("AddtlRsnInf")

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=RejectionAndRepairReason36Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlRsnInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
	))

