from . import base_types
from ._ATMDeviceReport5 import ATMDeviceReport5
from ._ContentInformationType10 import ContentInformationType10
from ._ContentInformationType13 import ContentInformationType13
from ._Header31 import Header31

class ATMDeviceReportV05(base_types._BaseFieldType):

	__slots__ = ["_ATMDvcRpt", "_Hdr", "_PrtctdATMDvcRpt", "_SctyTrlr"]
	@property
	def ATMDvcRpt(self):
		return self._ATMDvcRpt

	@ATMDvcRpt.setter
	def ATMDvcRpt(self, value):
		self._ATMDvcRpt = value if type(value) != base_types.auto else self.make_default("ATMDvcRpt")

	@ATMDvcRpt.deleter
	def ATMDvcRpt(self):
		del self._ATMDvcRpt
		self._ATMDvcRpt = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def PrtctdATMDvcRpt(self):
		return self._PrtctdATMDvcRpt

	@PrtctdATMDvcRpt.setter
	def PrtctdATMDvcRpt(self, value):
		self._PrtctdATMDvcRpt = value if type(value) != base_types.auto else self.make_default("PrtctdATMDvcRpt")

	@PrtctdATMDvcRpt.deleter
	def PrtctdATMDvcRpt(self):
		del self._PrtctdATMDvcRpt
		self._PrtctdATMDvcRpt = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMDvcRpt', type=ATMDeviceReport5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDvcRpt', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType13, min=0, max=1, mutex_group=None, array=False),
	))

