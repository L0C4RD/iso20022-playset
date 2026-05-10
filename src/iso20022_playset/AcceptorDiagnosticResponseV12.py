from . import base_types
from .AcceptorDiagnosticResponse11 import AcceptorDiagnosticResponse11
from .Header70 import Header70
from .ContentInformationType37 import ContentInformationType37

class AcceptorDiagnosticResponseV12(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_DgnstcRspn", "_Hdr"]
	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def DgnstcRspn(self):
		return self._DgnstcRspn

	@DgnstcRspn.setter
	def DgnstcRspn(self, value):
		self._DgnstcRspn = value if type(value) != auto else self.make_default("DgnstcRspn")

	@DgnstcRspn.deleter
	def DgnstcRspn(self):
		del self._DgnstcRspn
		self._DgnstcRspn = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgnstcRspn', type=AcceptorDiagnosticResponse11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
	))

