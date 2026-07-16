# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import YesNoIndicator

class DerivativeBasicAttributes1(base_types._BaseFieldType):

	__slots__ = ["_IntrstInclInPric", "_NtnlCcyAndAmt"]
	@property
	def IntrstInclInPric(self):
		return self._IntrstInclInPric

	@IntrstInclInPric.setter
	def IntrstInclInPric(self, value):
		self._IntrstInclInPric = value if value is not None else base_types.UninitialisedField(self, 'IntrstInclInPric', YesNoIndicator, False)

	@IntrstInclInPric.deleter
	def IntrstInclInPric(self):
		del self._IntrstInclInPric
		self._IntrstInclInPric = base_types.UninitialisedField(self, 'IntrstInclInPric', YesNoIndicator, False)

	@property
	def NtnlCcyAndAmt(self):
		return self._NtnlCcyAndAmt

	@NtnlCcyAndAmt.setter
	def NtnlCcyAndAmt(self, value):
		self._NtnlCcyAndAmt = value if value is not None else base_types.UninitialisedField(self, 'NtnlCcyAndAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@NtnlCcyAndAmt.deleter
	def NtnlCcyAndAmt(self):
		del self._NtnlCcyAndAmt
		self._NtnlCcyAndAmt = base_types.UninitialisedField(self, 'NtnlCcyAndAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstInclInPric', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlCcyAndAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))