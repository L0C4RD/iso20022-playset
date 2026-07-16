# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PercentageRate

class OwnershipBeneficiaryRate1(base_types._BaseFieldType):

	__slots__ = ["_Frctn", "_Rate"]
	@property
	def Frctn(self):
		return self._Frctn

	@Frctn.setter
	def Frctn(self, value):
		self._Frctn = value if value is not None else base_types.UninitialisedField(self, 'Frctn', Max35Text, False)

	@Frctn.deleter
	def Frctn(self):
		del self._Frctn
		self._Frctn = base_types.UninitialisedField(self, 'Frctn', Max35Text, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))