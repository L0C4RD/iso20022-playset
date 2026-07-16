# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import PartyIdentification63

class PartyOrCurrency1Choice(base_types._BaseFieldType):

	__slots__ = ["_Dpstry", "_SttlmCcy"]
	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if value is not None else base_types.UninitialisedField(self, 'Dpstry', PartyIdentification63, False)

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = base_types.UninitialisedField(self, 'Dpstry', PartyIdentification63, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification63, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=1, array=False),
	))