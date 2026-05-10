from . import base_types
from .MICIdentifier import MICIdentifier
from .TrueFalseIndicator import TrueFalseIndicator
from .ISODateTime import ISODateTime

class TradingVenueAttributes1(base_types._BaseFieldType):

	__slots__ = ["_IssrReq", "_ReqForAdmssnDt", "_FrstTradDt", "_AdmssnApprvlDtByIssr", "_Id", "_TermntnDt"]
	@property
	def IssrReq(self):
		return self._IssrReq

	@IssrReq.setter
	def IssrReq(self, value):
		self._IssrReq = value if type(value) != base_types.auto else self.make_default("IssrReq")

	@IssrReq.deleter
	def IssrReq(self):
		del self._IssrReq
		self._IssrReq = None

	@property
	def ReqForAdmssnDt(self):
		return self._ReqForAdmssnDt

	@ReqForAdmssnDt.setter
	def ReqForAdmssnDt(self, value):
		self._ReqForAdmssnDt = value if type(value) != base_types.auto else self.make_default("ReqForAdmssnDt")

	@ReqForAdmssnDt.deleter
	def ReqForAdmssnDt(self):
		del self._ReqForAdmssnDt
		self._ReqForAdmssnDt = None

	@property
	def FrstTradDt(self):
		return self._FrstTradDt

	@FrstTradDt.setter
	def FrstTradDt(self, value):
		self._FrstTradDt = value if type(value) != base_types.auto else self.make_default("FrstTradDt")

	@FrstTradDt.deleter
	def FrstTradDt(self):
		del self._FrstTradDt
		self._FrstTradDt = None

	@property
	def AdmssnApprvlDtByIssr(self):
		return self._AdmssnApprvlDtByIssr

	@AdmssnApprvlDtByIssr.setter
	def AdmssnApprvlDtByIssr(self, value):
		self._AdmssnApprvlDtByIssr = value if type(value) != base_types.auto else self.make_default("AdmssnApprvlDtByIssr")

	@AdmssnApprvlDtByIssr.deleter
	def AdmssnApprvlDtByIssr(self):
		del self._AdmssnApprvlDtByIssr
		self._AdmssnApprvlDtByIssr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != base_types.auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssrReq', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForAdmssnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstTradDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdmssnApprvlDtByIssr', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

