from . import base_types
from .ContentInformationType38 import ContentInformationType38
from .AcceptorToAcquirerFileBody2 import AcceptorToAcquirerFileBody2
from .Header56 import Header56

class AcceptorToAcquirerBatchFileExchangeV02(base_types._BaseFieldType):

	__slots__ = ["_BodyElmt", "_SctyTrlr", "_Hdr"]
	@property
	def BodyElmt(self):
		return self._BodyElmt

	@BodyElmt.setter
	def BodyElmt(self, value):
		self._BodyElmt = value if type(value) != base_types.auto else self.make_default("BodyElmt")

	@BodyElmt.deleter
	def BodyElmt(self):
		del self._BodyElmt
		self._BodyElmt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BodyElmt', type=AcceptorToAcquirerFileBody2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header56, min=1, max=1, mutex_group=None, array=False),
	))

