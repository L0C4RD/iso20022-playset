import base_types
import ActiveCurrencyAnd24Amount
import PositiveNumber

class OpenInterest1(base_types._BaseFieldType):

	__slots__ = ["_GrssNtnlAmt", "_NbOfLots"]
	@property
	def GrssNtnlAmt(self):
		return self._GrssNtnlAmt

	@GrssNtnlAmt.setter
	def GrssNtnlAmt(self, value):
		self._GrssNtnlAmt = value if type(value) != auto else self.make_default("GrssNtnlAmt")

	@GrssNtnlAmt.deleter
	def GrssNtnlAmt(self):
		del self._GrssNtnlAmt
		self._GrssNtnlAmt = None

	@property
	def NbOfLots(self):
		return self._NbOfLots

	@NbOfLots.setter
	def NbOfLots(self, value):
		self._NbOfLots = value if type(value) != auto else self.make_default("NbOfLots")

	@NbOfLots.deleter
	def NbOfLots(self):
		del self._NbOfLots
		self._NbOfLots = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrssNtnlAmt', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfLots', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))

