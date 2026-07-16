# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import MICIdentifier
from . import TrueFalseIndicator

class TradingVenueAttributes2(base_types._BaseFieldType):

	__slots__ = ["_AdmssnApprvlDtByIssr", "_FrstTradDt", "_Id", "_IssrReq", "_ReqForAdmssnDt", "_TermntnDt"]
	@property
	def AdmssnApprvlDtByIssr(self):
		return self._AdmssnApprvlDtByIssr

	@AdmssnApprvlDtByIssr.setter
	def AdmssnApprvlDtByIssr(self, value):
		self._AdmssnApprvlDtByIssr = value if value is not None else base_types.UninitialisedField(self, 'AdmssnApprvlDtByIssr', ISODateTime, False)

	@AdmssnApprvlDtByIssr.deleter
	def AdmssnApprvlDtByIssr(self):
		del self._AdmssnApprvlDtByIssr
		self._AdmssnApprvlDtByIssr = base_types.UninitialisedField(self, 'AdmssnApprvlDtByIssr', ISODateTime, False)

	@property
	def FrstTradDt(self):
		return self._FrstTradDt

	@FrstTradDt.setter
	def FrstTradDt(self, value):
		self._FrstTradDt = value if value is not None else base_types.UninitialisedField(self, 'FrstTradDt', ISODateTime, False)

	@FrstTradDt.deleter
	def FrstTradDt(self):
		del self._FrstTradDt
		self._FrstTradDt = base_types.UninitialisedField(self, 'FrstTradDt', ISODateTime, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', MICIdentifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', MICIdentifier, False)

	@property
	def IssrReq(self):
		return self._IssrReq

	@IssrReq.setter
	def IssrReq(self, value):
		self._IssrReq = value if value is not None else base_types.UninitialisedField(self, 'IssrReq', TrueFalseIndicator, False)

	@IssrReq.deleter
	def IssrReq(self):
		del self._IssrReq
		self._IssrReq = base_types.UninitialisedField(self, 'IssrReq', TrueFalseIndicator, False)

	@property
	def ReqForAdmssnDt(self):
		return self._ReqForAdmssnDt

	@ReqForAdmssnDt.setter
	def ReqForAdmssnDt(self, value):
		self._ReqForAdmssnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqForAdmssnDt', ISODateTime, False)

	@ReqForAdmssnDt.deleter
	def ReqForAdmssnDt(self):
		del self._ReqForAdmssnDt
		self._ReqForAdmssnDt = base_types.UninitialisedField(self, 'ReqForAdmssnDt', ISODateTime, False)

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if value is not None else base_types.UninitialisedField(self, 'TermntnDt', ISODateTime, False)

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = base_types.UninitialisedField(self, 'TermntnDt', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdmssnApprvlDtByIssr', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstTradDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrReq', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForAdmssnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))