# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UnderlyingPaymentInstruction9
from . import UnderlyingPaymentTransaction8
from . import UnderlyingStatementEntry3

class UnderlyingTransaction8Choice(base_types._BaseFieldType):

	__slots__ = ["_Initn", "_IntrBk", "_StmtNtry"]
	@property
	def Initn(self):
		return self._Initn

	@Initn.setter
	def Initn(self, value):
		self._Initn = value if value is not None else base_types.UninitialisedField(self, 'Initn', UnderlyingPaymentInstruction9, False)

	@Initn.deleter
	def Initn(self):
		del self._Initn
		self._Initn = base_types.UninitialisedField(self, 'Initn', UnderlyingPaymentInstruction9, False)

	@property
	def IntrBk(self):
		return self._IntrBk

	@IntrBk.setter
	def IntrBk(self, value):
		self._IntrBk = value if value is not None else base_types.UninitialisedField(self, 'IntrBk', UnderlyingPaymentTransaction8, False)

	@IntrBk.deleter
	def IntrBk(self):
		del self._IntrBk
		self._IntrBk = base_types.UninitialisedField(self, 'IntrBk', UnderlyingPaymentTransaction8, False)

	@property
	def StmtNtry(self):
		return self._StmtNtry

	@StmtNtry.setter
	def StmtNtry(self, value):
		self._StmtNtry = value if value is not None else base_types.UninitialisedField(self, 'StmtNtry', UnderlyingStatementEntry3, False)

	@StmtNtry.deleter
	def StmtNtry(self):
		del self._StmtNtry
		self._StmtNtry = base_types.UninitialisedField(self, 'StmtNtry', UnderlyingStatementEntry3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Initn', type=UnderlyingPaymentInstruction9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrBk', type=UnderlyingPaymentTransaction8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtNtry', type=UnderlyingStatementEntry3, min=0, max=1, mutex_group=1, array=False),
	))