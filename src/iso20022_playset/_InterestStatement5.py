from . import base_types
from .Max35Text import Max35Text
from .DatePeriod2 import DatePeriod2
from .InterestCalculation5 import InterestCalculation5
from .ISODate import ISODate
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class InterestStatement5(base_types._BaseFieldType):

	__slots__ = ["_ValDt", "_TtlIntrstAmtDueToA", "_IntrstPrd", "_IntrstClctn", "_IntrstPmtReqId", "_TtlIntrstAmtDueToB"]
	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def TtlIntrstAmtDueToA(self):
		return self._TtlIntrstAmtDueToA

	@TtlIntrstAmtDueToA.setter
	def TtlIntrstAmtDueToA(self, value):
		self._TtlIntrstAmtDueToA = value if type(value) != base_types.auto else self.make_default("TtlIntrstAmtDueToA")

	@TtlIntrstAmtDueToA.deleter
	def TtlIntrstAmtDueToA(self):
		del self._TtlIntrstAmtDueToA
		self._TtlIntrstAmtDueToA = None

	@property
	def IntrstPrd(self):
		return self._IntrstPrd

	@IntrstPrd.setter
	def IntrstPrd(self, value):
		self._IntrstPrd = value if type(value) != base_types.auto else self.make_default("IntrstPrd")

	@IntrstPrd.deleter
	def IntrstPrd(self):
		del self._IntrstPrd
		self._IntrstPrd = None

	@property
	def IntrstClctn(self):
		return self._IntrstClctn

	@IntrstClctn.setter
	def IntrstClctn(self, value):
		self._IntrstClctn = value if type(value) != base_types.auto else self.make_default("IntrstClctn")

	@IntrstClctn.deleter
	def IntrstClctn(self):
		del self._IntrstClctn
		self._IntrstClctn = None

	@property
	def IntrstPmtReqId(self):
		return self._IntrstPmtReqId

	@IntrstPmtReqId.setter
	def IntrstPmtReqId(self, value):
		self._IntrstPmtReqId = value if type(value) != base_types.auto else self.make_default("IntrstPmtReqId")

	@IntrstPmtReqId.deleter
	def IntrstPmtReqId(self):
		del self._IntrstPmtReqId
		self._IntrstPmtReqId = None

	@property
	def TtlIntrstAmtDueToB(self):
		return self._TtlIntrstAmtDueToB

	@TtlIntrstAmtDueToB.setter
	def TtlIntrstAmtDueToB(self, value):
		self._TtlIntrstAmtDueToB = value if type(value) != base_types.auto else self.make_default("TtlIntrstAmtDueToB")

	@TtlIntrstAmtDueToB.deleter
	def TtlIntrstAmtDueToB(self):
		del self._TtlIntrstAmtDueToB
		self._TtlIntrstAmtDueToB = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlIntrstAmtDueToA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstClctn', type=InterestCalculation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstPmtReqId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlIntrstAmtDueToB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

