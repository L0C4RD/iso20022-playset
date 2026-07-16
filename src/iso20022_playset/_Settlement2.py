# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection27
from . import PartyIdentification255Choice

class Settlement2(base_types._BaseFieldType):

	__slots__ = ["_Dpstry", "_SttlmAmt"]
	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if value is not None else base_types.UninitialisedField(self, 'Dpstry', PartyIdentification255Choice, False)

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = base_types.UninitialisedField(self, 'Dpstry', PartyIdentification255Choice, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection27, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection27, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification255Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection27, min=1, max=1, mutex_group=None, array=False),
	))