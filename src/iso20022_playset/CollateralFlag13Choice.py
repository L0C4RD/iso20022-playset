from . import base_types
from .CollaterisedData12 import CollaterisedData12
from .NoReasonCode import NoReasonCode

class CollateralFlag13Choice(base_types._BaseFieldType):

	__slots__ = ["_Uncollsd", "_Collsd"]
	@property
	def Uncollsd(self):
		return self._Uncollsd

	@Uncollsd.setter
	def Uncollsd(self, value):
		self._Uncollsd = value if type(value) != auto else self.make_default("Uncollsd")

	@Uncollsd.deleter
	def Uncollsd(self):
		del self._Uncollsd
		self._Uncollsd = None

	@property
	def Collsd(self):
		return self._Collsd

	@Collsd.setter
	def Collsd(self, value):
		self._Collsd = value if type(value) != auto else self.make_default("Collsd")

	@Collsd.deleter
	def Collsd(self):
		del self._Collsd
		self._Collsd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Uncollsd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Collsd', type=CollaterisedData12, min=0, max=1, mutex_group=1, array=False),
	))

