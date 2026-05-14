# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Number import Number
from ._VoteInstructionType1Choice import VoteInstructionType1Choice

class VoteTypeAndQuantity1(base_types._BaseFieldType):

	__slots__ = ["_VoteInstrTp", "_VoteQty"]
	@property
	def VoteInstrTp(self):
		return self._VoteInstrTp

	@VoteInstrTp.setter
	def VoteInstrTp(self, value):
		self._VoteInstrTp = value if type(value) != base_types.auto else self.make_default("VoteInstrTp")

	@VoteInstrTp.deleter
	def VoteInstrTp(self):
		del self._VoteInstrTp
		self._VoteInstrTp = None

	@property
	def VoteQty(self):
		return self._VoteQty

	@VoteQty.setter
	def VoteQty(self, value):
		self._VoteQty = value if type(value) != base_types.auto else self.make_default("VoteQty")

	@VoteQty.deleter
	def VoteQty(self):
		del self._VoteQty
		self._VoteQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteInstrTp', type=VoteInstructionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteQty', type=Number, min=1, max=1, mutex_group=None, array=False),
	))