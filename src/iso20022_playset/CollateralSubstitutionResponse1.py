import base_types
import Max35Text
import ActiveCurrencyAndAmount

class CollateralSubstitutionResponse1(base_types._BaseFieldType):

	__slots__ = ["_AccptdAmt", "_CollSbstitnReqId"]
	@property
	def AccptdAmt(self):
		return self._AccptdAmt

	@AccptdAmt.setter
	def AccptdAmt(self, value):
		self._AccptdAmt = value if type(value) != auto else self.make_default("AccptdAmt")

	@AccptdAmt.deleter
	def AccptdAmt(self):
		del self._AccptdAmt
		self._AccptdAmt = None

	@property
	def CollSbstitnReqId(self):
		return self._CollSbstitnReqId

	@CollSbstitnReqId.setter
	def CollSbstitnReqId(self, value):
		self._CollSbstitnReqId = value if type(value) != auto else self.make_default("CollSbstitnReqId")

	@CollSbstitnReqId.deleter
	def CollSbstitnReqId(self):
		del self._CollSbstitnReqId
		self._CollSbstitnReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

