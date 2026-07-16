# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCompletionAdvice3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMCompletionAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_ATMCmpltnAdvc", "_Hdr", "_PrtctdATMCmpltnAdvc", "_SctyTrlr"]
	@property
	def ATMCmpltnAdvc(self):
		return self._ATMCmpltnAdvc

	@ATMCmpltnAdvc.setter
	def ATMCmpltnAdvc(self, value):
		self._ATMCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMCmpltnAdvc', ATMCompletionAdvice3, False)

	@ATMCmpltnAdvc.deleter
	def ATMCmpltnAdvc(self):
		del self._ATMCmpltnAdvc
		self._ATMCmpltnAdvc = base_types.UninitialisedField(self, 'ATMCmpltnAdvc', ATMCompletionAdvice3, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header32, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header32, False)

	@property
	def PrtctdATMCmpltnAdvc(self):
		return self._PrtctdATMCmpltnAdvc

	@PrtctdATMCmpltnAdvc.setter
	def PrtctdATMCmpltnAdvc(self, value):
		self._PrtctdATMCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMCmpltnAdvc', ContentInformationType10, False)

	@PrtctdATMCmpltnAdvc.deleter
	def PrtctdATMCmpltnAdvc(self):
		del self._PrtctdATMCmpltnAdvc
		self._PrtctdATMCmpltnAdvc = base_types.UninitialisedField(self, 'PrtctdATMCmpltnAdvc', ContentInformationType10, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType15, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType15, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMCmpltnAdvc', type=ATMCompletionAdvice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMCmpltnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))