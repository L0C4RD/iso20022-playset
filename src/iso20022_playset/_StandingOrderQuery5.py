# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import QueryType2Code
from . import StandingOrderCriteria5Choice

class StandingOrderQuery5(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_StgOrdrCrit"]
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
	def StgOrdrCrit(self):
		return self._StgOrdrCrit

	@StgOrdrCrit.setter
	def StgOrdrCrit(self, value):
		self._StgOrdrCrit = value if value is not None else base_types.UninitialisedField(self, 'StgOrdrCrit', StandingOrderCriteria5Choice, False)

	@StgOrdrCrit.deleter
	def StgOrdrCrit(self):
		del self._StgOrdrCrit
		self._StgOrdrCrit = base_types.UninitialisedField(self, 'StgOrdrCrit', StandingOrderCriteria5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrCrit', type=StandingOrderCriteria5Choice, min=0, max=1, mutex_group=None, array=False),
	))