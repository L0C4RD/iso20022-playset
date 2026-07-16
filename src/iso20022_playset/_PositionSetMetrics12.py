# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import QuantityNominalValue2Choice
from . import VolumeMetrics6

class PositionSetMetrics12(base_types._BaseFieldType):

	__slots__ = ["_HrcutOrMrgn", "_QtyOrNmnlAmt", "_VolMtrcs"]
	@property
	def HrcutOrMrgn(self):
		return self._HrcutOrMrgn

	@HrcutOrMrgn.setter
	def HrcutOrMrgn(self, value):
		self._HrcutOrMrgn = value if value is not None else base_types.UninitialisedField(self, 'HrcutOrMrgn', PercentageRate, False)

	@HrcutOrMrgn.deleter
	def HrcutOrMrgn(self):
		del self._HrcutOrMrgn
		self._HrcutOrMrgn = base_types.UninitialisedField(self, 'HrcutOrMrgn', PercentageRate, False)

	@property
	def QtyOrNmnlAmt(self):
		return self._QtyOrNmnlAmt

	@QtyOrNmnlAmt.setter
	def QtyOrNmnlAmt(self, value):
		self._QtyOrNmnlAmt = value if value is not None else base_types.UninitialisedField(self, 'QtyOrNmnlAmt', QuantityNominalValue2Choice, False)

	@QtyOrNmnlAmt.deleter
	def QtyOrNmnlAmt(self):
		del self._QtyOrNmnlAmt
		self._QtyOrNmnlAmt = base_types.UninitialisedField(self, 'QtyOrNmnlAmt', QuantityNominalValue2Choice, False)

	@property
	def VolMtrcs(self):
		return self._VolMtrcs

	@VolMtrcs.setter
	def VolMtrcs(self, value):
		self._VolMtrcs = value if value is not None else base_types.UninitialisedField(self, 'VolMtrcs', VolumeMetrics6, False)

	@VolMtrcs.deleter
	def VolMtrcs(self):
		del self._VolMtrcs
		self._VolMtrcs = base_types.UninitialisedField(self, 'VolMtrcs', VolumeMetrics6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HrcutOrMrgn', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyOrNmnlAmt', type=QuantityNominalValue2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VolMtrcs', type=VolumeMetrics6, min=0, max=1, mutex_group=None, array=False),
	))