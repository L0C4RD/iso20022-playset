from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .InterestMethod1Code import InterestMethod1Code
from .ISODate import ISODate
from .CollateralBalance1 import CollateralBalance1

class InterestResult1(base_types._BaseFieldType):

	__slots__ = ["_IntrstDueToA", "_IntrstDueToB", "_ClsgCollBal", "_ValDt", "_OpngCollBal", "_IntrstMtd"]
	@property
	def IntrstDueToA(self):
		return self._IntrstDueToA

	@IntrstDueToA.setter
	def IntrstDueToA(self, value):
		self._IntrstDueToA = value if type(value) != base_types.auto else self.make_default("IntrstDueToA")

	@IntrstDueToA.deleter
	def IntrstDueToA(self):
		del self._IntrstDueToA
		self._IntrstDueToA = None

	@property
	def IntrstDueToB(self):
		return self._IntrstDueToB

	@IntrstDueToB.setter
	def IntrstDueToB(self, value):
		self._IntrstDueToB = value if type(value) != base_types.auto else self.make_default("IntrstDueToB")

	@IntrstDueToB.deleter
	def IntrstDueToB(self):
		del self._IntrstDueToB
		self._IntrstDueToB = None

	@property
	def ClsgCollBal(self):
		return self._ClsgCollBal

	@ClsgCollBal.setter
	def ClsgCollBal(self, value):
		self._ClsgCollBal = value if type(value) != base_types.auto else self.make_default("ClsgCollBal")

	@ClsgCollBal.deleter
	def ClsgCollBal(self):
		del self._ClsgCollBal
		self._ClsgCollBal = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def OpngCollBal(self):
		return self._OpngCollBal

	@OpngCollBal.setter
	def OpngCollBal(self, value):
		self._OpngCollBal = value if type(value) != base_types.auto else self.make_default("OpngCollBal")

	@OpngCollBal.deleter
	def OpngCollBal(self):
		del self._OpngCollBal
		self._OpngCollBal = None

	@property
	def IntrstMtd(self):
		return self._IntrstMtd

	@IntrstMtd.setter
	def IntrstMtd(self, value):
		self._IntrstMtd = value if type(value) != base_types.auto else self.make_default("IntrstMtd")

	@IntrstMtd.deleter
	def IntrstMtd(self):
		del self._IntrstMtd
		self._IntrstMtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstDueToA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstDueToB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgCollBal', type=CollateralBalance1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngCollBal', type=CollateralBalance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstMtd', type=InterestMethod1Code, min=1, max=1, mutex_group=None, array=False),
	))

