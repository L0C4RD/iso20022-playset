# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDeviceControl3
from . import ContentInformationType10
from . import ContentInformationType13
from . import Header31

class ATMDeviceControlV04(base_types._BaseFieldType):

	__slots__ = ["_ATMDvcCtrl", "_Hdr", "_PrtctdATMDvcCtrl", "_SctyTrlr"]
	@property
	def ATMDvcCtrl(self):
		return self._ATMDvcCtrl

	@ATMDvcCtrl.setter
	def ATMDvcCtrl(self, value):
		self._ATMDvcCtrl = value if value is not None else base_types.UninitialisedField(self, 'ATMDvcCtrl', ATMDeviceControl3, False)

	@ATMDvcCtrl.deleter
	def ATMDvcCtrl(self):
		del self._ATMDvcCtrl
		self._ATMDvcCtrl = base_types.UninitialisedField(self, 'ATMDvcCtrl', ATMDeviceControl3, False)

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
	def PrtctdATMDvcCtrl(self):
		return self._PrtctdATMDvcCtrl

	@PrtctdATMDvcCtrl.setter
	def PrtctdATMDvcCtrl(self, value):
		self._PrtctdATMDvcCtrl = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMDvcCtrl', ContentInformationType10, False)

	@PrtctdATMDvcCtrl.deleter
	def PrtctdATMDvcCtrl(self):
		del self._PrtctdATMDvcCtrl
		self._PrtctdATMDvcCtrl = base_types.UninitialisedField(self, 'PrtctdATMDvcCtrl', ContentInformationType10, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType13, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType13, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMDvcCtrl', type=ATMDeviceControl3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDvcCtrl', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType13, min=0, max=1, mutex_group=None, array=False),
	))