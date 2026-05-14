# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._QueryType2Code import QueryType2Code
from ._ReservationCriteria6Choice import ReservationCriteria6Choice

class ReservationQuery6(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_RsvatnCrit"]
	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != base_types.auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	@property
	def RsvatnCrit(self):
		return self._RsvatnCrit

	@RsvatnCrit.setter
	def RsvatnCrit(self, value):
		self._RsvatnCrit = value if type(value) != base_types.auto else self.make_default("RsvatnCrit")

	@RsvatnCrit.deleter
	def RsvatnCrit(self):
		del self._RsvatnCrit
		self._RsvatnCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnCrit', type=ReservationCriteria6Choice, min=0, max=1, mutex_group=None, array=False),
	))