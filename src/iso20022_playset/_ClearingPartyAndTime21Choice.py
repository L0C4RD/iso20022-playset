from . import base_types
from ._NoReasonCode import NoReasonCode
from ._ClearingPartyAndTime22 import ClearingPartyAndTime22

class ClearingPartyAndTime21Choice(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_Dtls"]
	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if type(value) != base_types.auto else self.make_default("Dtls")

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dtls', type=ClearingPartyAndTime22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

