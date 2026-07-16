# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyConversion29
from . import CurrencyConversionResponse3Code
from . import Max35Text

class CurrencyConversion31(base_types._BaseFieldType):

	__slots__ = ["_ConvsDtls", "_Rslt", "_RsltRsn"]
	@property
	def ConvsDtls(self):
		return self._ConvsDtls

	@ConvsDtls.setter
	def ConvsDtls(self, value):
		self._ConvsDtls = value if value is not None else base_types.UninitialisedField(self, 'ConvsDtls', CurrencyConversion29, True)

	@ConvsDtls.deleter
	def ConvsDtls(self):
		del self._ConvsDtls
		self._ConvsDtls = base_types.UninitialisedField(self, 'ConvsDtls', CurrencyConversion29, True)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', CurrencyConversionResponse3Code, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', CurrencyConversionResponse3Code, False)

	@property
	def RsltRsn(self):
		return self._RsltRsn

	@RsltRsn.setter
	def RsltRsn(self, value):
		self._RsltRsn = value if value is not None else base_types.UninitialisedField(self, 'RsltRsn', Max35Text, False)

	@RsltRsn.deleter
	def RsltRsn(self):
		del self._RsltRsn
		self._RsltRsn = base_types.UninitialisedField(self, 'RsltRsn', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConvsDtls', type=CurrencyConversion29, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rslt', type=CurrencyConversionResponse3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))