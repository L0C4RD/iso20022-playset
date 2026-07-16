# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CounterpartyData91
from . import Number
from . import ReconciliationReport15

class ReconciliationCounterpartyPairStatistics7(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_RcncltnRpt", "_TtlNbOfTxs"]
	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyId', CounterpartyData91, False)

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = base_types.UninitialisedField(self, 'CtrPtyId', CounterpartyData91, False)

	@property
	def RcncltnRpt(self):
		return self._RcncltnRpt

	@RcncltnRpt.setter
	def RcncltnRpt(self, value):
		self._RcncltnRpt = value if value is not None else base_types.UninitialisedField(self, 'RcncltnRpt', ReconciliationReport15, True)

	@RcncltnRpt.deleter
	def RcncltnRpt(self):
		del self._RcncltnRpt
		self._RcncltnRpt = base_types.UninitialisedField(self, 'RcncltnRpt', ReconciliationReport15, True)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData91, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnRpt', type=ReconciliationReport15, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNbOfTxs', type=Number, min=1, max=1, mutex_group=None, array=False),
	))