from . import base_types
from ._SafekeepingAccountIdentification1Code import SafekeepingAccountIdentification1Code

class AccountIdentification10(base_types._BaseFieldType):

	__slots__ = ["_IdCd"]
	@property
	def IdCd(self):
		return self._IdCd

	@IdCd.setter
	def IdCd(self, value):
		self._IdCd = value if type(value) != base_types.auto else self.make_default("IdCd")

	@IdCd.deleter
	def IdCd(self):
		del self._IdCd
		self._IdCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdCd', type=SafekeepingAccountIdentification1Code, min=1, max=1, mutex_group=None, array=False),
	))

