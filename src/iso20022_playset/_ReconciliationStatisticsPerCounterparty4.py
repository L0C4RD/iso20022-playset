# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODate import ISODate
from ._Number import Number
from ._ReconciliationCounterpartyPairStatistics7 import ReconciliationCounterpartyPairStatistics7
from ._ReportingRequirement3Choice import ReportingRequirement3Choice

class ReconciliationStatisticsPerCounterparty4(base_types._BaseFieldType):

	__slots__ = ["_RcncltnCtgrs", "_RefDt", "_TtlNbOfTxs", "_TxDtls"]
	@property
	def RcncltnCtgrs(self):
		return self._RcncltnCtgrs

	@RcncltnCtgrs.setter
	def RcncltnCtgrs(self, value):
		self._RcncltnCtgrs = value if type(value) != base_types.auto else self.make_default("RcncltnCtgrs")

	@RcncltnCtgrs.deleter
	def RcncltnCtgrs(self):
		del self._RcncltnCtgrs
		self._RcncltnCtgrs = None

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
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != base_types.auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcncltnCtgrs', type=ReportingRequirement3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=ReconciliationCounterpartyPairStatistics7, min=0, max=None, mutex_group=None, array=True),
	))