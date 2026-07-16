# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionMovementDetails20
from . import SafekeepingPlaceFormat39Choice
from . import SecuritiesBalanceType8Choice

class IntraPositionDetails63(base_types._BaseFieldType):

	__slots__ = ["_BalFr", "_IntraPosMvmnt", "_SfkpgPlc"]
	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if value is not None else base_types.UninitialisedField(self, 'BalFr', SecuritiesBalanceType8Choice, False)

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = base_types.UninitialisedField(self, 'BalFr', SecuritiesBalanceType8Choice, False)

	@property
	def IntraPosMvmnt(self):
		return self._IntraPosMvmnt

	@IntraPosMvmnt.setter
	def IntraPosMvmnt(self, value):
		self._IntraPosMvmnt = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmnt', IntraPositionMovementDetails20, True)

	@IntraPosMvmnt.deleter
	def IntraPosMvmnt(self):
		del self._IntraPosMvmnt
		self._IntraPosMvmnt = base_types.UninitialisedField(self, 'IntraPosMvmnt', IntraPositionMovementDetails20, True)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat39Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat39Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalFr', type=SecuritiesBalanceType8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraPosMvmnt', type=IntraPositionMovementDetails20, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat39Choice, min=0, max=1, mutex_group=None, array=False),
	))