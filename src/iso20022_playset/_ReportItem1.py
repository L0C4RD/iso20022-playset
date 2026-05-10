from . import base_types
from ._ISODate import ISODate
from ._SecurityIdentification19 import SecurityIdentification19
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._HoldingAccountLevel1Code import HoldingAccountLevel1Code

class ReportItem1(base_types._BaseFieldType):

	__slots__ = ["_AcctLvl", "_ItmDt", "_AcctId", "_FinInstrmId"]
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

	@property
	def AcctLvl(self):
		return self._AcctLvl

	@AcctLvl.setter
	def AcctLvl(self, value):
		self._AcctLvl = value if type(value) != base_types.auto else self.make_default("AcctLvl")

	@AcctLvl.deleter
	def AcctLvl(self):
		del self._AcctLvl
		self._AcctLvl = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def ItmDt(self):
		return self._ItmDt

	@ItmDt.setter
	def ItmDt(self, value):
		self._ItmDt = value if type(value) != base_types.auto else self.make_default("ItmDt")

	@ItmDt.deleter
	def ItmDt(self):
		del self._ItmDt
		self._ItmDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctLvl', type=HoldingAccountLevel1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

