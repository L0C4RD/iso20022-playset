# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CurrencyConversion32 import CurrencyConversion32
from ._CurrencyConversionResponse2Code import CurrencyConversionResponse2Code
from ._Max35Text import Max35Text

class CurrencyConversion33(base_types._BaseFieldType):

	__slots__ = ["_Convs", "_Rslt", "_RsltRsn"]
	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if type(value) != base_types.auto else self.make_default("Convs")

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != base_types.auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def RsltRsn(self):
		return self._RsltRsn

	@RsltRsn.setter
	def RsltRsn(self, value):
		self._RsltRsn = value if type(value) != base_types.auto else self.make_default("RsltRsn")

	@RsltRsn.deleter
	def RsltRsn(self):
		del self._RsltRsn
		self._RsltRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Convs', type=CurrencyConversion32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=CurrencyConversionResponse2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))