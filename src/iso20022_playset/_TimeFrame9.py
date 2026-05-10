from . import base_types
from ._BusinessDayConvention1Code import BusinessDayConvention1Code
from ._Max350Text import Max350Text
from ._Number import Number
from ._ReferToFundOrderDesk1Code import ReferToFundOrderDesk1Code

class TimeFrame9(base_types._BaseFieldType):

	__slots__ = ["_NonWorkgDayAdjstmnt", "_OthrTmFrameDesc", "_RefrToOrdrDsk", "_TMns"]
	@property
	def NonWorkgDayAdjstmnt(self):
		return self._NonWorkgDayAdjstmnt

	@NonWorkgDayAdjstmnt.setter
	def NonWorkgDayAdjstmnt(self, value):
		self._NonWorkgDayAdjstmnt = value if type(value) != base_types.auto else self.make_default("NonWorkgDayAdjstmnt")

	@NonWorkgDayAdjstmnt.deleter
	def NonWorkgDayAdjstmnt(self):
		del self._NonWorkgDayAdjstmnt
		self._NonWorkgDayAdjstmnt = None

	@property
	def OthrTmFrameDesc(self):
		return self._OthrTmFrameDesc

	@OthrTmFrameDesc.setter
	def OthrTmFrameDesc(self, value):
		self._OthrTmFrameDesc = value if type(value) != base_types.auto else self.make_default("OthrTmFrameDesc")

	@OthrTmFrameDesc.deleter
	def OthrTmFrameDesc(self):
		del self._OthrTmFrameDesc
		self._OthrTmFrameDesc = None

	@property
	def RefrToOrdrDsk(self):
		return self._RefrToOrdrDsk

	@RefrToOrdrDsk.setter
	def RefrToOrdrDsk(self, value):
		self._RefrToOrdrDsk = value if type(value) != base_types.auto else self.make_default("RefrToOrdrDsk")

	@RefrToOrdrDsk.deleter
	def RefrToOrdrDsk(self):
		del self._RefrToOrdrDsk
		self._RefrToOrdrDsk = None

	@property
	def TMns(self):
		return self._TMns

	@TMns.setter
	def TMns(self, value):
		self._TMns = value if type(value) != base_types.auto else self.make_default("TMns")

	@TMns.deleter
	def TMns(self):
		del self._TMns
		self._TMns = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonWorkgDayAdjstmnt', type=BusinessDayConvention1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTmFrameDesc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefrToOrdrDsk', type=ReferToFundOrderDesk1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMns', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

