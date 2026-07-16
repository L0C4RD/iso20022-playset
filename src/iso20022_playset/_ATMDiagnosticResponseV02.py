# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDiagnosticResponse2
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMDiagnosticResponseV02(base_types._BaseFieldType):

	__slots__ = ["_ATMDgnstcRspn", "_Hdr", "_PrtctdATMDgnstcRspn", "_SctyTrlr"]
	@property
	def ATMDgnstcRspn(self):
		return self._ATMDgnstcRspn

	@ATMDgnstcRspn.setter
	def ATMDgnstcRspn(self, value):
		self._ATMDgnstcRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMDgnstcRspn', ATMDiagnosticResponse2, False)

	@ATMDgnstcRspn.deleter
	def ATMDgnstcRspn(self):
		del self._ATMDgnstcRspn
		self._ATMDgnstcRspn = base_types.UninitialisedField(self, 'ATMDgnstcRspn', ATMDiagnosticResponse2, False)

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
	def PrtctdATMDgnstcRspn(self):
		return self._PrtctdATMDgnstcRspn

	@PrtctdATMDgnstcRspn.setter
	def PrtctdATMDgnstcRspn(self, value):
		self._PrtctdATMDgnstcRspn = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMDgnstcRspn', ContentInformationType10, False)

	@PrtctdATMDgnstcRspn.deleter
	def PrtctdATMDgnstcRspn(self):
		del self._PrtctdATMDgnstcRspn
		self._PrtctdATMDgnstcRspn = base_types.UninitialisedField(self, 'PrtctdATMDgnstcRspn', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMDgnstcRspn', type=ATMDiagnosticResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDgnstcRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))