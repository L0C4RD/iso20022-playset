from . import base_types
from ._PartyIdentification255Choice import PartyIdentification255Choice
from ._AmountAndDirection27 import AmountAndDirection27

class Settlement2(base_types._BaseFieldType):

	__slots__ = ["_SttlmAmt", "_Dpstry"]
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
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification255Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection27, min=1, max=1, mutex_group=None, array=False),
	))

