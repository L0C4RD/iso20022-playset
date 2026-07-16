# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text

class InterestPaymentDateRange1(base_types._BaseFieldType):

	__slots__ = ["_DueDt", "_IntrstSchdlId", "_XpctdDt"]
	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if value is not None else base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@property
	def IntrstSchdlId(self):
		return self._IntrstSchdlId

	@IntrstSchdlId.setter
	def IntrstSchdlId(self, value):
		self._IntrstSchdlId = value if value is not None else base_types.UninitialisedField(self, 'IntrstSchdlId', Max35Text, False)

	@IntrstSchdlId.deleter
	def IntrstSchdlId(self):
		del self._IntrstSchdlId
		self._IntrstSchdlId = base_types.UninitialisedField(self, 'IntrstSchdlId', Max35Text, False)

	@property
	def XpctdDt(self):
		return self._XpctdDt

	@XpctdDt.setter
	def XpctdDt(self, value):
		self._XpctdDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdDt', ISODate, False)

	@XpctdDt.deleter
	def XpctdDt(self):
		del self._XpctdDt
		self._XpctdDt = base_types.UninitialisedField(self, 'XpctdDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstSchdlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))