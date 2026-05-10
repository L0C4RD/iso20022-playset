from . import base_types
from ._DateFormat15Choice import DateFormat15Choice
from ._ISODate import ISODate
from ._YesNoIndicator import YesNoIndicator

class BuyIn4(base_types._BaseFieldType):

	__slots__ = ["_BuyInRvrsnDt", "_CxlLmtDt", "_WrngInd", "_XpctdBuyInDt"]
	@property
	def BuyInRvrsnDt(self):
		return self._BuyInRvrsnDt

	@BuyInRvrsnDt.setter
	def BuyInRvrsnDt(self, value):
		self._BuyInRvrsnDt = value if type(value) != base_types.auto else self.make_default("BuyInRvrsnDt")

	@BuyInRvrsnDt.deleter
	def BuyInRvrsnDt(self):
		del self._BuyInRvrsnDt
		self._BuyInRvrsnDt = None

	@property
	def CxlLmtDt(self):
		return self._CxlLmtDt

	@CxlLmtDt.setter
	def CxlLmtDt(self, value):
		self._CxlLmtDt = value if type(value) != base_types.auto else self.make_default("CxlLmtDt")

	@CxlLmtDt.deleter
	def CxlLmtDt(self):
		del self._CxlLmtDt
		self._CxlLmtDt = None

	@property
	def WrngInd(self):
		return self._WrngInd

	@WrngInd.setter
	def WrngInd(self, value):
		self._WrngInd = value if type(value) != base_types.auto else self.make_default("WrngInd")

	@WrngInd.deleter
	def WrngInd(self):
		del self._WrngInd
		self._WrngInd = None

	@property
	def XpctdBuyInDt(self):
		return self._XpctdBuyInDt

	@XpctdBuyInDt.setter
	def XpctdBuyInDt(self, value):
		self._XpctdBuyInDt = value if type(value) != base_types.auto else self.make_default("XpctdBuyInDt")

	@XpctdBuyInDt.deleter
	def XpctdBuyInDt(self):
		del self._XpctdBuyInDt
		self._XpctdBuyInDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyInRvrsnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlLmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WrngInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdBuyInDt', type=DateFormat15Choice, min=1, max=1, mutex_group=None, array=False),
	))

