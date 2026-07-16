# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMReconciliationOperation1

class ATMTransaction36(base_types._BaseFieldType):

	__slots__ = ["_RcncltnOpr"]
	@property
	def RcncltnOpr(self):
		return self._RcncltnOpr

	@RcncltnOpr.setter
	def RcncltnOpr(self, value):
		self._RcncltnOpr = value if value is not None else base_types.UninitialisedField(self, 'RcncltnOpr', ATMReconciliationOperation1, True)

	@RcncltnOpr.deleter
	def RcncltnOpr(self):
		del self._RcncltnOpr
		self._RcncltnOpr = base_types.UninitialisedField(self, 'RcncltnOpr', ATMReconciliationOperation1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcncltnOpr', type=ATMReconciliationOperation1, min=0, max=None, mutex_group=None, array=True),
	))