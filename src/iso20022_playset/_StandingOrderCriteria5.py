# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import StandingOrderReturnCriteria1
from . import StandingOrderSearchCriteria5

class StandingOrderCriteria5(base_types._BaseFieldType):

	__slots__ = ["_NewQryNm", "_RtrCrit", "_SchCrit"]
	@property
	def NewQryNm(self):
		return self._NewQryNm

	@NewQryNm.setter
	def NewQryNm(self, value):
		self._NewQryNm = value if value is not None else base_types.UninitialisedField(self, 'NewQryNm', Max35Text, False)

	@NewQryNm.deleter
	def NewQryNm(self):
		del self._NewQryNm
		self._NewQryNm = base_types.UninitialisedField(self, 'NewQryNm', Max35Text, False)

	@property
	def RtrCrit(self):
		return self._RtrCrit

	@RtrCrit.setter
	def RtrCrit(self, value):
		self._RtrCrit = value if value is not None else base_types.UninitialisedField(self, 'RtrCrit', StandingOrderReturnCriteria1, False)

	@RtrCrit.deleter
	def RtrCrit(self):
		del self._RtrCrit
		self._RtrCrit = base_types.UninitialisedField(self, 'RtrCrit', StandingOrderReturnCriteria1, False)

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if value is not None else base_types.UninitialisedField(self, 'SchCrit', StandingOrderSearchCriteria5, True)

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = base_types.UninitialisedField(self, 'SchCrit', StandingOrderSearchCriteria5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewQryNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrCrit', type=StandingOrderReturnCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=StandingOrderSearchCriteria5, min=0, max=None, mutex_group=None, array=True),
	))