# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ReconciliationType1Code
from . import TransactionTotalsSet2

class ReconciliationResponseData2(base_types._BaseFieldType):

	__slots__ = ["_POIRcncltnId", "_RcncltnTp", "_TxTtls"]
	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if value is not None else base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

	@property
	def RcncltnTp(self):
		return self._RcncltnTp

	@RcncltnTp.setter
	def RcncltnTp(self, value):
		self._RcncltnTp = value if value is not None else base_types.UninitialisedField(self, 'RcncltnTp', ReconciliationType1Code, False)

	@RcncltnTp.deleter
	def RcncltnTp(self):
		del self._RcncltnTp
		self._RcncltnTp = base_types.UninitialisedField(self, 'RcncltnTp', ReconciliationType1Code, False)

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if value is not None else base_types.UninitialisedField(self, 'TxTtls', TransactionTotalsSet2, True)

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = base_types.UninitialisedField(self, 'TxTtls', TransactionTotalsSet2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnTp', type=ReconciliationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotalsSet2, min=0, max=None, mutex_group=None, array=True),
	))