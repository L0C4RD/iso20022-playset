import base_types
import BillingMethod1
import BillingMethod3
import BillingMethod2

class BillingMethod1Choice(base_types._BaseFieldType):

	__slots__ = ["_MtdD", "_MtdA", "_MtdB"]
	@property
	def MtdD(self):
		return self._MtdD

	@MtdD.setter
	def MtdD(self, value):
		self._MtdD = value if type(value) != auto else self.make_default("MtdD")

	@MtdD.deleter
	def MtdD(self):
		del self._MtdD
		self._MtdD = None

	@property
	def MtdA(self):
		return self._MtdA

	@MtdA.setter
	def MtdA(self, value):
		self._MtdA = value if type(value) != auto else self.make_default("MtdA")

	@MtdA.deleter
	def MtdA(self):
		del self._MtdA
		self._MtdA = None

	@property
	def MtdB(self):
		return self._MtdB

	@MtdB.setter
	def MtdB(self, value):
		self._MtdB = value if type(value) != auto else self.make_default("MtdB")

	@MtdB.deleter
	def MtdB(self):
		del self._MtdB
		self._MtdB = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtdD', type=BillingMethod3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtdA', type=BillingMethod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtdB', type=BillingMethod2, min=0, max=1, mutex_group=1, array=False),
	))

