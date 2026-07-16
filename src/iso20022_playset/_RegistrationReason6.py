# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Registration12Choice
from . import RestrictedFINXMax210Text

class RegistrationReason6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Cd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', RestrictedFINXMax210Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', RestrictedFINXMax210Text, False)

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Registration12Choice, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Registration12Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=RestrictedFINXMax210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=Registration12Choice, min=1, max=1, mutex_group=None, array=False),
	))