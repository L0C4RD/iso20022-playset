from . import base_types
from ._Max35Text import Max35Text
from ._ReconciliationType1Code import ReconciliationType1Code
from ._TransactionTotalsSet2 import TransactionTotalsSet2

class ReconciliationResponseData2(base_types._BaseFieldType):

	__slots__ = ["_POIRcncltnId", "_RcncltnTp", "_TxTtls"]
	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if type(value) != base_types.auto else self.make_default("POIRcncltnId")

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = None

	@property
	def RcncltnTp(self):
		return self._RcncltnTp

	@RcncltnTp.setter
	def RcncltnTp(self, value):
		self._RcncltnTp = value if type(value) != base_types.auto else self.make_default("RcncltnTp")

	@RcncltnTp.deleter
	def RcncltnTp(self):
		del self._RcncltnTp
		self._RcncltnTp = None

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if type(value) != base_types.auto else self.make_default("TxTtls")

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnTp', type=ReconciliationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotalsSet2, min=0, max=None, mutex_group=None, array=True),
	))

