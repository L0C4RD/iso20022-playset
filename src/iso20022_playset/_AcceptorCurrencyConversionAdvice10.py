# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentEnvironment82 import CardPaymentEnvironment82
from ._CardPaymentTransaction154 import CardPaymentTransaction154
from ._CurrencyConversion35 import CurrencyConversion35

class AcceptorCurrencyConversionAdvice10(base_types._BaseFieldType):

	__slots__ = ["_CcyConvsRslt", "_Envt", "_Tx"]
	@property
	def CcyConvsRslt(self):
		return self._CcyConvsRslt

	@CcyConvsRslt.setter
	def CcyConvsRslt(self, value):
		self._CcyConvsRslt = value if type(value) != base_types.auto else self.make_default("CcyConvsRslt")

	@CcyConvsRslt.deleter
	def CcyConvsRslt(self):
		del self._CcyConvsRslt
		self._CcyConvsRslt = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyConvsRslt', type=CurrencyConversion35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction154, min=1, max=1, mutex_group=None, array=False),
	))