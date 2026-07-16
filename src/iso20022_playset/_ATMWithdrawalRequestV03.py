# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMWithdrawalRequest3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMWithdrawalRequestV03(base_types._BaseFieldType):

	__slots__ = ["_ATMWdrwlReq", "_Hdr", "_PrtctdATMWdrwlReq", "_SctyTrlr"]
	@property
	def ATMWdrwlReq(self):
		return self._ATMWdrwlReq

	@ATMWdrwlReq.setter
	def ATMWdrwlReq(self, value):
		self._ATMWdrwlReq = value if value is not None else base_types.UninitialisedField(self, 'ATMWdrwlReq', ATMWithdrawalRequest3, False)

	@ATMWdrwlReq.deleter
	def ATMWdrwlReq(self):
		del self._ATMWdrwlReq
		self._ATMWdrwlReq = base_types.UninitialisedField(self, 'ATMWdrwlReq', ATMWithdrawalRequest3, False)

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
	def PrtctdATMWdrwlReq(self):
		return self._PrtctdATMWdrwlReq

	@PrtctdATMWdrwlReq.setter
	def PrtctdATMWdrwlReq(self, value):
		self._PrtctdATMWdrwlReq = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMWdrwlReq', ContentInformationType10, False)

	@PrtctdATMWdrwlReq.deleter
	def PrtctdATMWdrwlReq(self):
		del self._PrtctdATMWdrwlReq
		self._PrtctdATMWdrwlReq = base_types.UninitialisedField(self, 'PrtctdATMWdrwlReq', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMWdrwlReq', type=ATMWithdrawalRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMWdrwlReq', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))