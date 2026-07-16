# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount

class AdditionalAmount1Choice(base_types._BaseFieldType):

	__slots__ = ["_AddtlCshIn", "_RsltgCshOut"]
	@property
	def AddtlCshIn(self):
		return self._AddtlCshIn

	@AddtlCshIn.setter
	def AddtlCshIn(self, value):
		self._AddtlCshIn = value if value is not None else base_types.UninitialisedField(self, 'AddtlCshIn', ActiveOrHistoricCurrencyAndAmount, False)

	@AddtlCshIn.deleter
	def AddtlCshIn(self):
		del self._AddtlCshIn
		self._AddtlCshIn = base_types.UninitialisedField(self, 'AddtlCshIn', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def RsltgCshOut(self):
		return self._RsltgCshOut

	@RsltgCshOut.setter
	def RsltgCshOut(self, value):
		self._RsltgCshOut = value if value is not None else base_types.UninitialisedField(self, 'RsltgCshOut', ActiveOrHistoricCurrencyAndAmount, False)

	@RsltgCshOut.deleter
	def RsltgCshOut(self):
		del self._RsltgCshOut
		self._RsltgCshOut = base_types.UninitialisedField(self, 'RsltgCshOut', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlCshIn', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RsltgCshOut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))