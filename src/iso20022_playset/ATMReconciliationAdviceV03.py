from . import base_types
from .ContentInformationType15 import ContentInformationType15
from .Header32 import Header32
from .ContentInformationType10 import ContentInformationType10
from .ATMReconciliationAdvice3 import ATMReconciliationAdvice3

class ATMReconciliationAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_ATMRcncltnAdvc", "_PrtctdATMRcncltnAdvc", "_SctyTrlr", "_Hdr"]
	@property
	def ATMRcncltnAdvc(self):
		return self._ATMRcncltnAdvc

	@ATMRcncltnAdvc.setter
	def ATMRcncltnAdvc(self, value):
		self._ATMRcncltnAdvc = value if type(value) != base_types.auto else self.make_default("ATMRcncltnAdvc")

	@ATMRcncltnAdvc.deleter
	def ATMRcncltnAdvc(self):
		del self._ATMRcncltnAdvc
		self._ATMRcncltnAdvc = None

	@property
	def PrtctdATMRcncltnAdvc(self):
		return self._PrtctdATMRcncltnAdvc

	@PrtctdATMRcncltnAdvc.setter
	def PrtctdATMRcncltnAdvc(self, value):
		self._PrtctdATMRcncltnAdvc = value if type(value) != base_types.auto else self.make_default("PrtctdATMRcncltnAdvc")

	@PrtctdATMRcncltnAdvc.deleter
	def PrtctdATMRcncltnAdvc(self):
		del self._PrtctdATMRcncltnAdvc
		self._PrtctdATMRcncltnAdvc = None

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
		base_types.FieldEntry(name='ATMRcncltnAdvc', type=ATMReconciliationAdvice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMRcncltnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
	))

