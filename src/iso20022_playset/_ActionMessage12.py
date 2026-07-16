# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType38
from . import InformationQualify1Code
from . import Max20000Text
from . import Number
from . import OutputBarcode2
from . import OutputFormat3Code
from . import TrueFalseIndicator
from . import UserInterface9Code

class ActionMessage12(base_types._BaseFieldType):

	__slots__ = ["_Frmt", "_InfQlfr", "_MinDispTm", "_MsgCntt", "_MsgCnttSgntr", "_MsgDstn", "_OutptBrcd", "_RspnReqrdFlg"]
	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', OutputFormat3Code, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', OutputFormat3Code, False)

	@property
	def InfQlfr(self):
		return self._InfQlfr

	@InfQlfr.setter
	def InfQlfr(self, value):
		self._InfQlfr = value if value is not None else base_types.UninitialisedField(self, 'InfQlfr', InformationQualify1Code, False)

	@InfQlfr.deleter
	def InfQlfr(self):
		del self._InfQlfr
		self._InfQlfr = base_types.UninitialisedField(self, 'InfQlfr', InformationQualify1Code, False)

	@property
	def MinDispTm(self):
		return self._MinDispTm

	@MinDispTm.setter
	def MinDispTm(self, value):
		self._MinDispTm = value if value is not None else base_types.UninitialisedField(self, 'MinDispTm', Number, False)

	@MinDispTm.deleter
	def MinDispTm(self):
		del self._MinDispTm
		self._MinDispTm = base_types.UninitialisedField(self, 'MinDispTm', Number, False)

	@property
	def MsgCntt(self):
		return self._MsgCntt

	@MsgCntt.setter
	def MsgCntt(self, value):
		self._MsgCntt = value if value is not None else base_types.UninitialisedField(self, 'MsgCntt', Max20000Text, False)

	@MsgCntt.deleter
	def MsgCntt(self):
		del self._MsgCntt
		self._MsgCntt = base_types.UninitialisedField(self, 'MsgCntt', Max20000Text, False)

	@property
	def MsgCnttSgntr(self):
		return self._MsgCnttSgntr

	@MsgCnttSgntr.setter
	def MsgCnttSgntr(self, value):
		self._MsgCnttSgntr = value if value is not None else base_types.UninitialisedField(self, 'MsgCnttSgntr', ContentInformationType38, False)

	@MsgCnttSgntr.deleter
	def MsgCnttSgntr(self):
		del self._MsgCnttSgntr
		self._MsgCnttSgntr = base_types.UninitialisedField(self, 'MsgCnttSgntr', ContentInformationType38, False)

	@property
	def MsgDstn(self):
		return self._MsgDstn

	@MsgDstn.setter
	def MsgDstn(self, value):
		self._MsgDstn = value if value is not None else base_types.UninitialisedField(self, 'MsgDstn', UserInterface9Code, False)

	@MsgDstn.deleter
	def MsgDstn(self):
		del self._MsgDstn
		self._MsgDstn = base_types.UninitialisedField(self, 'MsgDstn', UserInterface9Code, False)

	@property
	def OutptBrcd(self):
		return self._OutptBrcd

	@OutptBrcd.setter
	def OutptBrcd(self, value):
		self._OutptBrcd = value if value is not None else base_types.UninitialisedField(self, 'OutptBrcd', OutputBarcode2, False)

	@OutptBrcd.deleter
	def OutptBrcd(self):
		del self._OutptBrcd
		self._OutptBrcd = base_types.UninitialisedField(self, 'OutptBrcd', OutputBarcode2, False)

	@property
	def RspnReqrdFlg(self):
		return self._RspnReqrdFlg

	@RspnReqrdFlg.setter
	def RspnReqrdFlg(self, value):
		self._RspnReqrdFlg = value if value is not None else base_types.UninitialisedField(self, 'RspnReqrdFlg', TrueFalseIndicator, False)

	@RspnReqrdFlg.deleter
	def RspnReqrdFlg(self):
		del self._RspnReqrdFlg
		self._RspnReqrdFlg = base_types.UninitialisedField(self, 'RspnReqrdFlg', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frmt', type=OutputFormat3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfQlfr', type=InformationQualify1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinDispTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCntt', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgCnttSgntr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgDstn', type=UserInterface9Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutptBrcd', type=OutputBarcode2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnReqrdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))