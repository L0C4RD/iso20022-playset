# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InterestComputationMethod4Code
from . import Max1000Text

class InterestComputationMethodFormat7(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Nrrtv"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', InterestComputationMethod4Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', InterestComputationMethod4Code, False)

	@property
	def Nrrtv(self):
		return self._Nrrtv

	@Nrrtv.setter
	def Nrrtv(self, value):
		self._Nrrtv = value if value is not None else base_types.UninitialisedField(self, 'Nrrtv', Max1000Text, False)

	@Nrrtv.deleter
	def Nrrtv(self):
		del self._Nrrtv
		self._Nrrtv = base_types.UninitialisedField(self, 'Nrrtv', Max1000Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=InterestComputationMethod4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nrrtv', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
	))