from . import base_types
from ._RequestedIndicator import RequestedIndicator

class SecuritiesAccountReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_PtyTp", "_ClsgDt", "_OpngDt", "_PricgSchme", "_EndInvstrFlg", "_AcctSvcr", "_AcctTp", "_PtyId", "_AcctId"]
	@property
	def PtyTp(self):
		return self._PtyTp

	@PtyTp.setter
	def PtyTp(self, value):
		self._PtyTp = value if type(value) != base_types.auto else self.make_default("PtyTp")

	@PtyTp.deleter
	def PtyTp(self):
		del self._PtyTp
		self._PtyTp = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != base_types.auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if type(value) != base_types.auto else self.make_default("OpngDt")

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = None

	@property
	def PricgSchme(self):
		return self._PricgSchme

	@PricgSchme.setter
	def PricgSchme(self, value):
		self._PricgSchme = value if type(value) != base_types.auto else self.make_default("PricgSchme")

	@PricgSchme.deleter
	def PricgSchme(self):
		del self._PricgSchme
		self._PricgSchme = None

	@property
	def EndInvstrFlg(self):
		return self._EndInvstrFlg

	@EndInvstrFlg.setter
	def EndInvstrFlg(self, value):
		self._EndInvstrFlg = value if type(value) != base_types.auto else self.make_default("EndInvstrFlg")

	@EndInvstrFlg.deleter
	def EndInvstrFlg(self):
		del self._EndInvstrFlg
		self._EndInvstrFlg = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != base_types.auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtyTp', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgSchme', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndInvstrFlg', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTp', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

