import base_types
import RetailerEvent7
import ActionMessage11
import TrueFalseIndicator
import LanguageCode

class EventNotificationData7(base_types._BaseFieldType):

	__slots__ = ["_CstmrLang", "_DispOutpt", "_MntncReqrdFlg", "_RtlrEvt"]
	@property
	def CstmrLang(self):
		return self._CstmrLang

	@CstmrLang.setter
	def CstmrLang(self, value):
		self._CstmrLang = value if type(value) != auto else self.make_default("CstmrLang")

	@CstmrLang.deleter
	def CstmrLang(self):
		del self._CstmrLang
		self._CstmrLang = None

	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if type(value) != auto else self.make_default("DispOutpt")

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = None

	@property
	def MntncReqrdFlg(self):
		return self._MntncReqrdFlg

	@MntncReqrdFlg.setter
	def MntncReqrdFlg(self, value):
		self._MntncReqrdFlg = value if type(value) != auto else self.make_default("MntncReqrdFlg")

	@MntncReqrdFlg.deleter
	def MntncReqrdFlg(self):
		del self._MntncReqrdFlg
		self._MntncReqrdFlg = None

	@property
	def RtlrEvt(self):
		return self._RtlrEvt

	@RtlrEvt.setter
	def RtlrEvt(self, value):
		self._RtlrEvt = value if type(value) != auto else self.make_default("RtlrEvt")

	@RtlrEvt.deleter
	def RtlrEvt(self):
		del self._RtlrEvt
		self._RtlrEvt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncReqrdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtlrEvt', type=RetailerEvent7, min=1, max=1, mutex_group=None, array=False),
	))

