# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class MarginResult1Choice(base_types._BaseFieldType):

	__slots__ = ["_DfcitAmt", "_XcssAmt"]
	@property
	def DfcitAmt(self):
		return self._DfcitAmt

	@DfcitAmt.setter
	def DfcitAmt(self, value):
		self._DfcitAmt = value if value is not None else base_types.UninitialisedField(self, 'DfcitAmt', ActiveCurrencyAndAmount, False)

	@DfcitAmt.deleter
	def DfcitAmt(self):
		del self._DfcitAmt
		self._DfcitAmt = base_types.UninitialisedField(self, 'DfcitAmt', ActiveCurrencyAndAmount, False)

	@property
	def XcssAmt(self):
		return self._XcssAmt

	@XcssAmt.setter
	def XcssAmt(self, value):
		self._XcssAmt = value if value is not None else base_types.UninitialisedField(self, 'XcssAmt', ActiveCurrencyAndAmount, False)

	@XcssAmt.deleter
	def XcssAmt(self):
		del self._XcssAmt
		self._XcssAmt = base_types.UninitialisedField(self, 'XcssAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfcitAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XcssAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))