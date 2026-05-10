from . import base_types
from ._Max35Text import Max35Text
from ._EventStatus1 import EventStatus1
from ._NotificationType3Code import NotificationType3Code
from ._YesNoIndicator import YesNoIndicator

class NotificationGeneralInformation4(base_types._BaseFieldType):

	__slots__ = ["_ShrhldrRghtsDrctvInd", "_ConfOfHldgReqrd", "_NtfctnSts", "_NtfctnId", "_NtfctnTp"]
	@property
	def ConfOfHldgReqrd(self):
		return self._ConfOfHldgReqrd

	@ConfOfHldgReqrd.setter
	def ConfOfHldgReqrd(self, value):
		self._ConfOfHldgReqrd = value if type(value) != base_types.auto else self.make_default("ConfOfHldgReqrd")

	@ConfOfHldgReqrd.deleter
	def ConfOfHldgReqrd(self):
		del self._ConfOfHldgReqrd
		self._ConfOfHldgReqrd = None

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if type(value) != base_types.auto else self.make_default("NtfctnId")

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = None

	@property
	def NtfctnSts(self):
		return self._NtfctnSts

	@NtfctnSts.setter
	def NtfctnSts(self, value):
		self._NtfctnSts = value if type(value) != base_types.auto else self.make_default("NtfctnSts")

	@NtfctnSts.deleter
	def NtfctnSts(self):
		del self._NtfctnSts
		self._NtfctnSts = None

	@property
	def NtfctnTp(self):
		return self._NtfctnTp

	@NtfctnTp.setter
	def NtfctnTp(self, value):
		self._NtfctnTp = value if type(value) != base_types.auto else self.make_default("NtfctnTp")

	@NtfctnTp.deleter
	def NtfctnTp(self):
		del self._NtfctnTp
		self._NtfctnTp = None

	@property
	def ShrhldrRghtsDrctvInd(self):
		return self._ShrhldrRghtsDrctvInd

	@ShrhldrRghtsDrctvInd.setter
	def ShrhldrRghtsDrctvInd(self, value):
		self._ShrhldrRghtsDrctvInd = value if type(value) != base_types.auto else self.make_default("ShrhldrRghtsDrctvInd")

	@ShrhldrRghtsDrctvInd.deleter
	def ShrhldrRghtsDrctvInd(self):
		del self._ShrhldrRghtsDrctvInd
		self._ShrhldrRghtsDrctvInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfOfHldgReqrd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnSts', type=EventStatus1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnTp', type=NotificationType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrRghtsDrctvInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

