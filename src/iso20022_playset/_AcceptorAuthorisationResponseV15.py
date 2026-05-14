from . import base_types
from ._AcceptorAuthorisationResponse15 import AcceptorAuthorisationResponse15
from ._ContentInformationType37 import ContentInformationType37
from ._Header70 import Header70

class AcceptorAuthorisationResponseV15(base_types._BaseFieldType):

	__slots__ = ["_AuthstnRspn", "_Hdr", "_SctyTrlr"]
	@property
	def AuthstnRspn(self):
		return self._AuthstnRspn

	@AuthstnRspn.setter
	def AuthstnRspn(self, value):
		self._AuthstnRspn = value if type(value) != base_types.auto else self.make_default("AuthstnRspn")

	@AuthstnRspn.deleter
	def AuthstnRspn(self):
		del self._AuthstnRspn
		self._AuthstnRspn = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthstnRspn', type=AcceptorAuthorisationResponse15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))

