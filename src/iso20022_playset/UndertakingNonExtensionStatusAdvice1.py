import base_types
import PartyIdentification43
import Undertaking7

class UndertakingNonExtensionStatusAdvice1(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgId", "_NtifngPty"]
	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

	@property
	def NtifngPty(self):
		return self._NtifngPty

	@NtifngPty.setter
	def NtifngPty(self, value):
		self._NtifngPty = value if type(value) != auto else self.make_default("NtifngPty")

	@NtifngPty.deleter
	def NtifngPty(self):
		del self._NtifngPty
		self._NtifngPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtifngPty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
	))

