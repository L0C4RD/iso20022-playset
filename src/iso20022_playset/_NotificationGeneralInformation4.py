# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EventStatus1
from . import Max35Text
from . import NotificationType3Code
from . import YesNoIndicator

class NotificationGeneralInformation4(base_types._BaseFieldType):

	__slots__ = ["_ConfOfHldgReqrd", "_NtfctnId", "_NtfctnSts", "_NtfctnTp", "_ShrhldrRghtsDrctvInd"]
	@property
	def ConfOfHldgReqrd(self):
		return self._ConfOfHldgReqrd

	@ConfOfHldgReqrd.setter
	def ConfOfHldgReqrd(self, value):
		self._ConfOfHldgReqrd = value if value is not None else base_types.UninitialisedField(self, 'ConfOfHldgReqrd', YesNoIndicator, False)

	@ConfOfHldgReqrd.deleter
	def ConfOfHldgReqrd(self):
		del self._ConfOfHldgReqrd
		self._ConfOfHldgReqrd = base_types.UninitialisedField(self, 'ConfOfHldgReqrd', YesNoIndicator, False)

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if value is not None else base_types.UninitialisedField(self, 'NtfctnId', Max35Text, False)

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = base_types.UninitialisedField(self, 'NtfctnId', Max35Text, False)

	@property
	def NtfctnSts(self):
		return self._NtfctnSts

	@NtfctnSts.setter
	def NtfctnSts(self, value):
		self._NtfctnSts = value if value is not None else base_types.UninitialisedField(self, 'NtfctnSts', EventStatus1, False)

	@NtfctnSts.deleter
	def NtfctnSts(self):
		del self._NtfctnSts
		self._NtfctnSts = base_types.UninitialisedField(self, 'NtfctnSts', EventStatus1, False)

	@property
	def NtfctnTp(self):
		return self._NtfctnTp

	@NtfctnTp.setter
	def NtfctnTp(self, value):
		self._NtfctnTp = value if value is not None else base_types.UninitialisedField(self, 'NtfctnTp', NotificationType3Code, False)

	@NtfctnTp.deleter
	def NtfctnTp(self):
		del self._NtfctnTp
		self._NtfctnTp = base_types.UninitialisedField(self, 'NtfctnTp', NotificationType3Code, False)

	@property
	def ShrhldrRghtsDrctvInd(self):
		return self._ShrhldrRghtsDrctvInd

	@ShrhldrRghtsDrctvInd.setter
	def ShrhldrRghtsDrctvInd(self, value):
		self._ShrhldrRghtsDrctvInd = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrRghtsDrctvInd', YesNoIndicator, False)

	@ShrhldrRghtsDrctvInd.deleter
	def ShrhldrRghtsDrctvInd(self):
		del self._ShrhldrRghtsDrctvInd
		self._ShrhldrRghtsDrctvInd = base_types.UninitialisedField(self, 'ShrhldrRghtsDrctvInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfOfHldgReqrd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnSts', type=EventStatus1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnTp', type=NotificationType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrRghtsDrctvInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))