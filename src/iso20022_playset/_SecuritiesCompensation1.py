from . import base_types
from ._PartyIdentification34Choice import PartyIdentification34Choice
from ._AmountAndDirection20 import AmountAndDirection20

class SecuritiesCompensation1(base_types._BaseFieldType):

	__slots__ = ["_Dpstry", "_SttlmAmt", "_Fees"]
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
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if type(value) != base_types.auto else self.make_default("Fees")

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = None

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
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification34Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fees', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
	))

