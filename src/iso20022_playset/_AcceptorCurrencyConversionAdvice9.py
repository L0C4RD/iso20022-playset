# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment81
from . import CardPaymentTransaction137
from . import CurrencyConversion30

class AcceptorCurrencyConversionAdvice9(base_types._BaseFieldType):

	__slots__ = ["_CcyConvsRslt", "_Envt", "_Tx"]
	@property
	def CcyConvsRslt(self):
		return self._CcyConvsRslt

	@CcyConvsRslt.setter
	def CcyConvsRslt(self, value):
		self._CcyConvsRslt = value if value is not None else base_types.UninitialisedField(self, 'CcyConvsRslt', CurrencyConversion30, False)

	@CcyConvsRslt.deleter
	def CcyConvsRslt(self):
		del self._CcyConvsRslt
		self._CcyConvsRslt = base_types.UninitialisedField(self, 'CcyConvsRslt', CurrencyConversion30, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment81, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment81, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', CardPaymentTransaction137, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', CardPaymentTransaction137, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyConvsRslt', type=CurrencyConversion30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction137, min=1, max=1, mutex_group=None, array=False),
	))