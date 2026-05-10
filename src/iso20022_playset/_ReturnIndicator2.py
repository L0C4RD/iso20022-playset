from . import base_types
from ._InvestigationResult1Choice import InvestigationResult1Choice
from ._AuthorityRequestType1 import AuthorityRequestType1
from ._Max500Text import Max500Text
from ._DateOrDateTimePeriod1Choice import DateOrDateTimePeriod1Choice

class ReturnIndicator2(base_types._BaseFieldType):

	__slots__ = ["_AuthrtyReqTp", "_RspnPrd", "_AddtlInf", "_InvstgtnRslt"]
	@property
	def AuthrtyReqTp(self):
		return self._AuthrtyReqTp

	@AuthrtyReqTp.setter
	def AuthrtyReqTp(self, value):
		self._AuthrtyReqTp = value if type(value) != base_types.auto else self.make_default("AuthrtyReqTp")

	@AuthrtyReqTp.deleter
	def AuthrtyReqTp(self):
		del self._AuthrtyReqTp
		self._AuthrtyReqTp = None

	@property
	def RspnPrd(self):
		return self._RspnPrd

	@RspnPrd.setter
	def RspnPrd(self, value):
		self._RspnPrd = value if type(value) != base_types.auto else self.make_default("RspnPrd")

	@RspnPrd.deleter
	def RspnPrd(self):
		del self._RspnPrd
		self._RspnPrd = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def InvstgtnRslt(self):
		return self._InvstgtnRslt

	@InvstgtnRslt.setter
	def InvstgtnRslt(self, value):
		self._InvstgtnRslt = value if type(value) != base_types.auto else self.make_default("InvstgtnRslt")

	@InvstgtnRslt.deleter
	def InvstgtnRslt(self):
		del self._InvstgtnRslt
		self._InvstgtnRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthrtyReqTp', type=AuthorityRequestType1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnPrd', type=DateOrDateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnRslt', type=InvestigationResult1Choice, min=1, max=1, mutex_group=None, array=False),
	))

