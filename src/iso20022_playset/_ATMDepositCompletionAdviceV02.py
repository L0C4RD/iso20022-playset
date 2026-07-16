# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDepositCompletionAdvice2
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMDepositCompletionAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_ATMDpstCmpltnAdvc", "_Hdr", "_PrtctdATMDpstCmpltnAdvc", "_SctyTrlr"]
	@property
	def ATMDpstCmpltnAdvc(self):
		return self._ATMDpstCmpltnAdvc

	@ATMDpstCmpltnAdvc.setter
	def ATMDpstCmpltnAdvc(self, value):
		self._ATMDpstCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMDpstCmpltnAdvc', ATMDepositCompletionAdvice2, False)

	@ATMDpstCmpltnAdvc.deleter
	def ATMDpstCmpltnAdvc(self):
		del self._ATMDpstCmpltnAdvc
		self._ATMDpstCmpltnAdvc = base_types.UninitialisedField(self, 'ATMDpstCmpltnAdvc', ATMDepositCompletionAdvice2, False)

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
	def PrtctdATMDpstCmpltnAdvc(self):
		return self._PrtctdATMDpstCmpltnAdvc

	@PrtctdATMDpstCmpltnAdvc.setter
	def PrtctdATMDpstCmpltnAdvc(self, value):
		self._PrtctdATMDpstCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMDpstCmpltnAdvc', ContentInformationType10, False)

	@PrtctdATMDpstCmpltnAdvc.deleter
	def PrtctdATMDpstCmpltnAdvc(self):
		del self._PrtctdATMDpstCmpltnAdvc
		self._PrtctdATMDpstCmpltnAdvc = base_types.UninitialisedField(self, 'PrtctdATMDpstCmpltnAdvc', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMDpstCmpltnAdvc', type=ATMDepositCompletionAdvice2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDpstCmpltnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))