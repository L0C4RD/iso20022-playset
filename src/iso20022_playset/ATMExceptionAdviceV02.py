from . import base_types
from .ATMExceptionAdvice2 import ATMExceptionAdvice2
from .ContentInformationType15 import ContentInformationType15
from .ContentInformationType10 import ContentInformationType10
from .Header32 import Header32

class ATMExceptionAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_ATMXcptnAdvc", "_PrtctdATMXcptnAdvc", "_SctyTrlr", "_Hdr"]
	@property
	def ATMXcptnAdvc(self):
		return self._ATMXcptnAdvc

	@ATMXcptnAdvc.setter
	def ATMXcptnAdvc(self, value):
		self._ATMXcptnAdvc = value if type(value) != base_types.auto else self.make_default("ATMXcptnAdvc")

	@ATMXcptnAdvc.deleter
	def ATMXcptnAdvc(self):
		del self._ATMXcptnAdvc
		self._ATMXcptnAdvc = None

	@property
	def PrtctdATMXcptnAdvc(self):
		return self._PrtctdATMXcptnAdvc

	@PrtctdATMXcptnAdvc.setter
	def PrtctdATMXcptnAdvc(self, value):
		self._PrtctdATMXcptnAdvc = value if type(value) != base_types.auto else self.make_default("PrtctdATMXcptnAdvc")

	@PrtctdATMXcptnAdvc.deleter
	def PrtctdATMXcptnAdvc(self):
		del self._PrtctdATMXcptnAdvc
		self._PrtctdATMXcptnAdvc = None

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
		base_types.FieldEntry(name='ATMXcptnAdvc', type=ATMExceptionAdvice2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMXcptnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
	))

