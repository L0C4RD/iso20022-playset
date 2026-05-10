import base_types
import IntraPositionMovementDetails21
import SecuritiesBalanceType6Choice
import SafekeepingPlaceFormat41Choice

class IntraPositionDetails66(base_types._BaseFieldType):

	__slots__ = ["_BalFr", "_SfkpgPlc", "_IntraPosMvmnt"]
	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if type(value) != auto else self.make_default("BalFr")

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def IntraPosMvmnt(self):
		return self._IntraPosMvmnt

	@IntraPosMvmnt.setter
	def IntraPosMvmnt(self, value):
		self._IntraPosMvmnt = value if type(value) != auto else self.make_default("IntraPosMvmnt")

	@IntraPosMvmnt.deleter
	def IntraPosMvmnt(self):
		del self._IntraPosMvmnt
		self._IntraPosMvmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalFr', type=SecuritiesBalanceType6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraPosMvmnt', type=IntraPositionMovementDetails21, min=1, max=None, mutex_group=None, array=True),
	))

