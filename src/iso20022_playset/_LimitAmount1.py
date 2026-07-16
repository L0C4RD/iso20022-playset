# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebitAmount1

class LimitAmount1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AvlblAmt", "_UtlstnAmt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', CreditDebitAmount1, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', CreditDebitAmount1, False)

	@property
	def AvlblAmt(self):
		return self._AvlblAmt

	@AvlblAmt.setter
	def AvlblAmt(self, value):
		self._AvlblAmt = value if value is not None else base_types.UninitialisedField(self, 'AvlblAmt', CreditDebitAmount1, False)

	@AvlblAmt.deleter
	def AvlblAmt(self):
		del self._AvlblAmt
		self._AvlblAmt = base_types.UninitialisedField(self, 'AvlblAmt', CreditDebitAmount1, False)

	@property
	def UtlstnAmt(self):
		return self._UtlstnAmt

	@UtlstnAmt.setter
	def UtlstnAmt(self, value):
		self._UtlstnAmt = value if value is not None else base_types.UninitialisedField(self, 'UtlstnAmt', CreditDebitAmount1, False)

	@UtlstnAmt.deleter
	def UtlstnAmt(self):
		del self._UtlstnAmt
		self._UtlstnAmt = base_types.UninitialisedField(self, 'UtlstnAmt', CreditDebitAmount1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=CreditDebitAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvlblAmt', type=CreditDebitAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UtlstnAmt', type=CreditDebitAmount1, min=1, max=1, mutex_group=None, array=False),
	))