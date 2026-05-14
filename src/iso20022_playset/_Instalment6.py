# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Number import Number
from ._Plan3 import Plan3

class Instalment6(base_types._BaseFieldType):

	__slots__ = ["_Plan", "_PmtSeqNb"]
	@property
	def Plan(self):
		return self._Plan

	@Plan.setter
	def Plan(self, value):
		self._Plan = value if type(value) != base_types.auto else self.make_default("Plan")

	@Plan.deleter
	def Plan(self):
		del self._Plan
		self._Plan = None

	@property
	def PmtSeqNb(self):
		return self._PmtSeqNb

	@PmtSeqNb.setter
	def PmtSeqNb(self, value):
		self._PmtSeqNb = value if type(value) != base_types.auto else self.make_default("PmtSeqNb")

	@PmtSeqNb.deleter
	def PmtSeqNb(self):
		del self._PmtSeqNb
		self._PmtSeqNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Plan', type=Plan3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
	))