from . import base_types
from ._PaymentType4Choice import PaymentType4Choice
from ._ISODateTime import ISODateTime

class PaymentInstruction13(base_types._BaseFieldType):

	__slots__ = ["_ReqdExctnDtTm", "_PmtTp"]
	@property
	def ReqdExctnDtTm(self):
		return self._ReqdExctnDtTm

	@ReqdExctnDtTm.setter
	def ReqdExctnDtTm(self, value):
		self._ReqdExctnDtTm = value if type(value) != base_types.auto else self.make_default("ReqdExctnDtTm")

	@ReqdExctnDtTm.deleter
	def ReqdExctnDtTm(self):
		del self._ReqdExctnDtTm
		self._ReqdExctnDtTm = None

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if type(value) != base_types.auto else self.make_default("PmtTp")

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqdExctnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTp', type=PaymentType4Choice, min=0, max=1, mutex_group=None, array=False),
	))

