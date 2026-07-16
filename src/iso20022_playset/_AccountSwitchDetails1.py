# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceTransferWindow1Code
from . import ISODate
from . import ISODateTime
from . import Max35Text
from . import ResponseDetails1
from . import SwitchStatus1Code
from . import SwitchType1Code

class AccountSwitchDetails1(base_types._BaseFieldType):

	__slots__ = ["_BalTrfWndw", "_Rspn", "_RtgUnqRefNb", "_SwtchDt", "_SwtchRcvdDtTm", "_SwtchSts", "_SwtchTp", "_UnqRefNb"]
	@property
	def BalTrfWndw(self):
		return self._BalTrfWndw

	@BalTrfWndw.setter
	def BalTrfWndw(self, value):
		self._BalTrfWndw = value if value is not None else base_types.UninitialisedField(self, 'BalTrfWndw', BalanceTransferWindow1Code, False)

	@BalTrfWndw.deleter
	def BalTrfWndw(self):
		del self._BalTrfWndw
		self._BalTrfWndw = base_types.UninitialisedField(self, 'BalTrfWndw', BalanceTransferWindow1Code, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', ResponseDetails1, True)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', ResponseDetails1, True)

	@property
	def RtgUnqRefNb(self):
		return self._RtgUnqRefNb

	@RtgUnqRefNb.setter
	def RtgUnqRefNb(self, value):
		self._RtgUnqRefNb = value if value is not None else base_types.UninitialisedField(self, 'RtgUnqRefNb', Max35Text, False)

	@RtgUnqRefNb.deleter
	def RtgUnqRefNb(self):
		del self._RtgUnqRefNb
		self._RtgUnqRefNb = base_types.UninitialisedField(self, 'RtgUnqRefNb', Max35Text, False)

	@property
	def SwtchDt(self):
		return self._SwtchDt

	@SwtchDt.setter
	def SwtchDt(self, value):
		self._SwtchDt = value if value is not None else base_types.UninitialisedField(self, 'SwtchDt', ISODate, False)

	@SwtchDt.deleter
	def SwtchDt(self):
		del self._SwtchDt
		self._SwtchDt = base_types.UninitialisedField(self, 'SwtchDt', ISODate, False)

	@property
	def SwtchRcvdDtTm(self):
		return self._SwtchRcvdDtTm

	@SwtchRcvdDtTm.setter
	def SwtchRcvdDtTm(self, value):
		self._SwtchRcvdDtTm = value if value is not None else base_types.UninitialisedField(self, 'SwtchRcvdDtTm', ISODateTime, False)

	@SwtchRcvdDtTm.deleter
	def SwtchRcvdDtTm(self):
		del self._SwtchRcvdDtTm
		self._SwtchRcvdDtTm = base_types.UninitialisedField(self, 'SwtchRcvdDtTm', ISODateTime, False)

	@property
	def SwtchSts(self):
		return self._SwtchSts

	@SwtchSts.setter
	def SwtchSts(self, value):
		self._SwtchSts = value if value is not None else base_types.UninitialisedField(self, 'SwtchSts', SwitchStatus1Code, False)

	@SwtchSts.deleter
	def SwtchSts(self):
		del self._SwtchSts
		self._SwtchSts = base_types.UninitialisedField(self, 'SwtchSts', SwitchStatus1Code, False)

	@property
	def SwtchTp(self):
		return self._SwtchTp

	@SwtchTp.setter
	def SwtchTp(self, value):
		self._SwtchTp = value if value is not None else base_types.UninitialisedField(self, 'SwtchTp', SwitchType1Code, False)

	@SwtchTp.deleter
	def SwtchTp(self):
		del self._SwtchTp
		self._SwtchTp = base_types.UninitialisedField(self, 'SwtchTp', SwitchType1Code, False)

	@property
	def UnqRefNb(self):
		return self._UnqRefNb

	@UnqRefNb.setter
	def UnqRefNb(self, value):
		self._UnqRefNb = value if value is not None else base_types.UninitialisedField(self, 'UnqRefNb', Max35Text, False)

	@UnqRefNb.deleter
	def UnqRefNb(self):
		del self._UnqRefNb
		self._UnqRefNb = base_types.UninitialisedField(self, 'UnqRefNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTrfWndw', type=BalanceTransferWindow1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RtgUnqRefNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchRcvdDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchSts', type=SwitchStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchTp', type=SwitchType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqRefNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))