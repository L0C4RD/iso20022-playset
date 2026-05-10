from . import base_types
from ._AccountIdentification1 import AccountIdentification1
from ._AccountIdentification3 import AccountIdentification3
from ._AccountIdentificationAndPurpose import AccountIdentificationAndPurpose

class AccountIdentificationFormatChoice(base_types._BaseFieldType):

	__slots__ = ["_IdAndPurp", "_IdAsDSS", "_SmplId"]
	@property
	def IdAndPurp(self):
		return self._IdAndPurp

	@IdAndPurp.setter
	def IdAndPurp(self, value):
		self._IdAndPurp = value if type(value) != base_types.auto else self.make_default("IdAndPurp")

	@IdAndPurp.deleter
	def IdAndPurp(self):
		del self._IdAndPurp
		self._IdAndPurp = None

	@property
	def IdAsDSS(self):
		return self._IdAsDSS

	@IdAsDSS.setter
	def IdAsDSS(self, value):
		self._IdAsDSS = value if type(value) != base_types.auto else self.make_default("IdAsDSS")

	@IdAsDSS.deleter
	def IdAsDSS(self):
		del self._IdAsDSS
		self._IdAsDSS = None

	@property
	def SmplId(self):
		return self._SmplId

	@SmplId.setter
	def SmplId(self, value):
		self._SmplId = value if type(value) != base_types.auto else self.make_default("SmplId")

	@SmplId.deleter
	def SmplId(self):
		del self._SmplId
		self._SmplId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdAndPurp', type=AccountIdentificationAndPurpose, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IdAsDSS', type=AccountIdentification3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SmplId', type=AccountIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

