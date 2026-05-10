from . import base_types
from .RestrictedFINXMax350Text import RestrictedFINXMax350Text

class UpdatedAdditionalInformation23(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=RestrictedFINXMax350Text, min=1, max=None, mutex_group=None, array=True),
	))

