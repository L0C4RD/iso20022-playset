# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification47
from . import RestrictedFINXMax210Text

class ProprietaryReason5(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_Rsn"]
	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRsnInf', RestrictedFINXMax210Text, False)

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = base_types.UninitialisedField(self, 'AddtlRsnInf', RestrictedFINXMax210Text, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', GenericIdentification47, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', GenericIdentification47, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=RestrictedFINXMax210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
	))