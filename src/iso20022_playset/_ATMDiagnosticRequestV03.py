# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDiagnosticRequest3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMDiagnosticRequestV03(base_types._BaseFieldType):

	__slots__ = ["_ATMDgnstcReq", "_Hdr", "_PrtctdATMDgnstcReq", "_SctyTrlr"]
	@property
	def ATMDgnstcReq(self):
		return self._ATMDgnstcReq

	@ATMDgnstcReq.setter
	def ATMDgnstcReq(self, value):
		self._ATMDgnstcReq = value if value is not None else base_types.UninitialisedField(self, 'ATMDgnstcReq', ATMDiagnosticRequest3, False)

	@ATMDgnstcReq.deleter
	def ATMDgnstcReq(self):
		del self._ATMDgnstcReq
		self._ATMDgnstcReq = base_types.UninitialisedField(self, 'ATMDgnstcReq', ATMDiagnosticRequest3, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header31, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header31, False)

	@property
	def PrtctdATMDgnstcReq(self):
		return self._PrtctdATMDgnstcReq

	@PrtctdATMDgnstcReq.setter
	def PrtctdATMDgnstcReq(self, value):
		self._PrtctdATMDgnstcReq = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMDgnstcReq', ContentInformationType10, False)

	@PrtctdATMDgnstcReq.deleter
	def PrtctdATMDgnstcReq(self):
		del self._PrtctdATMDgnstcReq
		self._PrtctdATMDgnstcReq = base_types.UninitialisedField(self, 'PrtctdATMDgnstcReq', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMDgnstcReq', type=ATMDiagnosticRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDgnstcReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))