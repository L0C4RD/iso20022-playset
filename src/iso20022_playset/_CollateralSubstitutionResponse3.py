from . import base_types
from .Max35Text import Max35Text
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .RejectionReason68Code import RejectionReason68Code
from .Max140Text import Max140Text

class CollateralSubstitutionResponse3(base_types._BaseFieldType):

	__slots__ = ["_RjctnRsn", "_RjctnRsnInf", "_RjctdAmt", "_CollSbstitnReqId"]
	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != base_types.auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

	@property
	def RjctnRsnInf(self):
		return self._RjctnRsnInf

	@RjctnRsnInf.setter
	def RjctnRsnInf(self, value):
		self._RjctnRsnInf = value if type(value) != base_types.auto else self.make_default("RjctnRsnInf")

	@RjctnRsnInf.deleter
	def RjctnRsnInf(self):
		del self._RjctnRsnInf
		self._RjctnRsnInf = None

	@property
	def RjctdAmt(self):
		return self._RjctdAmt

	@RjctdAmt.setter
	def RjctdAmt(self, value):
		self._RjctdAmt = value if type(value) != base_types.auto else self.make_default("RjctdAmt")

	@RjctdAmt.deleter
	def RjctdAmt(self):
		del self._RjctdAmt
		self._RjctdAmt = None

	@property
	def CollSbstitnReqId(self):
		return self._CollSbstitnReqId

	@CollSbstitnReqId.setter
	def CollSbstitnReqId(self, value):
		self._CollSbstitnReqId = value if type(value) != base_types.auto else self.make_default("CollSbstitnReqId")

	@CollSbstitnReqId.deleter
	def CollSbstitnReqId(self):
		del self._CollSbstitnReqId
		self._CollSbstitnReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason68Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsnInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

