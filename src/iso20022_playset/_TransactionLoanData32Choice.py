# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LoanData143
from . import LoanData144
from . import LoanData145

class TransactionLoanData32Choice(base_types._BaseFieldType):

	__slots__ = ["_BuySellBck", "_RpTrad", "_SctiesLndg"]
	@property
	def BuySellBck(self):
		return self._BuySellBck

	@BuySellBck.setter
	def BuySellBck(self, value):
		self._BuySellBck = value if value is not None else base_types.UninitialisedField(self, 'BuySellBck', LoanData144, False)

	@BuySellBck.deleter
	def BuySellBck(self):
		del self._BuySellBck
		self._BuySellBck = base_types.UninitialisedField(self, 'BuySellBck', LoanData144, False)

	@property
	def RpTrad(self):
		return self._RpTrad

	@RpTrad.setter
	def RpTrad(self, value):
		self._RpTrad = value if value is not None else base_types.UninitialisedField(self, 'RpTrad', LoanData143, False)

	@RpTrad.deleter
	def RpTrad(self):
		del self._RpTrad
		self._RpTrad = base_types.UninitialisedField(self, 'RpTrad', LoanData143, False)

	@property
	def SctiesLndg(self):
		return self._SctiesLndg

	@SctiesLndg.setter
	def SctiesLndg(self, value):
		self._SctiesLndg = value if value is not None else base_types.UninitialisedField(self, 'SctiesLndg', LoanData145, False)

	@SctiesLndg.deleter
	def SctiesLndg(self):
		del self._SctiesLndg
		self._SctiesLndg = base_types.UninitialisedField(self, 'SctiesLndg', LoanData145, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuySellBck', type=LoanData144, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RpTrad', type=LoanData143, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesLndg', type=LoanData145, min=0, max=1, mutex_group=1, array=False),
	))