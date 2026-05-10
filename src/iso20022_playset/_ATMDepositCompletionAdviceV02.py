from . import base_types
from ._ATMDepositCompletionAdvice2 import ATMDepositCompletionAdvice2
from ._ContentInformationType10 import ContentInformationType10
from ._ContentInformationType15 import ContentInformationType15
from ._Header32 import Header32

class ATMDepositCompletionAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_ATMDpstCmpltnAdvc", "_Hdr", "_PrtctdATMDpstCmpltnAdvc", "_SctyTrlr"]
	@property
	def ATMDpstCmpltnAdvc(self):
		return self._ATMDpstCmpltnAdvc

	@ATMDpstCmpltnAdvc.setter
	def ATMDpstCmpltnAdvc(self, value):
		self._ATMDpstCmpltnAdvc = value if type(value) != base_types.auto else self.make_default("ATMDpstCmpltnAdvc")

	@ATMDpstCmpltnAdvc.deleter
	def ATMDpstCmpltnAdvc(self):
		del self._ATMDpstCmpltnAdvc
		self._ATMDpstCmpltnAdvc = None

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
	def PrtctdATMDpstCmpltnAdvc(self):
		return self._PrtctdATMDpstCmpltnAdvc

	@PrtctdATMDpstCmpltnAdvc.setter
	def PrtctdATMDpstCmpltnAdvc(self, value):
		self._PrtctdATMDpstCmpltnAdvc = value if type(value) != base_types.auto else self.make_default("PrtctdATMDpstCmpltnAdvc")

	@PrtctdATMDpstCmpltnAdvc.deleter
	def PrtctdATMDpstCmpltnAdvc(self):
		del self._PrtctdATMDpstCmpltnAdvc
		self._PrtctdATMDpstCmpltnAdvc = None

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
		base_types.FieldEntry(name='ATMDpstCmpltnAdvc', type=ATMDepositCompletionAdvice2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDpstCmpltnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))

