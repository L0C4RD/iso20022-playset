from . import base_types
from .ContentInformationType10 import ContentInformationType10
from .ATMWithdrawalCompletionAdvice3 import ATMWithdrawalCompletionAdvice3
from .ContentInformationType15 import ContentInformationType15
from .Header32 import Header32

class ATMWithdrawalCompletionAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_ATMWdrwlCmpltnAdvc", "_Hdr", "_PrtctdATMWdrwlCmpltnAdvc"]
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
	def ATMWdrwlCmpltnAdvc(self):
		return self._ATMWdrwlCmpltnAdvc

	@ATMWdrwlCmpltnAdvc.setter
	def ATMWdrwlCmpltnAdvc(self, value):
		self._ATMWdrwlCmpltnAdvc = value if type(value) != base_types.auto else self.make_default("ATMWdrwlCmpltnAdvc")

	@ATMWdrwlCmpltnAdvc.deleter
	def ATMWdrwlCmpltnAdvc(self):
		del self._ATMWdrwlCmpltnAdvc
		self._ATMWdrwlCmpltnAdvc = None

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
	def PrtctdATMWdrwlCmpltnAdvc(self):
		return self._PrtctdATMWdrwlCmpltnAdvc

	@PrtctdATMWdrwlCmpltnAdvc.setter
	def PrtctdATMWdrwlCmpltnAdvc(self, value):
		self._PrtctdATMWdrwlCmpltnAdvc = value if type(value) != base_types.auto else self.make_default("PrtctdATMWdrwlCmpltnAdvc")

	@PrtctdATMWdrwlCmpltnAdvc.deleter
	def PrtctdATMWdrwlCmpltnAdvc(self):
		del self._PrtctdATMWdrwlCmpltnAdvc
		self._PrtctdATMWdrwlCmpltnAdvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMWdrwlCmpltnAdvc', type=ATMWithdrawalCompletionAdvice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMWdrwlCmpltnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
	))

