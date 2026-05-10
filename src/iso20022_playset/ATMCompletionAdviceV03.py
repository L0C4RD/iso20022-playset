import base_types
import ContentInformationType15
import ATMCompletionAdvice3
import ContentInformationType10
import Header32

class ATMCompletionAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_Hdr", "_ATMCmpltnAdvc", "_PrtctdATMCmpltnAdvc"]
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
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def ATMCmpltnAdvc(self):
		return self._ATMCmpltnAdvc

	@ATMCmpltnAdvc.setter
	def ATMCmpltnAdvc(self, value):
		self._ATMCmpltnAdvc = value if type(value) != auto else self.make_default("ATMCmpltnAdvc")

	@ATMCmpltnAdvc.deleter
	def ATMCmpltnAdvc(self):
		del self._ATMCmpltnAdvc
		self._ATMCmpltnAdvc = None

	@property
	def PrtctdATMCmpltnAdvc(self):
		return self._PrtctdATMCmpltnAdvc

	@PrtctdATMCmpltnAdvc.setter
	def PrtctdATMCmpltnAdvc(self, value):
		self._PrtctdATMCmpltnAdvc = value if type(value) != auto else self.make_default("PrtctdATMCmpltnAdvc")

	@PrtctdATMCmpltnAdvc.deleter
	def PrtctdATMCmpltnAdvc(self):
		del self._PrtctdATMCmpltnAdvc
		self._PrtctdATMCmpltnAdvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMCmpltnAdvc', type=ATMCompletionAdvice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMCmpltnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
	))

