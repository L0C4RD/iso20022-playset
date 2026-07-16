# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import GenericIdentification165

class IntraDayRequirement1(base_types._BaseFieldType):

	__slots__ = ["_AggtPeakLblty", "_IntraDayMrgnCall", "_MrgnAcctId", "_PeakInitlMrgnLblty", "_PeakVartnMrgnLblty"]
	@property
	def AggtPeakLblty(self):
		return self._AggtPeakLblty

	@AggtPeakLblty.setter
	def AggtPeakLblty(self, value):
		self._AggtPeakLblty = value if value is not None else base_types.UninitialisedField(self, 'AggtPeakLblty', ActiveCurrencyAndAmount, False)

	@AggtPeakLblty.deleter
	def AggtPeakLblty(self):
		del self._AggtPeakLblty
		self._AggtPeakLblty = base_types.UninitialisedField(self, 'AggtPeakLblty', ActiveCurrencyAndAmount, False)

	@property
	def IntraDayMrgnCall(self):
		return self._IntraDayMrgnCall

	@IntraDayMrgnCall.setter
	def IntraDayMrgnCall(self, value):
		self._IntraDayMrgnCall = value if value is not None else base_types.UninitialisedField(self, 'IntraDayMrgnCall', ActiveCurrencyAndAmount, False)

	@IntraDayMrgnCall.deleter
	def IntraDayMrgnCall(self):
		del self._IntraDayMrgnCall
		self._IntraDayMrgnCall = base_types.UninitialisedField(self, 'IntraDayMrgnCall', ActiveCurrencyAndAmount, False)

	@property
	def MrgnAcctId(self):
		return self._MrgnAcctId

	@MrgnAcctId.setter
	def MrgnAcctId(self, value):
		self._MrgnAcctId = value if value is not None else base_types.UninitialisedField(self, 'MrgnAcctId', GenericIdentification165, False)

	@MrgnAcctId.deleter
	def MrgnAcctId(self):
		del self._MrgnAcctId
		self._MrgnAcctId = base_types.UninitialisedField(self, 'MrgnAcctId', GenericIdentification165, False)

	@property
	def PeakInitlMrgnLblty(self):
		return self._PeakInitlMrgnLblty

	@PeakInitlMrgnLblty.setter
	def PeakInitlMrgnLblty(self, value):
		self._PeakInitlMrgnLblty = value if value is not None else base_types.UninitialisedField(self, 'PeakInitlMrgnLblty', ActiveCurrencyAndAmount, False)

	@PeakInitlMrgnLblty.deleter
	def PeakInitlMrgnLblty(self):
		del self._PeakInitlMrgnLblty
		self._PeakInitlMrgnLblty = base_types.UninitialisedField(self, 'PeakInitlMrgnLblty', ActiveCurrencyAndAmount, False)

	@property
	def PeakVartnMrgnLblty(self):
		return self._PeakVartnMrgnLblty

	@PeakVartnMrgnLblty.setter
	def PeakVartnMrgnLblty(self, value):
		self._PeakVartnMrgnLblty = value if value is not None else base_types.UninitialisedField(self, 'PeakVartnMrgnLblty', ActiveCurrencyAndAmount, False)

	@PeakVartnMrgnLblty.deleter
	def PeakVartnMrgnLblty(self):
		del self._PeakVartnMrgnLblty
		self._PeakVartnMrgnLblty = base_types.UninitialisedField(self, 'PeakVartnMrgnLblty', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtPeakLblty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraDayMrgnCall', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnAcctId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PeakInitlMrgnLblty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PeakVartnMrgnLblty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))