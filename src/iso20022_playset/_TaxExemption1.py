# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max210Text import Max210Text

class TaxExemption1(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_XmptdAmt"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def XmptdAmt(self):
		return self._XmptdAmt

	@XmptdAmt.setter
	def XmptdAmt(self, value):
		self._XmptdAmt = value if type(value) != base_types.auto else self.make_default("XmptdAmt")

	@XmptdAmt.deleter
	def XmptdAmt(self):
		del self._XmptdAmt
		self._XmptdAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))