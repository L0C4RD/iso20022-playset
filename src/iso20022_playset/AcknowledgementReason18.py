from . import base_types
import RestrictedFINXMax210Text
import AcknowledgementReason21Choice

class AcknowledgementReason18(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_Cd"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=RestrictedFINXMax210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=AcknowledgementReason21Choice, min=1, max=1, mutex_group=None, array=False),
	))

