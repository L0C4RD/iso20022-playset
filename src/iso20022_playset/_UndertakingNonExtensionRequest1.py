from . import base_types
from ._PartyIdentification43 import PartyIdentification43
from ._Undertaking9 import Undertaking9

class UndertakingNonExtensionRequest1(base_types._BaseFieldType):

	__slots__ = ["_RqstngPty", "_UdrtkgId"]
	@property
	def RqstngPty(self):
		return self._RqstngPty

	@RqstngPty.setter
	def RqstngPty(self, value):
		self._RqstngPty = value if type(value) != base_types.auto else self.make_default("RqstngPty")

	@RqstngPty.deleter
	def RqstngPty(self):
		del self._RqstngPty
		self._RqstngPty = None

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != base_types.auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RqstngPty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
	))

