# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardAggregated2
from . import CashAccount40
from . import PaymentCard4
from . import PointOfInteraction1

class CardEntry5(base_types._BaseFieldType):

	__slots__ = ["_AggtdNtry", "_Card", "_POI", "_PrePdAcct"]
	@property
	def AggtdNtry(self):
		return self._AggtdNtry

	@AggtdNtry.setter
	def AggtdNtry(self, value):
		self._AggtdNtry = value if value is not None else base_types.UninitialisedField(self, 'AggtdNtry', CardAggregated2, False)

	@AggtdNtry.deleter
	def AggtdNtry(self):
		del self._AggtdNtry
		self._AggtdNtry = base_types.UninitialisedField(self, 'AggtdNtry', CardAggregated2, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtdNtry', type=CardAggregated2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=PaymentCard4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POI', type=PointOfInteraction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrePdAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
	))