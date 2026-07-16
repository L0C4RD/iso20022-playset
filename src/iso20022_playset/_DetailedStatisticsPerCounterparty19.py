# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max20PositiveNumber
from . import RejectionStatistics9

class DetailedStatisticsPerCounterparty19(base_types._BaseFieldType):

	__slots__ = ["_RefDt", "_RjctnSttstcs", "_TtlCrrctdRjctns", "_TtlNbOfRpts", "_TtlNbOfRptsAccptd", "_TtlNbOfRptsRjctd", "_TtlNbOfTxs", "_TtlNbOfTxsAccptd", "_TtlNbOfTxsRjctd"]
	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if value is not None else base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	@property
	def RjctnSttstcs(self):
		return self._RjctnSttstcs

	@RjctnSttstcs.setter
	def RjctnSttstcs(self, value):
		self._RjctnSttstcs = value if value is not None else base_types.UninitialisedField(self, 'RjctnSttstcs', RejectionStatistics9, True)

	@RjctnSttstcs.deleter
	def RjctnSttstcs(self):
		del self._RjctnSttstcs
		self._RjctnSttstcs = base_types.UninitialisedField(self, 'RjctnSttstcs', RejectionStatistics9, True)

	@property
	def TtlCrrctdRjctns(self):
		return self._TtlCrrctdRjctns

	@TtlCrrctdRjctns.setter
	def TtlCrrctdRjctns(self, value):
		self._TtlCrrctdRjctns = value if value is not None else base_types.UninitialisedField(self, 'TtlCrrctdRjctns', Max20PositiveNumber, False)

	@TtlCrrctdRjctns.deleter
	def TtlCrrctdRjctns(self):
		del self._TtlCrrctdRjctns
		self._TtlCrrctdRjctns = base_types.UninitialisedField(self, 'TtlCrrctdRjctns', Max20PositiveNumber, False)

	@property
	def TtlNbOfRpts(self):
		return self._TtlNbOfRpts

	@TtlNbOfRpts.setter
	def TtlNbOfRpts(self, value):
		self._TtlNbOfRpts = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfRpts', Max20PositiveNumber, False)

	@TtlNbOfRpts.deleter
	def TtlNbOfRpts(self):
		del self._TtlNbOfRpts
		self._TtlNbOfRpts = base_types.UninitialisedField(self, 'TtlNbOfRpts', Max20PositiveNumber, False)

	@property
	def TtlNbOfRptsAccptd(self):
		return self._TtlNbOfRptsAccptd

	@TtlNbOfRptsAccptd.setter
	def TtlNbOfRptsAccptd(self, value):
		self._TtlNbOfRptsAccptd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfRptsAccptd', Max20PositiveNumber, False)

	@TtlNbOfRptsAccptd.deleter
	def TtlNbOfRptsAccptd(self):
		del self._TtlNbOfRptsAccptd
		self._TtlNbOfRptsAccptd = base_types.UninitialisedField(self, 'TtlNbOfRptsAccptd', Max20PositiveNumber, False)

	@property
	def TtlNbOfRptsRjctd(self):
		return self._TtlNbOfRptsRjctd

	@TtlNbOfRptsRjctd.setter
	def TtlNbOfRptsRjctd(self, value):
		self._TtlNbOfRptsRjctd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfRptsRjctd', Max20PositiveNumber, False)

	@TtlNbOfRptsRjctd.deleter
	def TtlNbOfRptsRjctd(self):
		del self._TtlNbOfRptsRjctd
		self._TtlNbOfRptsRjctd = base_types.UninitialisedField(self, 'TtlNbOfRptsRjctd', Max20PositiveNumber, False)

	@property
	def TtlNbOfTxs(self):
		return self._TtlNbOfTxs

	@TtlNbOfTxs.setter
	def TtlNbOfTxs(self, value):
		self._TtlNbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTxs', Max20PositiveNumber, False)

	@TtlNbOfTxs.deleter
	def TtlNbOfTxs(self):
		del self._TtlNbOfTxs
		self._TtlNbOfTxs = base_types.UninitialisedField(self, 'TtlNbOfTxs', Max20PositiveNumber, False)

	@property
	def TtlNbOfTxsAccptd(self):
		return self._TtlNbOfTxsAccptd

	@TtlNbOfTxsAccptd.setter
	def TtlNbOfTxsAccptd(self, value):
		self._TtlNbOfTxsAccptd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTxsAccptd', Max20PositiveNumber, False)

	@TtlNbOfTxsAccptd.deleter
	def TtlNbOfTxsAccptd(self):
		del self._TtlNbOfTxsAccptd
		self._TtlNbOfTxsAccptd = base_types.UninitialisedField(self, 'TtlNbOfTxsAccptd', Max20PositiveNumber, False)

	@property
	def TtlNbOfTxsRjctd(self):
		return self._TtlNbOfTxsRjctd

	@TtlNbOfTxsRjctd.setter
	def TtlNbOfTxsRjctd(self, value):
		self._TtlNbOfTxsRjctd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTxsRjctd', Max20PositiveNumber, False)

	@TtlNbOfTxsRjctd.deleter
	def TtlNbOfTxsRjctd(self):
		del self._TtlNbOfTxsRjctd
		self._TtlNbOfTxsRjctd = base_types.UninitialisedField(self, 'TtlNbOfTxsRjctd', Max20PositiveNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnSttstcs', type=RejectionStatistics9, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlCrrctdRjctns', type=Max20PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfRpts', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfRptsAccptd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfRptsRjctd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxs', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxsAccptd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxsRjctd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
	))