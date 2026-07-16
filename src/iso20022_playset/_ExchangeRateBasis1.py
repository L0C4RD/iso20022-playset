# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode

class ExchangeRateBasis1(base_types._BaseFieldType):

	__slots__ = ["_BaseCcy", "_QtdCcy"]
	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if value is not None else base_types.UninitialisedField(self, 'BaseCcy', ActiveCurrencyCode, False)

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = base_types.UninitialisedField(self, 'BaseCcy', ActiveCurrencyCode, False)

	@property
	def QtdCcy(self):
		return self._QtdCcy

	@QtdCcy.setter
	def QtdCcy(self, value):
		self._QtdCcy = value if value is not None else base_types.UninitialisedField(self, 'QtdCcy', ActiveCurrencyCode, False)

	@QtdCcy.deleter
	def QtdCcy(self):
		del self._QtdCcy
		self._QtdCcy = base_types.UninitialisedField(self, 'QtdCcy', ActiveCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtdCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))