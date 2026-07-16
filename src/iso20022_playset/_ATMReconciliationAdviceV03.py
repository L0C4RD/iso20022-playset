# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMReconciliationAdvice3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMReconciliationAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_ATMRcncltnAdvc", "_Hdr", "_PrtctdATMRcncltnAdvc", "_SctyTrlr"]
	@property
	def ATMRcncltnAdvc(self):
		return self._ATMRcncltnAdvc

	@ATMRcncltnAdvc.setter
	def ATMRcncltnAdvc(self, value):
		self._ATMRcncltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMRcncltnAdvc', ATMReconciliationAdvice3, False)

	@ATMRcncltnAdvc.deleter
	def ATMRcncltnAdvc(self):
		del self._ATMRcncltnAdvc
		self._ATMRcncltnAdvc = base_types.UninitialisedField(self, 'ATMRcncltnAdvc', ATMReconciliationAdvice3, False)

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
	def PrtctdATMRcncltnAdvc(self):
		return self._PrtctdATMRcncltnAdvc

	@PrtctdATMRcncltnAdvc.setter
	def PrtctdATMRcncltnAdvc(self, value):
		self._PrtctdATMRcncltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMRcncltnAdvc', ContentInformationType10, False)

	@PrtctdATMRcncltnAdvc.deleter
	def PrtctdATMRcncltnAdvc(self):
		del self._PrtctdATMRcncltnAdvc
		self._PrtctdATMRcncltnAdvc = base_types.UninitialisedField(self, 'PrtctdATMRcncltnAdvc', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMRcncltnAdvc', type=ATMReconciliationAdvice3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMRcncltnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))