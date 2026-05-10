from . import base_types
import Max35Text
import CustomerOrder1
import PaymentTransaction165

class RetailerReversalResult7(base_types._BaseFieldType):

	__slots__ = ["_OrgnlPmtTx", "_POIRcncltnId", "_CstmrOrdr"]
	@property
	def OrgnlPmtTx(self):
		return self._OrgnlPmtTx

	@OrgnlPmtTx.setter
	def OrgnlPmtTx(self, value):
		self._OrgnlPmtTx = value if type(value) != auto else self.make_default("OrgnlPmtTx")

	@OrgnlPmtTx.deleter
	def OrgnlPmtTx(self):
		del self._OrgnlPmtTx
		self._OrgnlPmtTx = None

	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if type(value) != auto else self.make_default("POIRcncltnId")

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = None

	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if type(value) != auto else self.make_default("CstmrOrdr")

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlPmtTx', type=PaymentTransaction165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=None, mutex_group=None, array=True),
	))

