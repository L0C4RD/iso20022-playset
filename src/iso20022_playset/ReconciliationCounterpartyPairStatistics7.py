import base_types
import ReconciliationReport15
import CounterpartyData91
import Number

class ReconciliationCounterpartyPairStatistics7(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_TtlNbOfTxs", "_RcncltnRpt"]
	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	@property
	def TtlNbOfTxs(self):
		return self._TtlNbOfTxs

	@TtlNbOfTxs.setter
	def TtlNbOfTxs(self, value):
		self._TtlNbOfTxs = value if type(value) != auto else self.make_default("TtlNbOfTxs")

	@TtlNbOfTxs.deleter
	def TtlNbOfTxs(self):
		del self._TtlNbOfTxs
		self._TtlNbOfTxs = None

	@property
	def RcncltnRpt(self):
		return self._RcncltnRpt

	@RcncltnRpt.setter
	def RcncltnRpt(self, value):
		self._RcncltnRpt = value if type(value) != auto else self.make_default("RcncltnRpt")

	@RcncltnRpt.deleter
	def RcncltnRpt(self):
		del self._RcncltnRpt
		self._RcncltnRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData91, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnRpt', type=ReconciliationReport15, min=1, max=None, mutex_group=None, array=True),
	))

