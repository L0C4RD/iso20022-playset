from . import base_types
import CashAccount40
import PaymentCard4
import CardTransaction3Choice
import PointOfInteraction1

class CardTransaction18(base_types._BaseFieldType):

	__slots__ = ["_POI", "_Tx", "_PrePdAcct", "_Card"]
	@property
	def POI(self):
		return self._POI

	@POI.setter
	def POI(self, value):
		self._POI = value if type(value) != auto else self.make_default("POI")

	@POI.deleter
	def POI(self):
		del self._POI
		self._POI = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	@property
	def PrePdAcct(self):
		return self._PrePdAcct

	@PrePdAcct.setter
	def PrePdAcct(self, value):
		self._PrePdAcct = value if type(value) != auto else self.make_default("PrePdAcct")

	@PrePdAcct.deleter
	def PrePdAcct(self):
		del self._PrePdAcct
		self._PrePdAcct = None

	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if type(value) != auto else self.make_default("Card")

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POI', type=PointOfInteraction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=CardTransaction3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrePdAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=PaymentCard4, min=0, max=1, mutex_group=None, array=False),
	))

