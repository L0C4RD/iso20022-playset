# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Number
from . import VoteInstructionType1Choice

class VoteTypeAndQuantity1(base_types._BaseFieldType):

	__slots__ = ["_VoteInstrTp", "_VoteQty"]
	@property
	def VoteInstrTp(self):
		return self._VoteInstrTp

	@VoteInstrTp.setter
	def VoteInstrTp(self, value):
		self._VoteInstrTp = value if value is not None else base_types.UninitialisedField(self, 'VoteInstrTp', VoteInstructionType1Choice, False)

	@VoteInstrTp.deleter
	def VoteInstrTp(self):
		del self._VoteInstrTp
		self._VoteInstrTp = base_types.UninitialisedField(self, 'VoteInstrTp', VoteInstructionType1Choice, False)

	@property
	def VoteQty(self):
		return self._VoteQty

	@VoteQty.setter
	def VoteQty(self, value):
		self._VoteQty = value if value is not None else base_types.UninitialisedField(self, 'VoteQty', Number, False)

	@VoteQty.deleter
	def VoteQty(self):
		del self._VoteQty
		self._VoteQty = base_types.UninitialisedField(self, 'VoteQty', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteInstrTp', type=VoteInstructionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteQty', type=Number, min=1, max=1, mutex_group=None, array=False),
	))