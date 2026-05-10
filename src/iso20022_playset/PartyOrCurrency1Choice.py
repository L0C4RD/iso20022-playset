import base_types
import PartyIdentification63
import ActiveCurrencyCode

class PartyOrCurrency1Choice(base_types._BaseFieldType):

	__slots__ = ["_SttlmCcy", "_Dpstry"]
	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if type(value) != auto else self.make_default("Dpstry")

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification63, min=0, max=1, mutex_group=1, array=False),
	))

