from . import base_types
from .EncryptionFormat1Code import EncryptionFormat1Code
from .BytePadding1Code import BytePadding1Code
from .Max500Binary import Max500Binary

class Parameter6(base_types._BaseFieldType):

	__slots__ = ["_InitlstnVctr", "_NcrptnFrmt", "_BPddg"]
	@property
	def InitlstnVctr(self):
		return self._InitlstnVctr

	@InitlstnVctr.setter
	def InitlstnVctr(self, value):
		self._InitlstnVctr = value if type(value) != auto else self.make_default("InitlstnVctr")

	@InitlstnVctr.deleter
	def InitlstnVctr(self):
		del self._InitlstnVctr
		self._InitlstnVctr = None

	@property
	def NcrptnFrmt(self):
		return self._NcrptnFrmt

	@NcrptnFrmt.setter
	def NcrptnFrmt(self, value):
		self._NcrptnFrmt = value if type(value) != auto else self.make_default("NcrptnFrmt")

	@NcrptnFrmt.deleter
	def NcrptnFrmt(self):
		del self._NcrptnFrmt
		self._NcrptnFrmt = None

	@property
	def BPddg(self):
		return self._BPddg

	@BPddg.setter
	def BPddg(self, value):
		self._BPddg = value if type(value) != auto else self.make_default("BPddg")

	@BPddg.deleter
	def BPddg(self):
		del self._BPddg
		self._BPddg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlstnVctr', type=Max500Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptnFrmt', type=EncryptionFormat1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BPddg', type=BytePadding1Code, min=0, max=1, mutex_group=None, array=False),
	))

