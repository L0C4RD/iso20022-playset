# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import LanguageCode
from . import RetailerEvent8
from . import TrueFalseIndicator

class EventNotificationData8(base_types._BaseFieldType):

	__slots__ = ["_CstmrLang", "_DispOutpt", "_MntncReqrdFlg", "_RtlrEvt"]
	@property
	def CstmrLang(self):
		return self._CstmrLang

	@CstmrLang.setter
	def CstmrLang(self, value):
		self._CstmrLang = value if value is not None else base_types.UninitialisedField(self, 'CstmrLang', LanguageCode, False)

	@CstmrLang.deleter
	def CstmrLang(self):
		del self._CstmrLang
		self._CstmrLang = base_types.UninitialisedField(self, 'CstmrLang', LanguageCode, False)

	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if value is not None else base_types.UninitialisedField(self, 'DispOutpt', ActionMessage12, False)

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = base_types.UninitialisedField(self, 'DispOutpt', ActionMessage12, False)

	@property
	def MntncReqrdFlg(self):
		return self._MntncReqrdFlg

	@MntncReqrdFlg.setter
	def MntncReqrdFlg(self, value):
		self._MntncReqrdFlg = value if value is not None else base_types.UninitialisedField(self, 'MntncReqrdFlg', TrueFalseIndicator, False)

	@MntncReqrdFlg.deleter
	def MntncReqrdFlg(self):
		del self._MntncReqrdFlg
		self._MntncReqrdFlg = base_types.UninitialisedField(self, 'MntncReqrdFlg', TrueFalseIndicator, False)

	@property
	def RtlrEvt(self):
		return self._RtlrEvt

	@RtlrEvt.setter
	def RtlrEvt(self, value):
		self._RtlrEvt = value if value is not None else base_types.UninitialisedField(self, 'RtlrEvt', RetailerEvent8, False)

	@RtlrEvt.deleter
	def RtlrEvt(self):
		del self._RtlrEvt
		self._RtlrEvt = base_types.UninitialisedField(self, 'RtlrEvt', RetailerEvent8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncReqrdFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtlrEvt', type=RetailerEvent8, min=1, max=1, mutex_group=None, array=False),
	))