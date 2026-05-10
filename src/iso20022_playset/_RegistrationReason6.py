from . import base_types
from ._RestrictedFINXMax210Text import RestrictedFINXMax210Text
from ._Registration12Choice import Registration12Choice

class RegistrationReason6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Cd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=RestrictedFINXMax210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=Registration12Choice, min=1, max=1, mutex_group=None, array=False),
	))

