# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LimitCriteria7Choice import LimitCriteria7Choice
from ._QueryType2Code import QueryType2Code

class LimitQuery5(base_types._BaseFieldType):

	__slots__ = ["_LmtCrit", "_QryTp"]
	@property
	def LmtCrit(self):
		return self._LmtCrit

	@LmtCrit.setter
	def LmtCrit(self, value):
		self._LmtCrit = value if type(value) != base_types.auto else self.make_default("LmtCrit")

	@LmtCrit.deleter
	def LmtCrit(self):
		del self._LmtCrit
		self._LmtCrit = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LmtCrit', type=LimitCriteria7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))