from . import base_types
from ._TradeConfirmationType2Code import TradeConfirmationType2Code

class TradeNonConfirmation1(base_types._BaseFieldType):

	__slots__ = ["_Tp"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=TradeConfirmationType2Code, min=1, max=1, mutex_group=None, array=False),
	))

