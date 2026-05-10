from . import base_types
from .RejectionStatistics9 import RejectionStatistics9
from .Max20PositiveNumber import Max20PositiveNumber
from .ISODate import ISODate

class DetailedStatisticsPerCounterparty19(base_types._BaseFieldType):

	__slots__ = ["_TtlNbOfRptsRjctd", "_TtlNbOfTxsRjctd", "_RefDt", "_TtlCrrctdRjctns", "_TtlNbOfTxs", "_RjctnSttstcs", "_TtlNbOfRptsAccptd", "_TtlNbOfRpts", "_TtlNbOfTxsAccptd"]
	@property
	def TtlNbOfRptsRjctd(self):
		return self._TtlNbOfRptsRjctd

	@TtlNbOfRptsRjctd.setter
	def TtlNbOfRptsRjctd(self, value):
		self._TtlNbOfRptsRjctd = value if type(value) != base_types.auto else self.make_default("TtlNbOfRptsRjctd")

	@TtlNbOfRptsRjctd.deleter
	def TtlNbOfRptsRjctd(self):
		del self._TtlNbOfRptsRjctd
		self._TtlNbOfRptsRjctd = None

	@property
	def TtlNbOfTxsRjctd(self):
		return self._TtlNbOfTxsRjctd

	@TtlNbOfTxsRjctd.setter
	def TtlNbOfTxsRjctd(self, value):
		self._TtlNbOfTxsRjctd = value if type(value) != base_types.auto else self.make_default("TtlNbOfTxsRjctd")

	@TtlNbOfTxsRjctd.deleter
	def TtlNbOfTxsRjctd(self):
		del self._TtlNbOfTxsRjctd
		self._TtlNbOfTxsRjctd = None

	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if type(value) != base_types.auto else self.make_default("RefDt")

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = None

	@property
	def TtlCrrctdRjctns(self):
		return self._TtlCrrctdRjctns

	@TtlCrrctdRjctns.setter
	def TtlCrrctdRjctns(self, value):
		self._TtlCrrctdRjctns = value if type(value) != base_types.auto else self.make_default("TtlCrrctdRjctns")

	@TtlCrrctdRjctns.deleter
	def TtlCrrctdRjctns(self):
		del self._TtlCrrctdRjctns
		self._TtlCrrctdRjctns = None

	@property
	def TtlNbOfTxs(self):
		return self._TtlNbOfTxs

	@TtlNbOfTxs.setter
	def TtlNbOfTxs(self, value):
		self._TtlNbOfTxs = value if type(value) != base_types.auto else self.make_default("TtlNbOfTxs")

	@TtlNbOfTxs.deleter
	def TtlNbOfTxs(self):
		del self._TtlNbOfTxs
		self._TtlNbOfTxs = None

	@property
	def RjctnSttstcs(self):
		return self._RjctnSttstcs

	@RjctnSttstcs.setter
	def RjctnSttstcs(self, value):
		self._RjctnSttstcs = value if type(value) != base_types.auto else self.make_default("RjctnSttstcs")

	@RjctnSttstcs.deleter
	def RjctnSttstcs(self):
		del self._RjctnSttstcs
		self._RjctnSttstcs = None

	@property
	def TtlNbOfRptsAccptd(self):
		return self._TtlNbOfRptsAccptd

	@TtlNbOfRptsAccptd.setter
	def TtlNbOfRptsAccptd(self, value):
		self._TtlNbOfRptsAccptd = value if type(value) != base_types.auto else self.make_default("TtlNbOfRptsAccptd")

	@TtlNbOfRptsAccptd.deleter
	def TtlNbOfRptsAccptd(self):
		del self._TtlNbOfRptsAccptd
		self._TtlNbOfRptsAccptd = None

	@property
	def TtlNbOfRpts(self):
		return self._TtlNbOfRpts

	@TtlNbOfRpts.setter
	def TtlNbOfRpts(self, value):
		self._TtlNbOfRpts = value if type(value) != base_types.auto else self.make_default("TtlNbOfRpts")

	@TtlNbOfRpts.deleter
	def TtlNbOfRpts(self):
		del self._TtlNbOfRpts
		self._TtlNbOfRpts = None

	@property
	def TtlNbOfTxsAccptd(self):
		return self._TtlNbOfTxsAccptd

	@TtlNbOfTxsAccptd.setter
	def TtlNbOfTxsAccptd(self, value):
		self._TtlNbOfTxsAccptd = value if type(value) != base_types.auto else self.make_default("TtlNbOfTxsAccptd")

	@TtlNbOfTxsAccptd.deleter
	def TtlNbOfTxsAccptd(self):
		del self._TtlNbOfTxsAccptd
		self._TtlNbOfTxsAccptd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlNbOfRptsRjctd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxsRjctd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCrrctdRjctns', type=Max20PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxs', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnSttstcs', type=RejectionStatistics9, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNbOfRptsAccptd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfRpts', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxsAccptd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
	))

