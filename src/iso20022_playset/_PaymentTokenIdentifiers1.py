from . import base_types
from ._Max35Text import Max35Text

class PaymentTokenIdentifiers1(base_types._BaseFieldType):

	__slots__ = ["_RqstrId", "_PrvdrId"]
	@property
	def RqstrId(self):
		return self._RqstrId

	@RqstrId.setter
	def RqstrId(self, value):
		self._RqstrId = value if type(value) != base_types.auto else self.make_default("RqstrId")

	@RqstrId.deleter
	def RqstrId(self):
		del self._RqstrId
		self._RqstrId = None

	@property
	def PrvdrId(self):
		return self._PrvdrId

	@PrvdrId.setter
	def PrvdrId(self, value):
		self._PrvdrId = value if type(value) != base_types.auto else self.make_default("PrvdrId")

	@PrvdrId.deleter
	def PrvdrId(self):
		del self._PrvdrId
		self._PrvdrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RqstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

