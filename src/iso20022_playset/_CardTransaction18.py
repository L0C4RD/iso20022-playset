# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardTransaction3Choice
from . import CashAccount40
from . import PaymentCard4
from . import PointOfInteraction1

class CardTransaction18(base_types._BaseFieldType):

	__slots__ = ["_Card", "_POI", "_PrePdAcct", "_Tx"]
	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if value is not None else base_types.UninitialisedField(self, 'Card', PaymentCard4, False)

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = base_types.UninitialisedField(self, 'Card', PaymentCard4, False)

	@property
	def POI(self):
		return self._POI

	@POI.setter
	def POI(self, value):
		self._POI = value if value is not None else base_types.UninitialisedField(self, 'POI', PointOfInteraction1, False)

	@POI.deleter
	def POI(self):
		del self._POI
		self._POI = base_types.UninitialisedField(self, 'POI', PointOfInteraction1, False)

	@property
	def PrePdAcct(self):
		return self._PrePdAcct

	@PrePdAcct.setter
	def PrePdAcct(self, value):
		self._PrePdAcct = value if value is not None else base_types.UninitialisedField(self, 'PrePdAcct', CashAccount40, False)

	@PrePdAcct.deleter
	def PrePdAcct(self):
		del self._PrePdAcct
		self._PrePdAcct = base_types.UninitialisedField(self, 'PrePdAcct', CashAccount40, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', CardTransaction3Choice, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', CardTransaction3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Card', type=PaymentCard4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POI', type=PointOfInteraction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrePdAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=CardTransaction3Choice, min=0, max=1, mutex_group=None, array=False),
	))