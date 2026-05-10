from . import base_types
from .PaymentTransaction165 import PaymentTransaction165
from .CustomerOrder1 import CustomerOrder1
from .Max35Text import Max35Text

class RetailerReversalResult7(base_types._BaseFieldType):

	__slots__ = ["_CstmrOrdr", "_OrgnlPmtTx", "_POIRcncltnId"]
	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if type(value) != base_types.auto else self.make_default("CstmrOrdr")

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = None

	@property
	def OrgnlPmtTx(self):
		return self._OrgnlPmtTx

	@OrgnlPmtTx.setter
	def OrgnlPmtTx(self, value):
		self._OrgnlPmtTx = value if type(value) != base_types.auto else self.make_default("OrgnlPmtTx")

	@OrgnlPmtTx.deleter
	def OrgnlPmtTx(self):
		del self._OrgnlPmtTx
		self._OrgnlPmtTx = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlPmtTx', type=PaymentTransaction165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

