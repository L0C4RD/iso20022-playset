# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashSubBalanceTypeAndQuantityBreakdown3
from . import IntraBalancePosting6

class IntraBalancePosting5(base_types._BaseFieldType):

	__slots__ = ["_BalFr", "_Mvmnt"]
	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if value is not None else base_types.UninitialisedField(self, 'BalFr', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = base_types.UninitialisedField(self, 'BalFr', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@property
	def Mvmnt(self):
		return self._Mvmnt

	@Mvmnt.setter
	def Mvmnt(self, value):
		self._Mvmnt = value if value is not None else base_types.UninitialisedField(self, 'Mvmnt', IntraBalancePosting6, True)

	@Mvmnt.deleter
	def Mvmnt(self):
		del self._Mvmnt
		self._Mvmnt = base_types.UninitialisedField(self, 'Mvmnt', IntraBalancePosting6, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalFr', type=CashSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mvmnt', type=IntraBalancePosting6, min=1, max=None, mutex_group=None, array=True),
	))