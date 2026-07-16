# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Number
from . import ReconciliationCounterpartyPairStatistics7
from . import ReportingRequirement3Choice

class ReconciliationStatisticsPerCounterparty4(base_types._BaseFieldType):

	__slots__ = ["_RcncltnCtgrs", "_RefDt", "_TtlNbOfTxs", "_TxDtls"]
	@property
	def RcncltnCtgrs(self):
		return self._RcncltnCtgrs

	@RcncltnCtgrs.setter
	def RcncltnCtgrs(self, value):
		self._RcncltnCtgrs = value if value is not None else base_types.UninitialisedField(self, 'RcncltnCtgrs', ReportingRequirement3Choice, False)

	@RcncltnCtgrs.deleter
	def RcncltnCtgrs(self):
		del self._RcncltnCtgrs
		self._RcncltnCtgrs = base_types.UninitialisedField(self, 'RcncltnCtgrs', ReportingRequirement3Choice, False)

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
	def TtlNbOfTxs(self):
		return self._TtlNbOfTxs

	@TtlNbOfTxs.setter
	def TtlNbOfTxs(self, value):
		self._TtlNbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTxs', Number, False)

	@TtlNbOfTxs.deleter
	def TtlNbOfTxs(self):
		del self._TtlNbOfTxs
		self._TtlNbOfTxs = base_types.UninitialisedField(self, 'TtlNbOfTxs', Number, False)

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', ReconciliationCounterpartyPairStatistics7, True)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', ReconciliationCounterpartyPairStatistics7, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcncltnCtgrs', type=ReportingRequirement3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=ReconciliationCounterpartyPairStatistics7, min=0, max=None, mutex_group=None, array=True),
	))