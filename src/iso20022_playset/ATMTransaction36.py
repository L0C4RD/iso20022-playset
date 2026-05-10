from . import base_types
from .ATMReconciliationOperation1 import ATMReconciliationOperation1

class ATMTransaction36(base_types._BaseFieldType):

	__slots__ = ["_RcncltnOpr"]
	@property
	def RcncltnOpr(self):
		return self._RcncltnOpr

	@RcncltnOpr.setter
	def RcncltnOpr(self, value):
		self._RcncltnOpr = value if type(value) != auto else self.make_default("RcncltnOpr")

	@RcncltnOpr.deleter
	def RcncltnOpr(self):
		del self._RcncltnOpr
		self._RcncltnOpr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcncltnOpr', type=ATMReconciliationOperation1, min=0, max=None, mutex_group=None, array=True),
	))

