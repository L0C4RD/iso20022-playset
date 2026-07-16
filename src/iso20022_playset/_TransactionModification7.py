# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaymentIdentification8Choice
from . import PaymentInstruction33

class TransactionModification7(base_types._BaseFieldType):

	__slots__ = ["_NewPmtValSet", "_PmtId"]
	@property
	def NewPmtValSet(self):
		return self._NewPmtValSet

	@NewPmtValSet.setter
	def NewPmtValSet(self, value):
		self._NewPmtValSet = value if value is not None else base_types.UninitialisedField(self, 'NewPmtValSet', PaymentInstruction33, False)

	@NewPmtValSet.deleter
	def NewPmtValSet(self):
		del self._NewPmtValSet
		self._NewPmtValSet = base_types.UninitialisedField(self, 'NewPmtValSet', PaymentInstruction33, False)

	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if value is not None else base_types.UninitialisedField(self, 'PmtId', PaymentIdentification8Choice, False)

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = base_types.UninitialisedField(self, 'PmtId', PaymentIdentification8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewPmtValSet', type=PaymentInstruction33, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification8Choice, min=1, max=1, mutex_group=None, array=False),
	))