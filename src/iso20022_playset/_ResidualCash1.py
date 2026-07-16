# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import YesNoIndicator

class ResidualCash1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_RsdlCshInd"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def RsdlCshInd(self):
		return self._RsdlCshInd

	@RsdlCshInd.setter
	def RsdlCshInd(self, value):
		self._RsdlCshInd = value if value is not None else base_types.UninitialisedField(self, 'RsdlCshInd', YesNoIndicator, False)

	@RsdlCshInd.deleter
	def RsdlCshInd(self):
		del self._RsdlCshInd
		self._RsdlCshInd = base_types.UninitialisedField(self, 'RsdlCshInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsdlCshInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))