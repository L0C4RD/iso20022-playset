# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max210Text

class TaxExemption1(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_XmptdAmt"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max210Text, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max210Text, False)

	@property
	def XmptdAmt(self):
		return self._XmptdAmt

	@XmptdAmt.setter
	def XmptdAmt(self, value):
		self._XmptdAmt = value if value is not None else base_types.UninitialisedField(self, 'XmptdAmt', ActiveCurrencyAndAmount, False)

	@XmptdAmt.deleter
	def XmptdAmt(self):
		del self._XmptdAmt
		self._XmptdAmt = base_types.UninitialisedField(self, 'XmptdAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))