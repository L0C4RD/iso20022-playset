from . import base_types
from ._PaymentCard4 import PaymentCard4
from ._CardAggregated2 import CardAggregated2
from ._PointOfInteraction1 import PointOfInteraction1
from ._CashAccount40 import CashAccount40

class CardEntry5(base_types._BaseFieldType):

	__slots__ = ["_AggtdNtry", "_Card", "_PrePdAcct", "_POI"]
	@property
	def AggtdNtry(self):
		return self._AggtdNtry

	@AggtdNtry.setter
	def AggtdNtry(self, value):
		self._AggtdNtry = value if type(value) != base_types.auto else self.make_default("AggtdNtry")

	@AggtdNtry.deleter
	def AggtdNtry(self):
		del self._AggtdNtry
		self._AggtdNtry = None

	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if type(value) != base_types.auto else self.make_default("Card")

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = None

	@property
	def POI(self):
		return self._POI

	@POI.setter
	def POI(self, value):
		self._POI = value if type(value) != base_types.auto else self.make_default("POI")

	@POI.deleter
	def POI(self):
		del self._POI
		self._POI = None

	@property
	def PrePdAcct(self):
		return self._PrePdAcct

	@PrePdAcct.setter
	def PrePdAcct(self, value):
		self._PrePdAcct = value if type(value) != base_types.auto else self.make_default("PrePdAcct")

	@PrePdAcct.deleter
	def PrePdAcct(self):
		del self._PrePdAcct
		self._PrePdAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtdNtry', type=CardAggregated2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=PaymentCard4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POI', type=PointOfInteraction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrePdAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
	))

