import base_types
import Intermediary29
import AggregateHoldingBalance1

class AggregateHoldingBalance3(base_types._BaseFieldType):

	__slots__ = ["_Agt", "_BalForAcct"]
	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

	@property
	def BalForAcct(self):
		return self._BalForAcct

	@BalForAcct.setter
	def BalForAcct(self, value):
		self._BalForAcct = value if type(value) != auto else self.make_default("BalForAcct")

	@BalForAcct.deleter
	def BalForAcct(self):
		del self._BalForAcct
		self._BalForAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Agt', type=Intermediary29, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalForAcct', type=AggregateHoldingBalance1, min=1, max=None, mutex_group=None, array=True),
	))

