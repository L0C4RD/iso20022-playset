# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BalanceTransferWindow1Code import BalanceTransferWindow1Code
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._ResponseDetails1 import ResponseDetails1
from ._SwitchStatus1Code import SwitchStatus1Code
from ._SwitchType1Code import SwitchType1Code

class AccountSwitchDetails1(base_types._BaseFieldType):

	__slots__ = ["_BalTrfWndw", "_Rspn", "_RtgUnqRefNb", "_SwtchDt", "_SwtchRcvdDtTm", "_SwtchSts", "_SwtchTp", "_UnqRefNb"]
	@property
	def BalTrfWndw(self):
		return self._BalTrfWndw

	@BalTrfWndw.setter
	def BalTrfWndw(self, value):
		self._BalTrfWndw = value if type(value) != base_types.auto else self.make_default("BalTrfWndw")

	@BalTrfWndw.deleter
	def BalTrfWndw(self):
		del self._BalTrfWndw
		self._BalTrfWndw = None

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != base_types.auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def RtgUnqRefNb(self):
		return self._RtgUnqRefNb

	@RtgUnqRefNb.setter
	def RtgUnqRefNb(self, value):
		self._RtgUnqRefNb = value if type(value) != base_types.auto else self.make_default("RtgUnqRefNb")

	@RtgUnqRefNb.deleter
	def RtgUnqRefNb(self):
		del self._RtgUnqRefNb
		self._RtgUnqRefNb = None

	@property
	def SwtchDt(self):
		return self._SwtchDt

	@SwtchDt.setter
	def SwtchDt(self, value):
		self._SwtchDt = value if type(value) != base_types.auto else self.make_default("SwtchDt")

	@SwtchDt.deleter
	def SwtchDt(self):
		del self._SwtchDt
		self._SwtchDt = None

	@property
	def SwtchRcvdDtTm(self):
		return self._SwtchRcvdDtTm

	@SwtchRcvdDtTm.setter
	def SwtchRcvdDtTm(self, value):
		self._SwtchRcvdDtTm = value if type(value) != base_types.auto else self.make_default("SwtchRcvdDtTm")

	@SwtchRcvdDtTm.deleter
	def SwtchRcvdDtTm(self):
		del self._SwtchRcvdDtTm
		self._SwtchRcvdDtTm = None

	@property
	def SwtchSts(self):
		return self._SwtchSts

	@SwtchSts.setter
	def SwtchSts(self, value):
		self._SwtchSts = value if type(value) != base_types.auto else self.make_default("SwtchSts")

	@SwtchSts.deleter
	def SwtchSts(self):
		del self._SwtchSts
		self._SwtchSts = None

	@property
	def SwtchTp(self):
		return self._SwtchTp

	@SwtchTp.setter
	def SwtchTp(self, value):
		self._SwtchTp = value if type(value) != base_types.auto else self.make_default("SwtchTp")

	@SwtchTp.deleter
	def SwtchTp(self):
		del self._SwtchTp
		self._SwtchTp = None

	@property
	def UnqRefNb(self):
		return self._UnqRefNb

	@UnqRefNb.setter
	def UnqRefNb(self, value):
		self._UnqRefNb = value if type(value) != base_types.auto else self.make_default("UnqRefNb")

	@UnqRefNb.deleter
	def UnqRefNb(self):
		del self._UnqRefNb
		self._UnqRefNb = None

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