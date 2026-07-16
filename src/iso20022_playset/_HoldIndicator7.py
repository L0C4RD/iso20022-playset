# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RegistrationReason6
from . import YesNoIndicator

class HoldIndicator7(base_types._BaseFieldType):

	__slots__ = ["_Ind", "_Rsn"]
	@property
	def Ind(self):
		return self._Ind

	@Ind.setter
	def Ind(self, value):
		self._Ind = value if value is not None else base_types.UninitialisedField(self, 'Ind', YesNoIndicator, False)

	@Ind.deleter
	def Ind(self):
		del self._Ind
		self._Ind = base_types.UninitialisedField(self, 'Ind', YesNoIndicator, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', RegistrationReason6, True)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', RegistrationReason6, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ind', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=RegistrationReason6, min=0, max=None, mutex_group=None, array=True),
	))