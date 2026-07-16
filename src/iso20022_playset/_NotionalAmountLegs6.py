# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotionalAmount7

class NotionalAmountLegs6(base_types._BaseFieldType):

	__slots__ = ["_FrstLeg", "_ScndLeg"]
	@property
	def FrstLeg(self):
		return self._FrstLeg

	@FrstLeg.setter
	def FrstLeg(self, value):
		self._FrstLeg = value if value is not None else base_types.UninitialisedField(self, 'FrstLeg', NotionalAmount7, False)

	@FrstLeg.deleter
	def FrstLeg(self):
		del self._FrstLeg
		self._FrstLeg = base_types.UninitialisedField(self, 'FrstLeg', NotionalAmount7, False)

	@property
	def ScndLeg(self):
		return self._ScndLeg

	@ScndLeg.setter
	def ScndLeg(self, value):
		self._ScndLeg = value if value is not None else base_types.UninitialisedField(self, 'ScndLeg', NotionalAmount7, False)

	@ScndLeg.deleter
	def ScndLeg(self):
		del self._ScndLeg
		self._ScndLeg = base_types.UninitialisedField(self, 'ScndLeg', NotionalAmount7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstLeg', type=NotionalAmount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLeg', type=NotionalAmount7, min=0, max=1, mutex_group=None, array=False),
	))