# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMWithdrawalResponse3
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header31

class ATMWithdrawalResponseV03(base_types._BaseFieldType):

	__slots__ = ["_ATMWdrwlRspn", "_Hdr", "_PrtctdATMWdrwlRspn", "_SctyTrlr"]
	@property
	def ATMWdrwlRspn(self):
		return self._ATMWdrwlRspn

	@ATMWdrwlRspn.setter
	def ATMWdrwlRspn(self, value):
		self._ATMWdrwlRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMWdrwlRspn', ATMWithdrawalResponse3, False)

	@ATMWdrwlRspn.deleter
	def ATMWdrwlRspn(self):
		del self._ATMWdrwlRspn
		self._ATMWdrwlRspn = base_types.UninitialisedField(self, 'ATMWdrwlRspn', ATMWithdrawalResponse3, False)

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
	def PrtctdATMWdrwlRspn(self):
		return self._PrtctdATMWdrwlRspn

	@PrtctdATMWdrwlRspn.setter
	def PrtctdATMWdrwlRspn(self, value):
		self._PrtctdATMWdrwlRspn = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMWdrwlRspn', ContentInformationType10, False)

	@PrtctdATMWdrwlRspn.deleter
	def PrtctdATMWdrwlRspn(self):
		del self._PrtctdATMWdrwlRspn
		self._PrtctdATMWdrwlRspn = base_types.UninitialisedField(self, 'PrtctdATMWdrwlRspn', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMWdrwlRspn', type=ATMWithdrawalResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMWdrwlRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))