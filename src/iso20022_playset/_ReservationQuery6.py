# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import QueryType2Code
from . import ReservationCriteria6Choice

class ReservationQuery6(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_RsvatnCrit"]
	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if value is not None else base_types.UninitialisedField(self, 'QryTp', QueryType2Code, False)

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = base_types.UninitialisedField(self, 'QryTp', QueryType2Code, False)

	@property
	def RsvatnCrit(self):
		return self._RsvatnCrit

	@RsvatnCrit.setter
	def RsvatnCrit(self, value):
		self._RsvatnCrit = value if value is not None else base_types.UninitialisedField(self, 'RsvatnCrit', ReservationCriteria6Choice, False)

	@RsvatnCrit.deleter
	def RsvatnCrit(self):
		del self._RsvatnCrit
		self._RsvatnCrit = base_types.UninitialisedField(self, 'RsvatnCrit', ReservationCriteria6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnCrit', type=ReservationCriteria6Choice, min=0, max=1, mutex_group=None, array=False),
	))