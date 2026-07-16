# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMWithdrawalCompletionAdvice3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMWithdrawalCompletionAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_ATMWdrwlCmpltnAdvc", "_Hdr", "_PrtctdATMWdrwlCmpltnAdvc", "_SctyTrlr"]
	@property
	def ATMWdrwlCmpltnAdvc(self):
		return self._ATMWdrwlCmpltnAdvc

	@ATMWdrwlCmpltnAdvc.setter
	def ATMWdrwlCmpltnAdvc(self, value):
		self._ATMWdrwlCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMWdrwlCmpltnAdvc', ATMWithdrawalCompletionAdvice3, False)

	@ATMWdrwlCmpltnAdvc.deleter
	def ATMWdrwlCmpltnAdvc(self):
		del self._ATMWdrwlCmpltnAdvc
		self._ATMWdrwlCmpltnAdvc = base_types.UninitialisedField(self, 'ATMWdrwlCmpltnAdvc', ATMWithdrawalCompletionAdvice3, False)

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
	def PrtctdATMWdrwlCmpltnAdvc(self):
		return self._PrtctdATMWdrwlCmpltnAdvc

	@PrtctdATMWdrwlCmpltnAdvc.setter
	def PrtctdATMWdrwlCmpltnAdvc(self, value):
		self._PrtctdATMWdrwlCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMWdrwlCmpltnAdvc', ContentInformationType10, False)

	@PrtctdATMWdrwlCmpltnAdvc.deleter
	def PrtctdATMWdrwlCmpltnAdvc(self):
		del self._PrtctdATMWdrwlCmpltnAdvc
		self._PrtctdATMWdrwlCmpltnAdvc = base_types.UninitialisedField(self, 'PrtctdATMWdrwlCmpltnAdvc', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMWdrwlCmpltnAdvc', type=ATMWithdrawalCompletionAdvice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMWdrwlCmpltnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))