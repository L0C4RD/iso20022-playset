# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class ProfitAndLoss2Choice(base_types._BaseFieldType):

	__slots__ = ["_Loss", "_Prft"]
	@property
	def Loss(self):
		return self._Loss

	@Loss.setter
	def Loss(self, value):
		self._Loss = value if value is not None else base_types.UninitialisedField(self, 'Loss', ActiveCurrencyAndAmount, False)

	@Loss.deleter
	def Loss(self):
		del self._Loss
		self._Loss = base_types.UninitialisedField(self, 'Loss', ActiveCurrencyAndAmount, False)

	@property
	def Prft(self):
		return self._Prft

	@Prft.setter
	def Prft(self, value):
		self._Prft = value if value is not None else base_types.UninitialisedField(self, 'Prft', ActiveCurrencyAndAmount, False)

	@Prft.deleter
	def Prft(self):
		del self._Prft
		self._Prft = base_types.UninitialisedField(self, 'Prft', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Loss', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prft', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))