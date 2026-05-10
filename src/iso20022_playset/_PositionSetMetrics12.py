from . import base_types
from ._PercentageRate import PercentageRate
from ._QuantityNominalValue2Choice import QuantityNominalValue2Choice
from ._VolumeMetrics6 import VolumeMetrics6

class PositionSetMetrics12(base_types._BaseFieldType):

	__slots__ = ["_HrcutOrMrgn", "_QtyOrNmnlAmt", "_VolMtrcs"]
	@property
	def HrcutOrMrgn(self):
		return self._HrcutOrMrgn

	@HrcutOrMrgn.setter
	def HrcutOrMrgn(self, value):
		self._HrcutOrMrgn = value if type(value) != base_types.auto else self.make_default("HrcutOrMrgn")

	@HrcutOrMrgn.deleter
	def HrcutOrMrgn(self):
		del self._HrcutOrMrgn
		self._HrcutOrMrgn = None

	@property
	def QtyOrNmnlAmt(self):
		return self._QtyOrNmnlAmt

	@QtyOrNmnlAmt.setter
	def QtyOrNmnlAmt(self, value):
		self._QtyOrNmnlAmt = value if type(value) != base_types.auto else self.make_default("QtyOrNmnlAmt")

	@QtyOrNmnlAmt.deleter
	def QtyOrNmnlAmt(self):
		del self._QtyOrNmnlAmt
		self._QtyOrNmnlAmt = None

	@property
	def VolMtrcs(self):
		return self._VolMtrcs

	@VolMtrcs.setter
	def VolMtrcs(self, value):
		self._VolMtrcs = value if type(value) != base_types.auto else self.make_default("VolMtrcs")

	@VolMtrcs.deleter
	def VolMtrcs(self):
		del self._VolMtrcs
		self._VolMtrcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HrcutOrMrgn', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyOrNmnlAmt', type=QuantityNominalValue2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VolMtrcs', type=VolumeMetrics6, min=0, max=1, mutex_group=None, array=False),
	))

