# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ReservationCriteria7

class ReservationCriteria6Choice(base_types._BaseFieldType):

	__slots__ = ["_NewCrit", "_QryNm"]
	@property
	def NewCrit(self):
		return self._NewCrit

	@NewCrit.setter
	def NewCrit(self, value):
		self._NewCrit = value if value is not None else base_types.UninitialisedField(self, 'NewCrit', ReservationCriteria7, False)

	@NewCrit.deleter
	def NewCrit(self):
		del self._NewCrit
		self._NewCrit = base_types.UninitialisedField(self, 'NewCrit', ReservationCriteria7, False)

	@property
	def QryNm(self):
		return self._QryNm

	@QryNm.setter
	def QryNm(self, value):
		self._QryNm = value if value is not None else base_types.UninitialisedField(self, 'QryNm', Max35Text, False)

	@QryNm.deleter
	def QryNm(self):
		del self._QryNm
		self._QryNm = base_types.UninitialisedField(self, 'QryNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewCrit', type=ReservationCriteria7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QryNm', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))