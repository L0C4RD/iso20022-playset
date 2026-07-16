# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerOrder1
from . import Max35Text
from . import PaymentTransaction183

class RetailerReversalResult8(base_types._BaseFieldType):

	__slots__ = ["_CstmrOrdr", "_OrgnlPmtTx", "_POIRcncltnId"]
	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, True)

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, True)

	@property
	def OrgnlPmtTx(self):
		return self._OrgnlPmtTx

	@OrgnlPmtTx.setter
	def OrgnlPmtTx(self, value):
		self._OrgnlPmtTx = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPmtTx', PaymentTransaction183, False)

	@OrgnlPmtTx.deleter
	def OrgnlPmtTx(self):
		del self._OrgnlPmtTx
		self._OrgnlPmtTx = base_types.UninitialisedField(self, 'OrgnlPmtTx', PaymentTransaction183, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlPmtTx', type=PaymentTransaction183, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))