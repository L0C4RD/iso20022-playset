# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InstalmentPlan1
from . import Number

class Instalment8(base_types._BaseFieldType):

	__slots__ = ["_Plan", "_PmtSeqNb"]
	@property
	def Plan(self):
		return self._Plan

	@Plan.setter
	def Plan(self, value):
		self._Plan = value if value is not None else base_types.UninitialisedField(self, 'Plan', InstalmentPlan1, True)

	@Plan.deleter
	def Plan(self):
		del self._Plan
		self._Plan = base_types.UninitialisedField(self, 'Plan', InstalmentPlan1, True)

	@property
	def PmtSeqNb(self):
		return self._PmtSeqNb

	@PmtSeqNb.setter
	def PmtSeqNb(self, value):
		self._PmtSeqNb = value if value is not None else base_types.UninitialisedField(self, 'PmtSeqNb', Number, False)

	@PmtSeqNb.deleter
	def PmtSeqNb(self):
		del self._PmtSeqNb
		self._PmtSeqNb = base_types.UninitialisedField(self, 'PmtSeqNb', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Plan', type=InstalmentPlan1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
	))