from . import base_types
from ._PartyIdentification63 import PartyIdentification63
from ._ActiveCurrencyCode import ActiveCurrencyCode

class PartyOrCurrency1Choice(base_types._BaseFieldType):

	__slots__ = ["_Dpstry", "_SttlmCcy"]
	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if type(value) != base_types.auto else self.make_default("Dpstry")

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != base_types.auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification63, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=1, array=False),
	))

