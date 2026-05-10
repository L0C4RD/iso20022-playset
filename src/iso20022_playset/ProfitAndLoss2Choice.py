from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class ProfitAndLoss2Choice(base_types._BaseFieldType):

	__slots__ = ["_Loss", "_Prft"]
	@property
	def Loss(self):
		return self._Loss

	@Loss.setter
	def Loss(self, value):
		self._Loss = value if type(value) != auto else self.make_default("Loss")

	@Loss.deleter
	def Loss(self):
		del self._Loss
		self._Loss = None

	@property
	def Prft(self):
		return self._Prft

	@Prft.setter
	def Prft(self, value):
		self._Prft = value if type(value) != auto else self.make_default("Prft")

	@Prft.deleter
	def Prft(self):
		del self._Prft
		self._Prft = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Loss', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prft', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))

