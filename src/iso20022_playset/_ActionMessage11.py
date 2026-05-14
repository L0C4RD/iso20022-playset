# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContentInformationType38 import ContentInformationType38
from ._InformationQualify1Code import InformationQualify1Code
from ._Max20000Text import Max20000Text
from ._Number import Number
from ._OutputBarcode2 import OutputBarcode2
from ._OutputFormat3Code import OutputFormat3Code
from ._TrueFalseIndicator import TrueFalseIndicator
from ._UserInterface4Code import UserInterface4Code

class ActionMessage11(base_types._BaseFieldType):

	__slots__ = ["_Frmt", "_InfQlfr", "_MinDispTm", "_MsgCntt", "_MsgCnttSgntr", "_MsgDstn", "_OutptBrcd", "_RspnReqrdFlg"]
	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

	@property
	def InfQlfr(self):
		return self._InfQlfr

	@InfQlfr.setter
	def InfQlfr(self, value):
		self._InfQlfr = value if type(value) != base_types.auto else self.make_default("InfQlfr")

	@InfQlfr.deleter
	def InfQlfr(self):
		del self._InfQlfr
		self._InfQlfr = None

	@property
	def MinDispTm(self):
		return self._MinDispTm

	@MinDispTm.setter
	def MinDispTm(self, value):
		self._MinDispTm = value if type(value) != base_types.auto else self.make_default("MinDispTm")

	@MinDispTm.deleter
	def MinDispTm(self):
		del self._MinDispTm
		self._MinDispTm = None

	@property
	def MsgCntt(self):
		return self._MsgCntt

	@MsgCntt.setter
	def MsgCntt(self, value):
		self._MsgCntt = value if type(value) != base_types.auto else self.make_default("MsgCntt")

	@MsgCntt.deleter
	def MsgCntt(self):
		del self._MsgCntt
		self._MsgCntt = None

	@property
	def MsgCnttSgntr(self):
		return self._MsgCnttSgntr

	@MsgCnttSgntr.setter
	def MsgCnttSgntr(self, value):
		self._MsgCnttSgntr = value if type(value) != base_types.auto else self.make_default("MsgCnttSgntr")

	@MsgCnttSgntr.deleter
	def MsgCnttSgntr(self):
		del self._MsgCnttSgntr
		self._MsgCnttSgntr = None

	@property
	def MsgDstn(self):
		return self._MsgDstn

	@MsgDstn.setter
	def MsgDstn(self, value):
		self._MsgDstn = value if type(value) != base_types.auto else self.make_default("MsgDstn")

	@MsgDstn.deleter
	def MsgDstn(self):
		del self._MsgDstn
		self._MsgDstn = None

	@property
	def OutptBrcd(self):
		return self._OutptBrcd

	@OutptBrcd.setter
	def OutptBrcd(self, value):
		self._OutptBrcd = value if type(value) != base_types.auto else self.make_default("OutptBrcd")

	@OutptBrcd.deleter
	def OutptBrcd(self):
		del self._OutptBrcd
		self._OutptBrcd = None

	@property
	def RspnReqrdFlg(self):
		return self._RspnReqrdFlg

	@RspnReqrdFlg.setter
	def RspnReqrdFlg(self, value):
		self._RspnReqrdFlg = value if type(value) != base_types.auto else self.make_default("RspnReqrdFlg")

	@RspnReqrdFlg.deleter
	def RspnReqrdFlg(self):
		del self._RspnReqrdFlg
		self._RspnReqrdFlg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frmt', type=OutputFormat3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfQlfr', type=InformationQualify1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinDispTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCntt', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCnttSgntr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgDstn', type=UserInterface4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutptBrcd', type=OutputBarcode2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnReqrdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))