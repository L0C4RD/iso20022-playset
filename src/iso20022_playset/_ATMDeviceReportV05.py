# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDeviceReport5
from . import ContentInformationType10
from . import ContentInformationType13
from . import Header31

class ATMDeviceReportV05(base_types._BaseFieldType):

	__slots__ = ["_ATMDvcRpt", "_Hdr", "_PrtctdATMDvcRpt", "_SctyTrlr"]
	@property
	def ATMDvcRpt(self):
		return self._ATMDvcRpt

	@ATMDvcRpt.setter
	def ATMDvcRpt(self, value):
		self._ATMDvcRpt = value if value is not None else base_types.UninitialisedField(self, 'ATMDvcRpt', ATMDeviceReport5, False)

	@ATMDvcRpt.deleter
	def ATMDvcRpt(self):
		del self._ATMDvcRpt
		self._ATMDvcRpt = base_types.UninitialisedField(self, 'ATMDvcRpt', ATMDeviceReport5, False)

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
	def PrtctdATMDvcRpt(self):
		return self._PrtctdATMDvcRpt

	@PrtctdATMDvcRpt.setter
	def PrtctdATMDvcRpt(self, value):
		self._PrtctdATMDvcRpt = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMDvcRpt', ContentInformationType10, False)

	@PrtctdATMDvcRpt.deleter
	def PrtctdATMDvcRpt(self):
		del self._PrtctdATMDvcRpt
		self._PrtctdATMDvcRpt = base_types.UninitialisedField(self, 'PrtctdATMDvcRpt', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMDvcRpt', type=ATMDeviceReport5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDvcRpt', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType13, min=0, max=1, mutex_group=None, array=False),
	))